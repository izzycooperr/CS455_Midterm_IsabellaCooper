"""activities.restaurant

Design Element: **Concrete Activity**
May be created via **Factory Method** from providers. :contentReference[oaicite:17]{index=17}
"""

from dataclasses import dataclass
from src.activities.base import Activity


@dataclass
class RestaurantActivity(Activity):
    """Restaurant outing (reservations may apply)."""
    cuisine: str | None = None
