from unreliable_car import UnreliableCar

my_car = UnreliableCar("Toyota", 100, 30)
for i in range(100):
    my_car.drive(1)
print(my_car)
other_car = UnreliableCar("Skoda", 100, 95)
for i in range (100):
    other_car.drive(1)
print(other_car)
best_car = UnreliableCar("MB", 100, 100)
for i in range (100):
    best_car.drive(1)
print(best_car)