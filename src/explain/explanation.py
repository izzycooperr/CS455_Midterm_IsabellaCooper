"""explain.explanation

Design Element: **ExplanationEngine**
Purpose: Justify why activities were selected (transparency). :contentReference[oaicite:15]{index=15}
"""

from src.core.itinerary import Itinerary


class ExplanationEngine:
    """Generates human-readable explanations for a given itinerary."""

    def explain(self, itinerary: Itinerary) -> str:
        names = ", ".join(a.name for a in itinerary.items)
        return f"Selected based on fit and balance: {names}."
