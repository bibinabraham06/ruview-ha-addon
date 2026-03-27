import pytest
from aiohttp import web

MOCK_RUVIEW_RESPONSE = {
    "zones": [
        {
            "zone_id": "living_room",
            "zone_name": "Living Room",
            "person_count": 1,
            "presence": True,
            "fall_detected": False,
            "motion": True,
            "intrusion": False,
            "breathing_rate": 15.2,
            "heart_rate": 68.0,
            "signal_quality": 0.91,
        }
    ]
}

@pytest.fixture
async def mock_ruview_url(aiohttp_server):
    """Start a local aiohttp server that mimics the RuView REST API."""

    async def handle_sensing(request):
        return web.json_response(MOCK_RUVIEW_RESPONSE)

    async def handle_health(request):
        return web.json_response({"status": "ok"})

    app = web.Application()
    app.router.add_get("/api/v1/sensing/latest", handle_sensing)
    app.router.add_get("/health", handle_health)

    server = await aiohttp_server(app)
    return f"http://{server.host}:{server.port}"
