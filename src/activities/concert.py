"""activities.concert

Design Element: **Concrete Activity** (Composite leaf). :contentReference[oaicite:20]{index=20}
"""

from dataclasses import dataclass
from src.activities.base import Activity


@dataclass
class ConcertActivity(Activity):
    """Live music event."""
    standing_room: bool | None = None
