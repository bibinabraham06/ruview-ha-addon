# Contributing to ruview-ha-addon

## Hardware-free development

RuView includes a simulation mode — no ESP32 hardware needed:

```bash
docker run -p 3000:3000 ruvnet/wifi-densepose:latest --simulate
```

Then start the bridge pointing at it:

```bash
RUVIEW_URL=http://localhost:3000 python -m bridge.main
```

## Running tests

```bash
pip install aiohttp pytest pytest-asyncio pytest-aiohttp
pytest tests/ -v
```

## Architecture

- `bridge/models.py` — ZoneData and SensingSnapshot dataclasses
- `bridge/zone_registry.py` — in-memory zone state store keyed by zone_id
- `bridge/ruview_client.py` — aiohttp HTTP client wrapping RuView REST API
- `bridge/api.py` — aiohttp REST + WebSocket bridge server
- `bridge/main.py` — entry point: config from env vars, polling loop

Issues are labeled: `add-on`, `integration`, `docs`
