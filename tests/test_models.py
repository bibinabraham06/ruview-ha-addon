from bridge.models import ZoneData, SensingSnapshot
import pytest

def test_zone_data_defaults():
    z = ZoneData(zone_id="living_room", zone_name="Living Room")
    assert z.person_count == 0
    assert z.presence is False
    assert z.fall_detected is False
    assert z.motion is False
    assert z.intrusion is False
    assert z.breathing_rate is None
    assert z.heart_rate is None
    assert z.signal_quality == 0.0

def test_sensing_snapshot_contains_zones():
    zones = [ZoneData(zone_id="bedroom", zone_name="Bedroom")]
    snap = SensingSnapshot(zones=zones)
    assert len(snap.zones) == 1
    assert snap.zones[0].zone_id == "bedroom"

def test_zone_data_from_ruview_payload():
    payload = {
        "zone_id": "kitchen",
        "zone_name": "Kitchen",
        "person_count": 2,
        "presence": True,
        "fall_detected": False,
        "motion": True,
        "intrusion": False,
        "breathing_rate": 14.5,
        "heart_rate": 72.0,
        "signal_quality": 0.87,
    }
    z = ZoneData(**payload)
    assert z.person_count == 2
    assert z.breathing_rate == 14.5
    assert z.signal_quality == 0.87
