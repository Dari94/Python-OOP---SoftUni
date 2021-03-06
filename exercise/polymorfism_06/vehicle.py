from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption, season="Summer"):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        self.season = season

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    ADD_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        need_liters = distance *( self.fuel_consumption + self.ADD_CONSUMPTION)
        if need_liters <= self.fuel_quantity:
            self.fuel_quantity -= need_liters

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    ADD_CONSUMPTION = 1.6
    LOST_FUEL = 95

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        need_liters = distance * (self.fuel_consumption + self.ADD_CONSUMPTION)
        if need_liters <= self.fuel_quantity:
            self.fuel_quantity -= need_liters

    def refuel(self, fuel):
        self.fuel_quantity += fuel * (self.LOST_FUEL /100)


car = Car(20, 5)
car.drive(5)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

#truck = Truck(100, 15)
#truck.drive(5)
#print(truck.fuel_quantity)
#truck.refuel(50)
#print(truck.fuel_quantity)
