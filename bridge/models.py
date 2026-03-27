from dataclasses import dataclass, field
from typing import Optional

@dataclass
class ZoneData:
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
