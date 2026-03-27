# RuView HA

WiFi-based presence, fall detection, and vitals monitoring — no cameras, no cloud.

## First-time setup

1. **Start the add-on** — it runs in simulation mode immediately, no hardware needed.
2. Go to **Settings → Devices & Services → Add Integration → RuView** to create your HA entities.
3. Open the **Web UI** tab to configure zones and pair ESP32 nodes when you have hardware.

## Configuration options

| Option | Default | Description |
|---|---|---|
| `log_level` | `info` | Log verbosity (`debug` / `info` / `warning` / `error`) |
| `scan_interval` | `1` | How often to poll RuView in seconds (1–10) |
| `intrusion_mode` | `false` | When enabled, motion events are flagged as intrusions |

## Connecting hardware

Once you have ESP32 nodes flashed with RuView firmware:

1. Open the **Web UI → Node Pairing** screen
2. Nodes on the same WiFi network appear automatically
3. Map each node to a named zone on the **Zone Config** screen
4. Entity names in HA update to reflect your zone names

Firmware flashing guide: [github.com/ruvnet/RuView](https://github.com/ruvnet/RuView#hardware)

## Vitals disclaimer

Breathing rate and heart rate readings are **indicative only** — derived from WiFi signal patterns. They are not medical-grade measurements and should not be used for clinical decisions.

## Support

- Bugs and feature requests: [github.com/bibinabraham06/ruview-ha-addon/issues](https://github.com/bibinabraham06/ruview-ha-addon/issues)
- Discussions: GitHub Discussions tab
