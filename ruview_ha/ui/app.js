// ruview-ha-addon/ui/app.js
const BASE = window.location.origin;

// Tab switching
document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById(`tab-${btn.dataset.tab}`).classList.add('active');
  });
});

// Load nodes (inferred from zone signal data)
async function loadNodes() {
  const el = document.getElementById('node-list');
  try {
    const res = await fetch(`${BASE}/api/sensing/latest`);
    const data = await res.json();
    if (!data.zones.length) {
      el.innerHTML = '<p class="hint">No zones detected. Ensure ESP32 nodes are powered and flashed.</p>';
      return;
    }
    el.innerHTML = data.zones.map(z => `
      <div class="node-card">
        <strong>${z.zone_name}</strong>
        <span class="${z.signal_quality > 50 ? 'badge-online' : 'badge-offline'}">
          Signal: ${z.signal_quality}%
        </span>
      </div>
    `).join('');
  } catch {
    el.innerHTML = '<p class="hint">Could not reach RuView bridge.</p>';
  }
}

// Load zone config
async function loadZones() {
  const el = document.getElementById('zone-list');
  try {
    const res = await fetch(`${BASE}/api/sensing/latest`);
    const data = await res.json();
    el.innerHTML = data.zones.map(z => `
      <div class="zone-card">
        <strong>${z.zone_name}</strong> <small>(${z.zone_id})</small>
        <div class="status-row"><span>Presence</span><span>${z.presence ? '✓' : '—'}</span></div>
        <div class="status-row"><span>Fall Detection</span><span>${z.fall_detected ? '⚠' : '—'}</span></div>
        <div class="status-row"><span>Breathing</span><span>${z.breathing_rate ?? '—'} BPM</span></div>
        <div class="status-row"><span>Heart Rate</span><span>${z.heart_rate ?? '—'} BPM</span></div>
      </div>
    `).join('') || '<p class="hint">No zones configured.</p>';
  } catch {
    el.innerHTML = '<p class="hint">Could not load zone data.</p>';
  }
}

// Load system status
async function loadStatus() {
  const el = document.getElementById('status-panel');
  try {
    const res = await fetch(`${BASE}/health`);
    const data = await res.json();
    el.innerHTML = `
      <div class="status-row"><span>Bridge</span><span class="badge-online">${data.status}</span></div>
      <div class="status-row"><span>Version</span><span>${data.version}</span></div>
    `;
  } catch {
    el.innerHTML = '<p class="hint">Bridge unreachable.</p>';
  }
}

// Init
loadNodes();
loadZones();
loadStatus();

// Auto-refresh status every 5s
setInterval(loadStatus, 5000);
