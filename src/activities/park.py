"""activities.park

Design Element: **Concrete Activity** (Composite leaf). :contentReference[oaicite:18]{index=18}
"""

from dataclasses import dataclass
from src.activities.base import Activity


@dataclass
class ParkActivity(Activity):
    """Outdoor walk or nature visit."""
    paved_paths: bool | None = None
