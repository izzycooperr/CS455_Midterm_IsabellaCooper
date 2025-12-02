# Design Patterns in the Date Generator

This repository is a **design-first** architecture for a romantic or platonic date generator.  
The Python files in `src/` are light stubs that show structure and patterns only. There is **no real business logic or external API integration** yet by design.

The high-level goal:

- Take user preferences (romantic vs platonic, indoor vs outdoor, budget, time window, etc.).
- Ask for a location.
- Optionally consider weather for outdoor plans.
- Build a small itinerary of activities that fits those constraints.
- Be easy to extend later (more activity types, better scoring, real APIs).

Below I describe the main patterns and where they appear in the current design.

---

## 1. Strategy – Scoring Policies

**Where in the code**

- `src/core/scoring.py` – `ScoringPolicy` (abstract) and concrete policies like `BudgetFriendlyPolicy`.

**Idea**

The generator will eventually need to rank different candidate itineraries:

- One user might care about **budget** first.
- Another might care more about **time balance**.
- Another might care about **“wow” factor / romance**.

Instead of hard-coding one scoring formula, the design uses a **Strategy**:

- `ScoringPolicy` is the Strategy interface (`score(self, activities)`).
- Concrete strategies (like `BudgetFriendlyPolicy`) implement different scoring rules.
- The planner can be configured with different policies without changing its own code.

**Why this helps**

- You can add new ways of ranking (weather-aware, accessibility-aware, “first date” vs “anniversary”) just by adding new `ScoringPolicy` subclasses.
- Tests can plug in a simple policy without changing the planner.

---

## 2. Template Method – Core Planning Workflow

**Where in the code**

- `src/core/plan_generator.py` – `PlanGenerator`.

**Idea**

Generating a plan always follows roughly the same high-level steps:

1. Collect user input / constraints.
2. Ask providers for candidate activities (places, parks, restaurants, etc.).
3. Filter activities by constraints (budget ceilings, indoor/outdoor, time).
4. Score them using a `ScoringPolicy`.
5. Pick the “best” set.
6. Assemble an `Itinerary`.

The class `PlanGenerator` captures this **Template Method** idea:

- It defines the overall structure of the algorithm.
- Individual steps (like scoring or filtering) are broken into overridable helper methods (`_filter_candidates`, `_rank_and_select`, `_assemble`).
- Later, you could subclass `PlanGenerator` for special cases (e.g., “rainy-day generator”, “double date generator”) and override only parts of the workflow.

**Why this helps**

- Keeps the full planning algorithm in one place.
- Still allows customization of parts of the pipeline without duplicating everything.

---

## 3. Composite + Builder – Itinerary and ItineraryAssembler

**Where in the code**

- `src/core/itinerary.py` – `Itinerary` and `ItineraryAssembler`.
- `src/activities/base.py` – `Activity` base class.
- `src/activities/restaurant.py`, `park.py`, `museum.py`, `concert.py` – concrete activities.

**Composite**

- `Activity` is the leaf type (single activity such as “Dinner at cozy café” or “Walk in the park”).
- `Itinerary` is the **Composite** that:
  - Holds a list of `Activity` objects.
  - Tracks things like `total_estimated_cost`.
  - Can be treated conceptually as “one big thing” (the date) while still made of parts.

**Builder**

- `ItineraryAssembler` acts as a simple **Builder**:
  - It starts with an empty `Itinerary`.
  - `add_activity` appends activities and updates totals.
  - `build()` returns the finished `Itinerary`.

**Why this helps**

- Composite: lets you treat an itinerary and individual activities consistently in future code (e.g., scoring, exporting).
- Builder: centralizes the logic for constructing an itinerary, so if the structure changes, you only update one place.

---

## 4. Adapter (and a bit of Factory Method) – Providers for Weather, Maps, and Places

**Where in the code**

- `src/providers/weather.py` – `WeatherProvider`, `StubWeather`.
- `src/providers/maps.py` – `MapsProvider`, `StubMaps`.
- `src/providers/places.py` – `PlacesProvider`, `StubPlaces`.

**Adapter**

The project will eventually talk to real external services:

- Weather APIs for simple labels like “sunny”, “rain”, “clouds”.
- Maps / routing APIs for travel time.
- Places / restaurant APIs for candidate date locations.

Instead of tying the domain classes directly to any one API, each module defines an **Adapter interface**:

- `WeatherProvider.summary(location)` → coarse weather category.
- `MapsProvider.travel_minutes(origin, destination)` → travel duration.
- `PlacesProvider.sample_candidates()` → a list of `Activity` objects.

Right now the project only has stub implementations (`StubWeather`, `StubMaps`, `StubPlaces`) so the design is visible without needing real API calls.

**Factory Method**

`StubPlaces.sample_candidates()` also plays with a small **Factory Method** flavor:

- It returns concrete `Activity` subclasses (e.g., `RestaurantActivity`, `ParkActivity`).
- The rest of the system doesn’t need to know exactly how they are instantiated.

**Why this helps**

- Swapping in real APIs later is just a matter of implementing the same interfaces.
- Tests can keep using stub providers for predictable behavior.
- Adding new activity types can happen inside providers without changing the planner.

---

## 5. Constraints – A Step Toward Decorator / Open-Closed Design

**Where in the code**

- `src/core/constraints.py` – `Constraint` base class and `BudgetCeiling`.

**Idea**

The generator needs to enforce rules such as:

- “Total cost must stay under $50.”
- “Only outdoor activities.”
- “Duration must fit into a 3-hour block.”

The design introduces a `Constraint` abstraction:

- `Constraint.is_satisfied_by(activity)` returns a boolean.
- `BudgetCeiling` is a concrete constraint that checks `estimated_cost`.

In `PlanGenerator`, the filtering step applies a list of constraints to candidate activities before scoring.

This isn’t a full **Decorator** pattern yet, but it leans in that direction:

- You can layer multiple constraints together (`BudgetCeiling`, `IndoorOnly`, etc.) without changing the basic filtering code.
- Each new rule is a new class instead of yet another `if` inside the planner.

---

## 6. Explanation and Export – Clear Responsibilities

**Where in the code**

- `src/explain/explanation.py` – `ExplanationEngine`.
- `src/export/pdf_exporter.py` – placeholder for future exporting logic.

**Idea**

These classes emphasize separation of concerns rather than a big pattern:

- `ExplanationEngine` is responsible for turning an `Itinerary` into a human-readable explanation string.  
  Later this could be extended to explain budget decisions or why certain activities were excluded.
- `pdf_exporter.py` is intended to handle formatting an itinerary into a PDF (e.g., for printing or sharing).

By isolating these concerns, the core planning logic doesn’t need to care how plans are explained or exported.

---

## 7. How This Matches the Original Plan

The original hand-written plan included ideas like:

- Budget tiers at different levels.
- Indoor vs outdoor dates.
- Special handling for weather-dependent outdoor dates.
- Support for both romantic and platonic outings.
- A focus on “design only” for the midterm.

The current code keeps all of that at the **design level**:

- The modules, interfaces, and patterns are in place.
- Implementations are intentionally simple stubs.
- Future work can fill in real logic and API calls without changing core structure.

This document is meant to be read alongside the `src/` tree so you can see exactly where each pattern appears and why it was chosen.
