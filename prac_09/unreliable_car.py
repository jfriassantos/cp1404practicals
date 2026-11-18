"""
CP1404 Practical Task: UnreliableCar class
By Jose Frias Santos
"""
from car import Car
import random


class UnreliableCar(Car):
    """Specalised version of Car where the Car object is unreliable."""

    def __init__(self, name, fuel, reliability):
        """Initalise a UnreliableCar class based on Car class."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent class but add reliability."""
        if random.randint(0, 100) < self.reliability:
            super().drive(distance)
        else:
            super().drive(0)
