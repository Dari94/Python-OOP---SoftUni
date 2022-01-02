from project.survivor import Survivor
import unittest


class TestSurvivor(unittest.TestCase):
    def test_whenValidValues(self):
        s_name = 'test'
        s_age = 26
        health = 100
        needs = 100
        s = Survivor(s_name, s_age)
        self.assertEqual(s.name, s_name)
        self.assertEqual(s.age, s_age)
        self.assertEqual(s.health, health)
        self.assertEqual(s.needs, needs)
        self.assertEqual(s.needs_healing, False)
        self.assertEqual(s.needs_sustenance, False)

    def testName_whenIsNotValid_ShouldRaiseValueError(self):
        s_name = ""
        s_age = 26

        with self.assertRaises(ValueError) as context:
            Survivor(s_name, s_age)
        self.assertEqual(str(context.exception), "Name not valid!")

    def testAge_whenIsNotValid_ShouldRaiseValueError(self):
        s_name = 'test'
        s_age = -4
        with self.assertRaises(ValueError) as context:
            Survivor(s_name, s_age)
        self.assertEqual(str(context.exception), "Age not valid!")

    def testHealth_whenIsNotValid_Bellow0_ShouldRaiseValueError(self):
        s_name = 'test'
        s_age = 26
        s = Survivor(s_name, s_age)

        with self.assertRaises(ValueError) as context:
            s.health = -10
        self.assertEqual(str(context.exception), "Health not valid!")

    def testHealth_whenIsNotValid_Above100_ShouldRaiseValueError(self):
        s_name = 'test'
        s_age = 26
        s = Survivor(s_name, s_age)
        self.assertEqual(s.health, 100)
        s.health = 160
        self.assertEqual(s.health, 100)
        s.health = 50
        self.assertEqual(s.health, 50)

    def testNeeds_whenIsNotValid_Bellow0_ShouldRaiseValueError(self):
        s_name = 'test'
        s_age = 26
        s = Survivor(s_name, s_age)

        with self.assertRaises(ValueError) as context:
            s.needs = -10
        self.assertEqual(str(context.exception), "Needs not valid!")

    def testNeeds_whenIsNotValid_Above100_ShouldRaiseValueError(self):
        s_name = 'test'
        s_age = 26
        s = Survivor(s_name, s_age)
        self.assertEqual(s.needs, 100)
        s.needs = 160
        self.assertEqual(s.needs, 100)
        s.needs = 50
        self.assertEqual(s.needs, 50)

    def testNeedsHealing_whenHealthAbove100_ShouldRaiseValueError(self):
        s_name = 'test'
        s_age = 26
        s = Survivor(s_name, s_age)
        self.assertFalse(s.health < 100)
        self.assertFalse(s.needs_healing)

    def testNeedsHealing_whenHealthBellow100_ShouldRaiseValueError(self):
        s_name = 'test'
        s_age = 26
        s = Survivor(s_name, s_age)
        s.health = 60
        self.assertTrue(s.health < 100)
        self.assertTrue(s.needs_healing)

    def testNeedsSustenance_whenNeedsAbove100_ShouldRaiseValueError(self):
        s_name = 'test'
        s_age = 26
        s = Survivor(s_name, s_age)
        self.assertFalse(s.needs < 100)
        self.assertFalse(s.needs_sustenance)

    def testNeedsSustenance_whenNeedsBellow100_ShouldRaiseValueError(self):
        s_name = 'test'
        s_age = 26
        s = Survivor(s_name, s_age)
        s.needs = 60
        self.assertTrue(s.needs < 100)
        self.assertTrue(s.needs_sustenance)


if __name__ == '__main__':
    unittest.main()
