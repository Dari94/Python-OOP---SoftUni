import unittest
from lab_9.cat.cat import Cat


class TestCat(unittest.TestCase):
    def test_catEat_shouldIncreaseSizeBy1(self):
        """Cat's size is increased after eating"""
        name = "Cat name"
        cat = Cat(name)
        cat.eat()

        self.assertEqual(1, cat.size)

    def test_catEat_shouldSedFedToTrue(self):
        """Cat is fed after eating"""
        name = "Cat name"
        cat = Cat(name)
        cat.eat()

        self.assertTrue(cat.fed)

    def test_catEat_whenFed_shouldRaiseException(self):
        """Cat cannot eat if already fed, raises an error"""

        name = "Cat name"
        cat = Cat(name)
        cat.eat()
        with self.assertRaises(Exception) as context:
            cat.eat()
        self.assertIsNotNone(context.exception)

    def test_catSleep_whenNotFed_shouldRaiseException(self):
        """Cat cannot fall asleep if not fed, raises an error"""
        name = "Cat name"
        cat = Cat(name)

        with self.assertRaises(Exception) as context:
            cat.sleep()
        self.assertIsNotNone(context.exception)

    def test_catSleep_shouldNotSleepAfterSleep(self):
        """Cat is not sleepy after sleeping"""
        name = "Cat name"
        cat = Cat(name)
        cat.eat()
        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    unittest.main()
