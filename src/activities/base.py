"""activities.base

Design Element: **Activity (abstract base)**
Acts as the leaf in the **Composite** structure (Itinerary). :contentReference[oaicite:16]{index=16}
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Activity:
    """Abstract activity with shared fields.

    Pattern: **Leaf (Composite)**
    """
    name: str
    estimated_cost: Optional[float] = None
    typical_minutes: Optional[int] = None
