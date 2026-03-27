from dataclasses import dataclass, field
from typing import Optional

@dataclass
class ZoneData:
    """Sensing data for a single zone (room).

    signal_quality is stored as a float in [0.0, 1.0] and serialized
    to an integer percentage (0-100) by to_dict(). Values outside [0.0, 1.0]
    raise ValueError on construction.

    breathing_rate and heart_rate are None when no person is detected;
    to_dict() preserves None as null in the JSON API. The HA integration
    is expected to handle null gracefully.
    """

    zone_id: str
    zone_name: str
    person_count: int = 0
    presence: bool = False
    fall_detected: bool = False
    motion: bool = False
    intrusion: bool = False
    breathing_rate: Optional[float] = None
    heart_rate: Optional[float] = None
    signal_quality: float = 0.0

    def __post_init__(self) -> None:
        if not 0.0 <= self.signal_quality <= 1.0:
            raise ValueError(
                f"signal_quality must be in [0.0, 1.0], got {self.signal_quality}"
            )

    def to_dict(self) -> dict:
        return {
            "zone_id": self.zone_id,
            "zone_name": self.zone_name,
            "person_count": self.person_count,
            "presence": self.presence,
            "fall_detected": self.fall_detected,
            "motion": self.motion,
            "intrusion": self.intrusion,
            "breathing_rate": self.breathing_rate,
            "heart_rate": self.heart_rate,
            "signal_quality": round(self.signal_quality * 100),
        }

@dataclass
class SensingSnapshot:
    zones: list[ZoneData] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {"zones": [z.to_dict() for z in self.zones]}
