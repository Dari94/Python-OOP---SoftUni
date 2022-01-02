from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}

    @abstractmethod
    def add_ingredient(self, type, quantity):
        """Add products to the factory"""
        pass

    @abstractmethod
    def remove_ingredient(self, type, quantity):
        """Remove products from the factory"""
        pass

    def can_add(self, value):
        return self.capacity - sum(self.ingredients.values()) - value >= 0

    def __repr__(self):
        result = ""
        result += f"Factory name: {self.name} with capacity {self.capacity}.\n"
        for ingredient in self.ingredients:
            result += f"{ingredient}: {self.ingredients[ingredient]}\n"
        return result


from project.factory.factory import Factory


class PaintFactory(Factory):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    def add_ingredient(self, product_type, product_quantity):
        if product_type in ["white", "yellow", "blue", "green", "red"]:
            if self.can_add(product_quantity):
                if product_type not in self.ingredients:
                    self.ingredients[product_type] = 0
                self.ingredients[product_type] += product_quantity
            else:
                raise ValueError("Not enough space in factory")
        else:
            raise TypeError(f"Ingredient of type {product_type} not allowed in {self.__class__.__name__}")

    def remove_ingredient(self, product_type, product_quantity):
        if product_type in self.ingredients:
            if self.ingredients[product_type] - product_quantity >= 0:
                self.ingredients[product_type] -= product_quantity
            else:
                raise ValueError("Ingredients quantity cannot be less than zero")
        else:
            raise KeyError("No such ingredient in the factory")

    @property
    def products(self):
        return self.ingredients


#import unittest
from project.factory.paint_factory import PaintFactory


#class Test:
import unittest
class PaintTest(unittest.TestCase):
    def test_AddIngredient_whenNotEnoughCapacity_ShouldRaiseValueError(self):
        p_name = 'paint'
        p_capacity = 10
        paint = PaintFactory(p_name, p_capacity)
        with self.assertRaises(ValueError):
            paint.add_ingredient('red', 15)

    def test_AddIngredient_whenIngredientNotIn_ShouldRaiseValueError(self):
        p_name = 'paint'
        p_capacity = 10
        paint = PaintFactory(p_name, p_capacity)

        with self.assertRaises(TypeError):
            paint.add_ingredient('purple', 5)

    def test_AddIngredient_whenIngredientNoInIngredients_shouldUpdateIngredients(self):
        p_name = 'paint'
        p_capacity = 10
        paint = PaintFactory(p_name, p_capacity)
        paint.add_ingredient('white', 3)
        paint.add_ingredient('red', 3)
        paint.add_ingredient('red', 3)

        expected = {'white': 3, 'red': 6}
        self.assertEqual(paint.ingredients, expected)

    def test_RemoveIngredient_whenIngredientNotIn_ShouldRaiseKeyError(self):
        p_name = 'paint'
        p_capacity = 10
        paint = PaintFactory(p_name, p_capacity)

        with self.assertRaises(KeyError):
            paint.remove_ingredient('blue', 5)

    def test_RemoveIngredient_whenNotEnoughQuantity_ShouldRaiseValueError(self):
        p_name = 'paint'
        p_capacity = 10
        paint = PaintFactory(p_name, p_capacity)

        with self.assertRaises(ValueError):
            paint.remove_ingredient('red', 7)

    def test_RemoveIngredient_whenNotIngredient_ShouldDecreaseQuantity(self):
        p_name = 'paint'
        p_capacity = 10
        paint = PaintFactory(p_name, p_capacity)
        paint.remove_ingredient('red', 3)
        expected = {'white': 3, 'red': 3}
        self.assertEqual(paint.ingredients, expected)


if __name__ == '__main__':
    unittest.main()