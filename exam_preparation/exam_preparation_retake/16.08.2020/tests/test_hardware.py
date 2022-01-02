import unittest
from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware


class testHardware(unittest.TestCase):
    def test_initHardwareAttributes(self):
        h_name = 'h1'
        h_type = "Heavy"
        capacity = 50
        memory = 100

        har = Hardware(h_name, h_type, capacity, memory)
        self.assertEqual(har.name, h_name)
        self.assertEqual(har.type, "Heavy")
        self.assertEqual(har.capacity, capacity)
        self.assertEqual(har.software_components, [])

    def test_Install_whenCapacityNotEnough_RaiseError(self):
        h_name = 'h1'
        h_type = "Heavy"
        har = Hardware(h_name, h_type, 500, 500)
        exp_s = ExpressSoftware('exp_soft', 600, 200)
        with self.assertRaises(Exception) as context:
            har.install(exp_s)
        self.assertIsNotNone(context.exception)

    def test_Install_whenMemoryNotEnough_RaiseError(self):
        h_name = 'h1'
        h_type = "Heavy"
        har = Hardware(h_name, h_type, 500, 500)
        exp_s = ExpressSoftware('exp_soft', 100, 600)
        with self.assertRaises(Exception) as context:
            har.install(exp_s)
        self.assertIsNotNone(context.exception)

    def test_Install_whenNotEnough_RaiseErrorMeassage(self):
        h_name = 'h1'
        h_type = "Heavy"
        har = Hardware(h_name, h_type, 500, 500)
        exp_s = ExpressSoftware('exp_soft', 100, 600)
        with self.assertRaises(Exception) as context:
            har.install(exp_s)
        self.assertEqual(str(context.exception), "Software cannot be installed")

    def test_Install_whenCapacityEnough_AddComponent(self):
        h_name = 'h1'
        h_type = "Heavy"
        har = Hardware(h_name, h_type, 500, 500)
        exp_s = ExpressSoftware('exp_soft', 30, 30)
        har.install(exp_s)
        expected = [exp_s]
        self.assertEqual(har.software_components, expected)

    def test_Uninstall_RemoveComponent(self):
        h_name = 'h1'
        h_type = "Heavy"
        har = Hardware(h_name, h_type, 500, 500)
        exp_s = ExpressSoftware('exp_soft', 30, 30)
        har.install(exp_s)
        self.assertEqual(har.software_components, [exp_s])
        har.install(exp_s)
        self.assertEqual(har.software_components, [exp_s, exp_s])
        har.uninstall(exp_s)
        self.assertEqual(har.software_components, [exp_s])


if __name__ == '__main__':
    unittest.main()
