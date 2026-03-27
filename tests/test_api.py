# ruview-ha-addon/tests/test_api.py
import pytest
from bridge.api import create_app
from bridge.zone_registry import ZoneRegistry
from bridge.models import ZoneData

@pytest.fixture
def registry_with_data():
    reg = ZoneRegistry()
    reg.update(ZoneData(
        zone_id="living_room",
        zone_name="Living Room",
        person_count=1,
        presence=True,
        breathing_rate=14.0,
        heart_rate=70.0,
        signal_quality=0.85,
    ))
    return reg

async def test_health_endpoint(aiohttp_client, registry_with_data):
    app = create_app(registry_with_data)
    client = await aiohttp_client(app)
    resp = await client.get("/health")
    assert resp.status == 200
    data = await resp.json()
    assert data["status"] == "ok"

async def test_sensing_latest_returns_zones(aiohttp_client, registry_with_data):
    app = create_app(registry_with_data)
    client = await aiohttp_client(app)
    resp = await client.get("/api/sensing/latest")
    assert resp.status == 200
    data = await resp.json()
    assert len(data["zones"]) == 1
    assert data["zones"][0]["zone_id"] == "living_room"
    assert data["zones"][0]["presence"] is True
    assert data["zones"][0]["signal_quality"] == 85

async def test_sensing_latest_empty_when_no_zones(aiohttp_client):
    app = create_app(ZoneRegistry())
    client = await aiohttp_client(app)
    resp = await client.get("/api/sensing/latest")
    assert resp.status == 200
    data = await resp.json()
    assert data["zones"] == []
