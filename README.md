# RuView HA — Add-on

Monitor presence, falls, vitals, and intruders using $54 of WiFi hardware — no cameras, no cloud, works with Home Assistant.

Built on [RuView](https://github.com/ruvnet/RuView), an open source WiFi Channel State Information (CSI) sensing engine.

---

## What it does

RuView HA turns your existing WiFi network into a sensing layer:

| Capability | What you get in HA |
|---|---|
| **Presence** | `binary_sensor` — person detected per zone |
| **Fall detection** | `binary_sensor` — fall event in zone |
| **Motion** | `binary_sensor` — active movement |
| **Intrusion** | `binary_sensor` — motion during armed mode |
| **Person count** | `sensor` — number of people in zone |
| **Breathing rate** | `sensor` — 6–30 BPM (indicative, not medical-grade) |
| **Heart rate** | `sensor` — 40–120 BPM (indicative, not medical-grade) |
| **Signal quality** | `sensor` — CSI confidence score (%) |

All entities are grouped per zone (e.g. "Living Room — RuView") under one HA device entry.

**Privacy-first:** no cameras, no cloud, all processing runs locally on your Home Assistant host.

---

## Requirements

- Home Assistant OS or Supervised (2024.1.0+)
- ESP32 hardware flashed with RuView firmware (optional for initial setup — the add-on runs in simulation mode without it)

### Hardware

| Item | Approx. cost |
|---|---|
| 2× ESP32-S3 dev boards | ~$20 |
| USB cables + power | ~$10 |
| Enclosures (optional) | ~$24 |

See the [RuView hardware guide](https://github.com/ruvnet/RuView#hardware) for exact models and firmware flashing instructions.

---

## Installation

### 1. Add this repository to HA

In Home Assistant: **Settings → Add-ons → Add-on Store → ⋮ → Repositories**

Add:
```
https://github.com/bibinabraham06/ruview-ha-addon
```

### 2. Install the add-on

Find **RuView HA** in the store and click **Install**.

### 3. Start it

Click **Start**. The add-on starts immediately in simulation mode — no hardware required.

### 4. Add the integration

**Settings → Devices & Services → Add Integration → RuView**

The integration auto-discovers the running add-on. One click and your entities are live.

---

## Configuration

| Option | Default | Description |
|---|---|---|
| `log_level` | `info` | Log verbosity: `debug`, `info`, `warning`, `error` |
| `scan_interval` | `1` | RuView polling interval in seconds (1–10) |
| `intrusion_mode` | `false` | Enable intrusion detection (flags motion as intrusion) |

---

## Ingress panel

Open the add-on's web UI from the HA sidebar:

- **Node Pairing** — connect ESP32 nodes
- **Zone Config** — map nodes to named rooms, adjust sensitivity
- **System Status** — pipeline health, frame rate, signal quality

---

## Roadmap

| Version | Scope |
|---|---|
| `v0.1.0` | Add-on boots, integration connects, presence entities live |
| `v0.2.0` | Fall detection + vitals, hardware-free sim mode documented |
| `v0.3.0` | Intrusion mode, full zone config UI |
| `v1.0.0` | HACS + HA Add-on Store submission |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). No ESP32 hardware needed for development — RuView has a built-in simulation mode.

## License

MIT — same as upstream RuView.
