"""core.itinerary

Design Elements: **Composite**, **Builder target**
- Composite: Itinerary holds Activities and can be treated like a single item.
- Builder target: `ItineraryAssembler` incrementally constructs an itinerary. :contentReference[oaicite:7]{index=7}
"""

from dataclasses import dataclass, field
from typing import List, Optional
from src.activities.base import Activity


@dataclass
class Itinerary:
    """Composite root representing a full outing plan.

    Pattern: **Composite**
    Contains: ordered `Activity` items, estimated travel times, and notes.
    """
    items: List[Activity] = field(default_factory=list)
    total_estimated_cost: float = 0.0
    notes: Optional[str] = None


class ItineraryAssembler:
    """Director/Builder responsible for constructing an `Itinerary`.

    Pattern: **Builder**
    Role: Encapsulates the stepwise assembly of activities into a coherent plan.
    """

    def __init__(self) -> None:
        self._itinerary = Itinerary()

    def add_activity(self, activity: Activity) -> None:
        """Add a single activity to the itinerary."""
        self._itinerary.items.append(activity)
        if activity.estimated_cost is not None:
            self._itinerary.total_estimated_cost += activity.estimated_cost

    def build(self) -> Itinerary:
        """Return the constructed itinerary."""
        return self._itinerary
