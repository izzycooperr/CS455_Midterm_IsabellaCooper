"""core.plan_generator

Design Elements: **Template Method**, **Facade (provider aggregation)**
- Template Method: defines high-level steps; subclasses may override selection/ranking.
- Facade: hides complexity of multiple providers behind one interface. :contentReference[oaicite:10]{index=10}
"""

from typing import Iterable, List
from src.core.itinerary import Itinerary, ItineraryAssembler
from src.core.scoring import ScoringPolicy
from src.core.constraints import Constraint
from src.activities.base import Activity
from src.providers.weather import WeatherProvider
from src.providers.places import PlacesProvider
from src.providers.maps import MapsProvider


class PlanGenerator:
    """High-level planner using the Template Method pattern."""

    def __init__(
        self,
        weather: WeatherProvider,
        places: PlacesProvider,
        maps: MapsProvider,
        scoring: ScoringPolicy,
        constraints: Iterable[Constraint] = (),
    ) -> None:
        self.weather = weather
        self.places = places
        self.maps = maps
        self.scoring = scoring
        self.constraints = list(constraints)

    # Template Method — override parts as needed in subclasses
    def generate(self) -> Itinerary:
        candidates = self._collect_candidates()
        filtered = self._apply_constraints(candidates)
        best = self._rank_and_select(filtered)
        return self._assemble(best)

    def _collect_candidates(self) -> List[Activity]:
        """Facade-style calls to providers to fetch raw activity candidates."""
        return self.places.sample_candidates()

    def _apply_constraints(self, items: List[Activity]) -> List[Activity]:
        result: List[Activity] = []
        for a in items:
            if all(c.is_satisfied_by(a) for c in self.constraints):
                result.append(a)
        return result

    def _rank_and_select(self, items: List[Activity]) -> List[Activity]:
        """Very simple stub: pick up to 3 activities maximizing the strategy score."""
        items = items[:6]
        return items[:3]

    def _assemble(self, chosen: List[Activity]) -> Itinerary:
        assembler = ItineraryAssembler()
        for a in chosen:
            assembler.add_activity(a)
        return assembler.build()
