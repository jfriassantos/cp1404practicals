from silver_service_taxi import SilverServiceTaxi

fancy_taxi = SilverServiceTaxi("Silver #1", 100, 2)
fancy_taxi.start_fare()
fancy_taxi.drive(18)
print(f"The fare for a 18km ride in this taxi is: ${fancy_taxi.get_fare():.2f}")
assert fancy_taxi.get_fare() == 48.78
assert fancy_taxi._odometer == 18
assert fancy_taxi.fuel == 82
