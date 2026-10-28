"""CP1404: Guitar Class Task
For All Three Programs under this task:
Estimate: 45 Minutes
  Actual:
"""
import datetime


class Guitar:
    """Represent a Guitar Object."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar Instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a formatted string."""
        return f"{self.name} ({self.year} : ${self.cost:.2f})"

    def get_age(self):
        """Calculate age of Guitar."""
        current_year = datetime.datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        """Determine if a Guitar is vintage."""
        age = self.get_age()
        if age > 50:
            return True
        return False
