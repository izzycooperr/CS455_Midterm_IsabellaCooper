"""core.input_collector

Design Element: **Input Collector (Interface / Role)**
Responsibility: Gather and validate user preferences and environmental parameters
(e.g., location, date/time, budget, accessibility, mode romantic/platonic). :contentReference[oaicite:5]{index=5}
"""

from typing import TypedDict, Literal, Optional


class UserInput(TypedDict, total=False):
    """Data shape for user preferences and context."""
    location: str
    datetime_iso: str
    budget_level: Literal["low", "medium", "high"]
    accessibility_needs: list[str]
    mode: Literal["romantic", "platonic"]
    preferred_atmosphere: Optional[str]


class InputCollector:
    """Interface-like base for collecting inputs (no external I/O here).

    Design Type: **Interface / Role**
    Why: Keeps UI/CLI/web layers decoupled from planning logic. Inputs can
    come from any front-end without changing the planner. :contentReference[oaicite:6]{index=6}
    """

    def collect(self) -> UserInput:
        """Return a validated `UserInput` mapping.

        Design Note: In production, implementations might prompt users or
        parse forms. For the midterm, return a minimal stub.
        """
        return UserInput(
            location="Ashland, OR",
            datetime_iso="2025-11-01T19:00:00",
            budget_level="medium",
            accessibility_needs=[],
            mode="romantic",
            preferred_atmosphere="cozy",
        )
