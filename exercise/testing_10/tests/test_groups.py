import unittest
from polymorfism_06.groups import Person
from polymorfism_06.groups import Group


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person('John', 'Smith')

    def test_PersonStr_shouldReturnName(self):
        result = str(self.person_1)
        self.assertIn('John', result)
        self.assertNotIn('ppp', result)
        self.assertEqual(result, 'John Smith')

    def test_PersonAdd_shouldAddName(self):
        person_2 = Person('Second', 'Rose')
        person_3 = self.person_1.name + " " + person_2.surname
        #self.assertEqual('John', person_3.name)
        #self.assertEqual('Rose', person_3.surname)
        self.assertEqual('John Rose', person_3)


class TestGroup(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person('John', 'Smith')
        self.person_2 = Person('Second', 'Rose')
        params = [self.person_1, self.person_2]
        self.group = Group('test', params)

    def test_GroupLen_shouldReturnLen(self):
        result = self.group
        self.assertEqual(2,len(result))

    def test_GroupAdd_shouldReturnLen(self):
        person_3 = Person('Ivan', 'Les')
        group_2 = Group('test2', [person_3])
        group_3 = self.group + group_2

        self.assertEqual(3, len(group_3))

    def test_GroupGetitem_shouldReturnName(self):
        result = self.group[1]
        self.assertIn('Second', result)
        self.assertEqual('Person 1: Second Rose', result)

    def testGroupGetitem_invalidIndex(self):
        with self.assertRaises(Exception) as context:
            result = self.group[2]
        self.assertIsNotNone(context.exception)

    def test_GroupStr(self):
        result = str(self.group)
        self.assertIn('test', result)
        self.assertIn('John', result)
        self.assertIn('Second', result)
        self.assertNotIn('Ivan', result)
        self.assertEqual('Group test with members John Smith, Second Rose', result)


if __name__ == '__main__':
    unittest.main()
