
---

# Patterns.md (copy-paste)

```markdown
# Patterns Used / Considered

For each pattern covered in class, I note **Used?** and **Rationale** in the context of this architecture.

| Pattern | Used? | Rationale |
|---|---|---|
| **Strategy** | Yes | `ScoringPolicy` is a Strategy. Different scoring schemes (budget-first, romance-first, accessibility-first) can be swapped at runtime without changing the generator. |
| **Builder** | Yes | `ItineraryAssembler` acts as a Builder that incrementally constructs an itinerary from activities, travel legs, and timing. |
| **Factory Method** | Yes | Activity creation (`RestaurantActivity`, `ParkActivity`, etc.) can be produced via factory methods based on type + constraints. |
| **Abstract Factory** | Considered | If we standardize activity “families” per season or city, an Abstract Factory could spawn coherent sets (e.g., “RainyDaySet”). Not required at midterm. |
| **Adapter** | Yes | `WeatherProvider`, `PlacesProvider`, `MapsProvider` are adapters over external services so the domain layer stays stable if APIs change. |
| **Facade** | Yes | A `ProviderFacade` (or aggregator inside `PlanGenerator`) hides the complexity of multiple providers behind one simpler interface. |
| **Template Method** | Yes | `PlanGenerator` defines the high-level algorithm steps; subclasses can refine selection, ranking, and assembly steps. |
| **Composite** | Yes | An `Itinerary` composed of `Activity` items (and sub-activities) fits Composite; treat whole itineraries and single activities uniformly. |
| **Decorator** | Considered | Could decorate `ScoringPolicy` with extra constraints on the fly (e.g., “AddWeatherPenalty”) without modifying base strategy. Included as optional extension. |
| **Observer** | Considered | Live updates for weather/availability would notify the UI or planner; left out for now because midterm is static design. |
| **State** | Considered | Mode toggles (romantic vs platonic) and planning phases could be modeled as states; Strategy already covers most needs here. |
| **Command** | Considered | User actions (save, export, compare versions) could be Commands to enable undo/redo; deferred. |
| **Proxy** | Considered | A caching proxy for provider calls (e.g., places lookup) would reduce latency; deferred. |
| **Iterator** | Yes | Iterating candidate activities and combinations is explicit in generator search loops; Python’s iterators make this natural. |
| **Memento** | Considered | Save/restore plan snapshots for “compare” could use Memento; earmarked for a later phase. |
| **Visitor** | Considered | Cross-cutting operations over activities (cost rollup, safety checks) could be Visitors; not necessary at midterm. |
