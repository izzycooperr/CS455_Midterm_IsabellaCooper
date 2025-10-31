"""providers.weather

Design Element: **Adapter interface** for weather APIs.
Why: Keep the domain stable while substituting real services later. :contentReference[oaicite:11]{index=11}
"""

from abc import ABC, abstractmethod
from typing import Literal


class WeatherProvider(ABC):
    """Adapter interface for weather lookups."""

    @abstractmethod
    def summary(self, location: str) -> Literal["sunny", "rain", "clouds", "snow"]:
        """Return a coarse weather category for a location."""
        raise NotImplementedError


class StubWeather(WeatherProvider):
    """Minimal stub returning a fixed weather label."""

    def summary(self, location: str) -> Literal["sunny", "rain", "clouds", "snow"]:
        return "clouds"
