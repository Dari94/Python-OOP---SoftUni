from project.factory.paint_factory import PaintFactory
import unittest


class TestPaintFactory(unittest.TestCase):
    def test_init_areCorrect(self):
        p_name = 'paint'
        p_capacity = 10
        f = PaintFactory(p_name, p_capacity)
        self.assertEqual(f.name, p_name)
        self.assertEqual(f.capacity, p_capacity)
        self.assertEqual(f.ingredients, {})
        self.assertEqual(len(f.ingredients), 0)

    def test_addIngredient_notEnoughCapacity(self):
        f = PaintFactory('paint', 10)
        with self.assertRaises(ValueError) as context:
            f.add_ingredient('white', 11)
        #self.assertEqual(str(context.exception), "Not enough space in factory")
        self.assertIsNotNone(context.exception)

    def test_addIngredient_notRightType(self):
        f = PaintFactory('paint', 10)
        with self.assertRaises(TypeError) as context:
            f.add_ingredient('sheep', 9)
        #self.assertEqual(str(context.exception), "Ingredient of type sheep not allowed in PaintFactory")
        self.assertIsNotNone(context.exception)

    def test_addIngredient_Right(self):
        f = PaintFactory('paint', 10)
        f.add_ingredient('white',2)
        f.add_ingredient('green', 1)
        f.add_ingredient('green', 1)
        expected = {'green': 2, 'white':2}
        self.assertEqual(f.ingredients, expected)

    def test_RemoveIngredient_Right(self):
        f = PaintFactory('paint', 10)
        f.add_ingredient('white',2)
        f.add_ingredient('green', 1)
        f.add_ingredient('green', 1)
        f.remove_ingredient('green', 1)
        expected = {'green': 1, 'white':2}
        self.assertEqual(f.ingredients, expected)

    def test_RemoveIngredient_notEnoughCapacity(self):
        f = PaintFactory('paint', 10)
        f.add_ingredient('white', 5)
        with self.assertRaises(ValueError) as context:
            f.remove_ingredient('white', 100)
        #self.assertEqual(str(context.exception), "Ingredient quantity cannot be less than zero")
        self.assertIsNotNone(context.exception)

    def test_RemoveIngredient_notRightType(self):
        f = PaintFactory('paint', 10)
        with self.assertRaises(KeyError):
            f.remove_ingredient('green', 2)
        #self.assertIsNotNone(context.exception)

    def test_property_ingredients(self):
        f = PaintFactory('paint', 10)
        f.add_ingredient('white', 1)
        self.assertEqual(f.products, {'white': 1})


if __name__ == '__main__':
    unittest.main()
