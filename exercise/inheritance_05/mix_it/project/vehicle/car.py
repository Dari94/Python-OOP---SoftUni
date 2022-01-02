from inheritance_05.mix_it.project.vehicle.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, available_seats, fuel_tank, fuel_consumption, fuel):
        super().__init__(available_seats)
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self.__fuel = fuel

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, value):
        if value <= (self.fuel_tank - self.__fuel):
            self.__fuel += value

    def drive(self, distance):
        new_fuel = self.fuel_consumption * distance
        if self.__fuel >= new_fuel:
            self.__fuel -= new_fuel
            return "We've enjoyed the travel!"

    def refuel(self, liters):
        capacity = self.fuel_tank - self.__fuel
        result = Car.get_capacity(capacity, liters)
        if isinstance(result, int):
            self.__fuel += liters
        return result
