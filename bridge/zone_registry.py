# ruview-ha-addon/bridge/zone_registry.py
from bridge.models import ZoneData, SensingSnapshot


class ZoneRegistry:
    """In-memory state store for zone sensing data.

    The registry maintains a dictionary of zones keyed by zone_id.
    Each call to update() overwrites the entry for that zone_id.
    snapshot() returns a SensingSnapshot with the current state of all zones.
    """

    def __init__(self) -> None:
        self._zones: dict[str, ZoneData] = {}

    def update(self, zone: ZoneData) -> None:
        """Update or create a zone entry in the registry.

        Args:
            zone: ZoneData instance with at least zone_id and zone_name.
        """
        self._zones[zone.zone_id] = zone

    def snapshot(self) -> SensingSnapshot:
        """Return a snapshot of all zones in the registry.

        Returns:
            SensingSnapshot containing all current zones.
        """
        return SensingSnapshot(zones=list(self._zones.values()))
