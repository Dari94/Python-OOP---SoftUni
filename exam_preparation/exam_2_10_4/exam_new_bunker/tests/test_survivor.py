from project.survivor import Survivor
import unittest


class TestSurvivor(unittest.TestCase):
    def test_whenValidValues(self):
        s_name = 'Dari'
        s_age = 26
        survivor = Survivor(s_name, s_age)
        self.assertEqual(survivor.name, s_name)
        self.assertEqual(survivor.age, s_age)
        self.assertEqual(survivor.needs, 100)
        self.assertEqual(survivor.health, 100)

    def testName_whenNameIsNotValid_shouldRaiseValueError(self):
        s_name = 'Dari'
        s_age = 26
        survivor = Survivor(s_name, s_age)
        with self.assertRaises(ValueError) as context:
            survivor.name = ""
        self.assertEqual(str(context.exception), "Name not valid!")

    def testName_whenNameIsValid_shouldChangeName(self):
        s_name = 'Dari'
        s_age = 26
        survivor = Survivor(s_name, s_age)
        survivor.name = 'Pp'
        self.assertEqual(survivor.name, 'Pp')

    def testAge_whenAgeIsNotValid_shouldRaiseValueError(self):
        s_name = 'Dari'
        s_age = 26
        survivor = Survivor(s_name, s_age)
        with self.assertRaises(ValueError) as context:
            survivor.age = -5
        self.assertEqual(str(context.exception), "Age not valid!")

    def testAge_whenAgeIsValid_shouldChangeName(self):
        s_name = 'Dari'
        s_age = 26
        survivor = Survivor(s_name, s_age)
        survivor.age = 40
        self.assertEqual(survivor.age, 40)

    def testHealth_whenIsNotValid_shouldRaiseValueError(self):
        s_name = 'Dari'
        s_age = 26
        survivor = Survivor(s_name, s_age)
        with self.assertRaises(ValueError) as context:
            survivor.health = -5
        self.assertEqual(str(context.exception), "Health not valid!")

    def testHealth_whenIsAbove100_shouldChangeHealth(self):
        s_name = 'Dari'
        s_age = 26
        survivor = Survivor(s_name, s_age)
        survivor.health = 150
        self.assertEqual(survivor.health, 100)
        survivor.health = 50
        self.assertEqual(survivor.health, 50)

    def testNeeds_whenIsNotValid_shouldRaiseValueError(self):
        s_name = 'Dari'
        s_age = 26
        survivor = Survivor(s_name, s_age)
        with self.assertRaises(ValueError) as context:
            survivor.needs = -5
        self.assertEqual(str(context.exception), "Needs not valid!")

    def testNeeds_whenIsAbove100_shouldChangeNeed(self):
        s_name = 'Dari'
        s_age = 26
        survivor = Survivor(s_name, s_age)
        survivor.needs = 150
        self.assertEqual(survivor.needs, 100)
        survivor.needs = 50
        self.assertEqual(survivor.needs, 50)

    def testNeedsHealing_whenIsAbove100_shouldCCheckTrue(self):
        s_name = 'Dari'
        s_age = 26
        survivor = Survivor(s_name, s_age)
        self.assertFalse(survivor.health < 100)
        self.assertFalse(survivor.needs_healing)

    def testNeedsSustenance_whenIsAbove100_shouldCCheckTrue(self):
        s_name = 'Dari'
        s_age = 26
        survivor = Survivor(s_name, s_age)
        self.assertFalse(survivor.needs < 100)
        self.assertFalse(survivor.needs_sustenance)


if __name__ == '__main__':
    unittest.main()
