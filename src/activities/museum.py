"""activities.museum

Design Element: **Concrete Activity** (Composite leaf). :contentReference[oaicite:19]{index=19}
"""

from dataclasses import dataclass
from src.activities.base import Activity


@dataclass
class MuseumActivity(Activity):
    """Indoor cultural activity."""
    ticket_required: bool | None = True
