from project.survivor import Survivor
import unittest


class TestSurvivor(unittest.TestCase):
    def test_whenValidValues(self):
        s_name = 'Dari'
        s_age = 20

        s = Survivor(s_name,s_age)
        self.assertEqual(s.name , s_name)
        self.assertEqual(s.age , s_age)
        self.assertEqual(s.health , 100)
        self.assertEqual(s.needs , 100)

    def test_nameNotValid_raiseValueError(self):
        s_name = ""
        s_age = 20
        with self.assertRaises(ValueError) as context:
            Survivor(s_name, s_age)
        self.assertIsNotNone(context.exception)

    def test_AgeNotValid_raiseValueError(self):
        s_name = 'test'
        s_age = -4
        with self.assertRaises(ValueError) as context:
            Survivor(s_name, s_age)
        #self.assertEqual(str(context.exception), "Age not valid!")
        self.assertIsNotNone(context.exception)

    def test_nameAgeValid_raiseValueError(self):
        s_name = "Dari"
        s_age = 20
        s = Survivor(s_name, s_age)
        self.assertEqual(s.name , s_name)
        self.assertEqual(s.age, s_age)

    def test_healthAbove100Valid_shouldReturn100(self):
        s_name = "Dari"
        s_age = 20
        s = Survivor(s_name, s_age)
        s.health = 150
        s.needs = 200
        self.assertEqual(s.health , 100)
        self.assertEqual(s.needs , 100)

    def test_healthBellow100Valid_shouldReturn100(self):
        s_name = "Dari"
        s_age = 20
        s = Survivor(s_name, s_age)
        s.health = 40
        s.needs = 60
        self.assertEqual(s.health , 40)
        self.assertEqual(s.needs , 60)
        s.health = 100
        s.needs = 120
        self.assertEqual(s.health, 100)
        self.assertEqual(s.needs, 100)


    def test_healthNotValid_shouldReturn100(self):
        s_name = "Dari"
        s_age = 20
        s = Survivor(s_name, s_age)
        with self.assertRaises(ValueError) as context:
            s.health = -60
        self.assertIsNotNone(context.exception)

    def test_NeedNotValid_shouldReturn100(self):
        s_name = "Dari"
        s_age = 20
        s = Survivor(s_name, s_age)
        with self.assertRaises(ValueError) as context:
            s.needs = -60
        self.assertIsNotNone(context.exception)

    def test_HealthLessThan100(self):
        s_name = "Dari"
        s_age = 20
        s = Survivor(s_name, s_age)
        s.health = 60
        self.assertTrue(s.needs_healing)
        s.health = 120
        self.assertFalse(s.needs_healing)

    def test_NeedsLessThan100(self):
        s_name = "Dari"
        s_age = 20
        s = Survivor(s_name, s_age)
        s.needs = 60
        self.assertTrue(s.needs_sustenance)
        s.needs = 120
        self.assertFalse(s.needs_sustenance)



if __name__ == '__main__':
    unittest.main()
