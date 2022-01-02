from project.factory.paint_factory import PaintFactory
import unittest


class TestPaintFactory(unittest.TestCase):
    def test_initFactoryAttributes(self):
        p_name = 'paint'
        p_capacity = 10
        factory = PaintFactory(p_name,p_capacity)
        self.assertEqual(factory.name, p_name)
        self.assertEqual(factory.capacity, p_capacity)
        self.assertEqual(len(factory.ingredients), 0)
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
        paint.add_ingredient('white', 1)
        paint.add_ingredient('red', 1)
        paint.add_ingredient('red', 1)

        expected = {'white': 1, 'red': 2}
        self.assertEqual(paint.ingredients, expected)

    def test_RemoveIngredient_whenIngredientNotIn_ShouldRaiseKeyError(self):
        p_name = 'paint'
        p_capacity = 10
        paint = PaintFactory(p_name, p_capacity)

        with self.assertRaises(KeyError):
            paint.remove_ingredient('sheep', 5)

    def test_RemoveIngredient_whenNotEnoughQuantity_ShouldRaiseValueError(self):
        p_name = 'paint'
        p_capacity = 10
        paint = PaintFactory(p_name, p_capacity)
        paint.add_ingredient('green',1)

        with self.assertRaises(ValueError):
            paint.remove_ingredient('green', 100)

    def test_RemoveIngredient_whenNotIngredient_ShouldDecreaseQuantity(self):
        p_name = 'paint'
        p_capacity = 10
        paint = PaintFactory(p_name, p_capacity)
        paint.add_ingredient('white',1)
        paint.add_ingredient("green", 1)
        paint.add_ingredient("green", 1)
        paint.remove_ingredient('green', 1)
        expected = {'white': 1, 'green': 1}
        self.assertEqual(paint.ingredients, expected)

    def test_PaintFactory_inherit_factory(self):
        self.assertTrue("Factory" == PaintFactory.__bases__[0].__name__)

    def test_return_ingredients_property(self):
        p_name = 'paint'
        p_capacity = 10
        paint = PaintFactory(p_name, p_capacity)
        paint.add_ingredient("green", 1)
        result = paint.products
        self.assertEqual(result, {"green": 1})


if __name__ == '__main__':
    unittest.main()