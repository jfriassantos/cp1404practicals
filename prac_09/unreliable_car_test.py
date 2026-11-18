from unreliable_car import UnreliableCar

my_car = UnreliableCar("Toyota", 100, 30)
for i in range(100):
    my_car.drive(1)
print(my_car)