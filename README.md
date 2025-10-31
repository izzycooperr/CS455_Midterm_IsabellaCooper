# Romantic or Platonic Date Generator (Design-First Midterm)

This project is a **design-focused** architecture for a Date Generator that proposes context-aware outings (romantic or platonic) using the user’s location, time, weather, season, preferences, and constraints. The current milestone ships **valid, runnable Python stubs** with exhaustive docstrings labeling every design element and pattern used. Future terms can fill in behavior.

> This repository follows the planning document closely (components like `InputCollector`, `PlanGenerator`, `ItineraryAssembler`, `ScoringPolicy`, `Constraint`, external `Providers`, `Exporter`, `ExplanationEngine`, and typed `Activity` classes). Design emphasizes extensibility and clarity for documentation. :contentReference[oaicite:2]{index=2}

## Project Overview

- **Goal:** Generate tailored itineraries with activities, timing, travel, cost notes, reservation hints, and weather-aware backups. :contentReference[oaicite:3]{index=3}
- **Scope (midterm):** No real integrations yet; we deliver architecture, interfaces, and Sphinx docs as a static site in `/docs`.

## Tech & Language

- **Language:** Python 3.11+
- **Docs:** Sphinx (autodoc + napoleon), HTML emitted into `/docs` so it can be hosted as a static site (e.g., GitHub Pages).

## Installation

```bash
# clone your private repo
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
