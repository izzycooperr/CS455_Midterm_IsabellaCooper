"""export.pdf_exporter

Design Element: **Exporter interface**
Purpose: Convert an `Itinerary` to a human-friendly output format (PDF/HTML/ICS). :contentReference[oaicite:14]{index=14}
"""

from abc import ABC, abstractmethod
from src.core.itinerary import Itinerary


class Exporter(ABC):
    """Exporter interface for rendering itineraries."""

    @abstractmethod
    def export(self, itinerary: Itinerary) -> bytes:
        """Return raw bytes of the exported document."""
        raise NotImplementedError


class StubPdfExporter(Exporter):
    """Stub PDF exporter that returns placeholder bytes."""

    def export(self, itinerary: Itinerary) -> bytes:
        return b"%PDF-1.4\n% stub content\n"
