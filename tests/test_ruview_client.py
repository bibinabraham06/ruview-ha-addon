import pytest
from bridge.ruview_client import RuViewClient
from bridge.models import ZoneData

@pytest.mark.asyncio
async def test_fetch_zones_returns_zone_data(mock_ruview_url):
    client = RuViewClient(base_url=mock_ruview_url)
    zones = await client.fetch_zones()
    assert len(zones) == 1
    assert isinstance(zones[0], ZoneData)
    assert zones[0].zone_id == "living_room"
    assert zones[0].presence is True
    assert zones[0].breathing_rate == 15.2

@pytest.mark.asyncio
async def test_health_check_returns_true(mock_ruview_url):
    client = RuViewClient(base_url=mock_ruview_url)
    assert await client.is_healthy() is True

@pytest.mark.asyncio
async def test_health_check_returns_false_on_connection_error():
    client = RuViewClient(base_url="http://localhost:1")
    assert await client.is_healthy() is False
