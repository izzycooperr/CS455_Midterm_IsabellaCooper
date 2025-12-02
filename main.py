"""
Main entry point for the Date Generator project.

This file provides a high-level demonstration that the architectural
components of the system exist, import correctly, and are executable.

The project is design-focused and does not implement full application logic.
"""

from src.providers.weather import StubWeather
from src.providers.maps import StubMaps
from src.providers.places import StubPlaces
from src.core.scoring import BudgetFriendlyPolicy
from src.core.plan_generator import PlanGenerator


class DateGeneratorApp:
    """
    High-level application wrapper for the Date Generator.
    """

    def __init__(self):
        print("Initializing Date Generator components...")

        # External service adapters (stubs)
        self.weather_provider = StubWeather()
        self.maps_provider = StubMaps()
        self.places_provider = StubPlaces()

        # Scoring policy
        self.scoring_policy = BudgetFriendlyPolicy()

        # Core generator (not fully executed in this demo)
        self.generator = PlanGenerator

    def run(self):
        print("Date Generator (Design-Only Demo)")
        print("--------------------------------")
        print("Weather provider:", type(self.weather_provider).__name__)
        print("Maps provider:", type(self.maps_provider).__name__)
        print("Places provider:", type(self.places_provider).__name__)
        print("Scoring policy:", type(self.scoring_policy).__name__)
        print("Core generator:", self.generator.__name__)
        print()
        print("System initialized successfully.")
        print("No date plans are generated in this demo.")


def main():
        app = DateGeneratorApp()
        app.run()


if __name__ == "__main__":
    main()
