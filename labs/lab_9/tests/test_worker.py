import unittest

from lab_9.worker.worker import Worker


class TestWorker(unittest.TestCase):
    def test_workerInit_whenCorrectNameSalaryEnergy_shouldBeInitialized(self):
        """
	    Test if the worker is initialized with correct name, salary and energy
        """
        name = "Worker name"
        salary = 123
        energy = 5
        worker = Worker(name, salary, energy)
        self.assertEqual(name, worker.name)
        self.assertEqual(salary, worker.salary)
        self.assertEqual(energy, worker.energy)
        self.assertEqual(0, worker.money)

    def test_workerRest_shouldIncrementEnergy(self):
        """
        •	Test if the worker's energy is incremented after the rest method is called
        """
        name = "Worker name"
        salary = 123
        energy = 5
        worker = Worker(name, salary, energy)

        worker.rest()

        self.assertEqual(energy + 1, worker.energy)

    def test_workerWork_whenEnergyIs0_shouldRaiseException(self):
        """
        Test if an error is raised if the worker tries to work with negative energy or equal to 0
        """
        name = "Worker name"
        salary = 123
        energy = 0
        worker = Worker(name, salary, energy)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertIsNotNone(context.exception)

    def test_workerWork_whenEnergyAIsAbove_shouldIncreaseMoneyBySalary(self):
        """
        Test if the worker's money is increased by his salary correctly after the work method is called
        """
        name = "Worker name"
        salary = 123
        energy = 5

        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(salary, worker.money)
        worker.work()
        self.assertEqual(salary * 2, worker.money)

    def test_workerWork_whenEnergyAIsAbove_shouldDecreaseEnergy(self):
        """
        Test if the worker's energy is decreased after the work method is called
        """
        name = "Worker name"
        salary = 123
        energy = 5

        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(energy - 1, worker.energy)

    def test_workerGetInfo_shouldReturnCorrectString(self):
        """
        Test if the get_info method returns the proper string with correct values
        """
        name = "Worker name"
        salary = 123
        energy = 0

        worker = Worker(name, salary, energy)
        expected = f'{name} has saved 0 money.'

        actual = worker.get_info()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
