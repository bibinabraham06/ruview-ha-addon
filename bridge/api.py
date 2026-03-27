# ruview-ha-addon/bridge/api.py
import json
import logging
from aiohttp import web
import aiohttp
from bridge.zone_registry import ZoneRegistry

log = logging.getLogger(__name__)

def create_app(registry: ZoneRegistry) -> web.Application:
    app = web.Application()
    app["registry"] = registry

    app.router.add_get("/health", handle_health)
    app.router.add_get("/api/sensing/latest", handle_sensing_latest)
    app.router.add_get("/ws", handle_websocket)

    return app

async def handle_health(request: web.Request) -> web.Response:
    return web.json_response({"status": "ok", "version": "0.1.0"})

async def handle_sensing_latest(request: web.Request) -> web.Response:
    registry: ZoneRegistry = request.app["registry"]
    return web.json_response(registry.snapshot().to_dict())

async def handle_websocket(request: web.Request) -> web.WebSocketResponse:
    registry: ZoneRegistry = request.app["registry"]
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    # Send current snapshot on connect
    await ws.send_str(json.dumps(registry.snapshot().to_dict()))

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.ERROR:
            log.warning("WebSocket error: %s", ws.exception())
            break
        # Other message types (text, binary) are ignored; server is push-only

    return ws
