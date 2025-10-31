"""core.constraints

Design Element: **Constraint abstraction**
Usage: Encodes rules like time limits, accessibility, indoor/outdoor, budget ceilings.
Potential Extension: Decorator to layer additional checks without changing base logic. :contentReference[oaicite:9]{index=9}
"""

from abc import ABC, abstractmethod
from src.activities.base import Activity


class Constraint(ABC):
    """Abstract constraint applied to candidate activities or full itineraries."""

    @abstractmethod
    def is_satisfied_by(self, activity: Activity) -> bool:
        """Return True if the activity passes this constraint."""
        raise NotImplementedError


class BudgetCeiling(Constraint):
    """Simple constraint that disallows items above a given price."""

    def __init__(self, max_cost: float) -> None:
        self.max_cost = max_cost

    def is_satisfied_by(self, activity: Activity) -> bool:
        return (activity.estimated_cost or 0.0) <= self.max_cost
