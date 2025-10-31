"""providers.places

Design Element: **Adapter interface** over places/POI services.
Also supports **Factory Method** for creating typed Activity instances. :contentReference[oaicite:12]{index=12}
"""

from abc import ABC, abstractmethod
from typing import List
from src.activities.base import Activity
from src.activities.restaurant import RestaurantActivity
from src.activities.park import ParkActivity


class PlacesProvider(ABC):
    """Adapter interface for finding candidate activities (POIs)."""

    @abstractmethod
    def sample_candidates(self) -> List[Activity]:
        """Return a small set of Activity instances."""
        raise NotImplementedError


class StubPlaces(PlacesProvider):
    """Stub provider: returns a few hard-coded activities."""

    def sample_candidates(self) -> List[Activity]:
        return [
            RestaurantActivity(name="Cozy Café", estimated_cost=25.0, typical_minutes=60),
            ParkActivity(name="Lithia Park Walk", estimated_cost=0.0, typical_minutes=45),
        ]
