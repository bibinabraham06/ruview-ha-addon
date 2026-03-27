# ruview-ha-addon/tests/test_zone_registry.py
from bridge.zone_registry import ZoneRegistry
from bridge.models import ZoneData


def test_registry_starts_empty():
    reg = ZoneRegistry()
    assert reg.snapshot().zones == []


def test_update_zone_creates_entry():
    reg = ZoneRegistry()
    zone = ZoneData(zone_id="hall", zone_name="Hallway", presence=True)
    reg.update(zone)
    snap = reg.snapshot()
    assert len(snap.zones) == 1
    assert snap.zones[0].zone_id == "hall"
    assert snap.zones[0].presence is True


def test_update_zone_overwrites_existing():
    reg = ZoneRegistry()
    reg.update(ZoneData(zone_id="hall", zone_name="Hallway", person_count=1))
    reg.update(ZoneData(zone_id="hall", zone_name="Hallway", person_count=3))
    snap = reg.snapshot()
    assert len(snap.zones) == 1
    assert snap.zones[0].person_count == 3


def test_multiple_zones():
    reg = ZoneRegistry()
    reg.update(ZoneData(zone_id="room_a", zone_name="Room A"))
    reg.update(ZoneData(zone_id="room_b", zone_name="Room B"))
    assert len(reg.snapshot().zones) == 2
