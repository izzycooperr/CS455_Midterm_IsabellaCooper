"""providers.maps

Design Element: **Adapter interface** for mapping/route services. :contentReference[oaicite:13]{index=13}
"""

from abc import ABC, abstractmethod
from typing import Tuple


class MapsProvider(ABC):
    """Adapter interface for travel time and routing."""

    @abstractmethod
    def travel_minutes(self, origin: str, destination: str) -> int:
        """Return an estimated travel duration in minutes."""
        raise NotImplementedError


class StubMaps(MapsProvider):
    """Stub mapping provider."""

    def travel_minutes(self, origin: str, destination: str) -> int:
        return 10
