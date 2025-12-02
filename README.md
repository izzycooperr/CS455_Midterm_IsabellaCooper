# Romantic or Platonic Date Generator (Design-First Midterm)

This project is a **design-focused** architecture for a Date Generator that proposes
context-aware outings (romantic or platonic) using a user’s location, time, weather,
season, preferences, and constraints.

This midterm milestone intentionally focuses on **software design and patterns**.
The repository contains **valid, runnable Python stubs** that demonstrate structure,
interfaces, and architectural decisions. Full application behavior and real API
integrations are planned for future work.

---

## Project Overview

**Goal**

Generate tailored date itineraries that may include:
- Activities (restaurants, parks, museums, concerts)
- Timing and duration notes
- Budget awareness
- Weather-aware filtering
- Clear explanations of why activities were selected

**Scope (Midterm)**

- No real API integrations yet
- No UI
- Emphasis on architecture, extensibility, and documentation
- Static HTML documentation generated with Sphinx

---

## Architecture Summary

The design closely follows the original planning document and is organized around
clear responsibilities:

- **InputCollector** – Gathers user preferences and constraints
- **PlanGenerator** – Coordinates itinerary generation using defined strategies
- **Itinerary / ItineraryAssembler** – Composite + Builder for assembling date plans
- **ScoringPolicy** – Strategy pattern for ranking candidate activities
- **Constraint** – Encapsulates filtering rules like budget ceilings
- **Providers** – Adapters for future external services (weather, maps, places)
- **ExplanationEngine** – Produces human-readable explanations of plans
- **Exporter** – Placeholder for exporting plans (PDF, etc.)
- **Activity classes** – Typed domain models for different activity types

---

## Tech & Language

- **Language:** Python 3.11+
- **Documentation:** Sphinx (HTML output)
- **Paradigm:** Object-oriented, design-pattern driven

---

## Installation

```bash
# clone the repository
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt
