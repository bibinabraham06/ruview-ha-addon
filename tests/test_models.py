# ruview-ha-addon/tests/test_models.py
from bridge.models import ZoneData, SensingSnapshot


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


def test_zone_data_to_dict_signal_quality_converts_to_percentage():
    z = ZoneData(zone_id="hall", zone_name="Hallway", signal_quality=0.87)
    d = z.to_dict()
    assert d["signal_quality"] == 87
    assert isinstance(d["signal_quality"], int)


def test_zone_data_to_dict_full_scale():
    z = ZoneData(zone_id="hall", zone_name="Hallway", signal_quality=1.0)
    assert z.to_dict()["signal_quality"] == 100

    z2 = ZoneData(zone_id="hall", zone_name="Hallway", signal_quality=0.0)
    assert z2.to_dict()["signal_quality"] == 0


def test_zone_data_to_dict_contains_all_fields():
    z = ZoneData(
        zone_id="hall",
        zone_name="Hallway",
        person_count=2,
        presence=True,
        fall_detected=False,
        motion=True,
        intrusion=False,
        breathing_rate=15.0,
        heart_rate=68.0,
        signal_quality=0.9,
    )
    d = z.to_dict()
    assert d["zone_id"] == "hall"
    assert d["zone_name"] == "Hallway"
    assert d["person_count"] == 2
    assert d["presence"] is True
    assert d["breathing_rate"] == 15.0
    assert d["heart_rate"] == 68.0
    # vitals: None passes through as None (null in JSON) — HA integration handles null
    z2 = ZoneData(zone_id="x", zone_name="X")
    assert z2.to_dict()["breathing_rate"] is None


def test_sensing_snapshot_to_dict():
    snap = SensingSnapshot(zones=[
        ZoneData(zone_id="room", zone_name="Room", signal_quality=0.5)
    ])
    d = snap.to_dict()
    assert "zones" in d
    assert len(d["zones"]) == 1
    assert d["zones"][0]["signal_quality"] == 50
