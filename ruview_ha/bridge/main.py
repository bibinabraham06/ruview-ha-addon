# ruview-ha-addon/bridge/main.py
import asyncio
import logging
import os
from aiohttp import web
from bridge.api import create_app
from bridge.models import ZoneData
from bridge.ruview_client import RuViewClient
from bridge.zone_registry import ZoneRegistry

logging.basicConfig(level=os.environ.get("LOG_LEVEL", "INFO").upper())
log = logging.getLogger(__name__)

RUVIEW_URL = os.environ.get("RUVIEW_URL", "http://localhost:3000")
BRIDGE_PORT = int(os.environ.get("BRIDGE_PORT", "8099"))
SCAN_INTERVAL = max(1, int(os.environ.get("SCAN_INTERVAL", "1")))

# Seed registry with a default zone so the integration has entities to create.
# Overwritten by real RuView data when hardware is present.
_DEFAULT_ZONE = ZoneData(
    zone_id="living_room",
    zone_name="Living Room",
    signal_quality=0.0,
)


async def poll_ruview(client: RuViewClient, registry: ZoneRegistry) -> None:
    while True:
        try:
            zones = await client.fetch_zones()
            for zone in zones:
                registry.update(zone)
        except Exception as exc:
            log.debug("RuView not reachable, using default zone data: %s", exc)
        await asyncio.sleep(SCAN_INTERVAL)


async def main() -> None:
    registry = ZoneRegistry()
    registry.update(_DEFAULT_ZONE)

    client = RuViewClient(base_url=RUVIEW_URL)
    app = create_app(registry)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", BRIDGE_PORT)
    await site.start()
    log.info("Bridge running on port %s", BRIDGE_PORT)

    await poll_ruview(client, registry)


if __name__ == "__main__":
    asyncio.run(main())
