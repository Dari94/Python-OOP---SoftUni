import unittest

from polymorfism_06.vehicle import Vehicle
from polymorfism_06.vehicle import Car
from polymorfism_06.vehicle import Truck


class TestVehicle(unittest.TestCase):

    def test_carDrive_whenEnoughFuel_shouldDecreaseFuel(self):
        fuel_quantity = 100
        fuel_consumption = 2
        car = Car(fuel_quantity, fuel_consumption)
        distance = 10
        car.drive(distance)
        expected = fuel_quantity - distance * (car.fuel_consumption + 0.9)
        self.assertEqual(car.fuel_quantity, expected)

    def test_carDrive_whenNotEnoughFuel_shouldDecreaseFuel(self):
        fuel_quantity = 100
        fuel_consumption = 2
        car = Car(fuel_quantity,fuel_consumption)

        distance = 40
        car.drive(distance)
        expected = fuel_quantity
        self.assertEqual(car.fuel_quantity, expected)

    def test_carRefuel_whenEnoughFuel_shouldDecreaseFuel(self):
        fuel_quantity = 100
        fuel_consumption = 2
        car = Car(fuel_quantity,fuel_consumption)

        car.refuel(10)
        self.assertEqual(car.fuel_quantity, fuel_quantity + 10)

    def test_truckDrive_whenEnoughFuel_shouldDecreaseFuel(self):
        fuel_quantity = 100
        fuel_consumption = 15
        params = [fuel_quantity, fuel_consumption]
        truck = Truck(*params)

        distance = 5
        truck.drive(distance)
        expected = fuel_quantity - distance * (truck.fuel_consumption + 1.6)

        self.assertEqual(truck.fuel_quantity, expected)

    def test_truckDrive_whenNotEnoughFuel_shouldDecreaseFuel(self):
        fuel_quantity = 100
        fuel_consumption = 15
        params = [fuel_quantity, fuel_consumption]
        truck = Truck(*params)

        distance = 40
        truck.drive(distance)
        expected = fuel_quantity
        self.assertEqual(truck.fuel_quantity, expected)


    def test_truckRefuel_whenEnoughFuel_shouldDecreaseFuel(self):
        fuel_quantity = 100
        fuel_consumption = 15
        params = [fuel_quantity, fuel_consumption]
        truck = Truck(*params)

        truck.refuel(50)
        self.assertEqual(truck.fuel_quantity, fuel_quantity + 50 *0.95)


if __name__ == '__main__':
    unittest.main()
