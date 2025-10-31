"""core.scoring

Design Element: **ScoringPolicy (Strategy)**
Rationale: Swap different ranking schemes without changing the planner:
budget-first, weather-first, romance-first, accessibility-first. :contentReference[oaicite:8]{index=8}
"""

from abc import ABC, abstractmethod
from typing import Sequence
from src.activities.base import Activity


class ScoringPolicy(ABC):
    """Strategy interface for scoring ranked activity candidates."""

    @abstractmethod
    def score(self, activities: Sequence[Activity]) -> float:
        """Return a numeric score for a set/sequence of activities."""
        raise NotImplementedError


class BudgetFriendlyPolicy(ScoringPolicy):
    """Concrete Strategy that prioritizes lower cost."""

    def score(self, activities: Sequence[Activity]) -> float:
        costs = [a.estimated_cost or 0.0 for a in activities]
        return -sum(costs)  # lower total cost => higher (less negative) score
