from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised fancier class of Taxi class."""

    def __init__(self, name, fuel, fanciness):
        """Initalise a specalised (fancier) version of Taxi."""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness
        self.flagfall = 4.5

    def __str__(self):
        """Return a string like Taxi but with flagfall."""
        return f"{super().__str__()} plus flagfall of {self.flagfall}"

    def get_fare(self):
        """Calculate fare like Taxi but add flagfall."""
        return super().get_fare() + self.flagfall
