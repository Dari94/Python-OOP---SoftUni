from project.factory.paint_factory import PaintFactory
import unittest


class Test(unittest.TestCase):
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
