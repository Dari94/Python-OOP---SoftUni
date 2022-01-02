from project.hardware.hardware import Hardware
#from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware
import unittest


class TestHardware(unittest.TestCase):
    def test_initHardwareAttributes(self):
        h_name = repr('h1')
        h_type = "Heavy"
        capacity = 50
        memory = 100

        har = Hardware(h_name, h_type, capacity, memory)
        self.assertEqual(har.name, h_name)
        self.assertEqual(har.type, "Heavy")
        self.assertEqual(har.capacity, capacity)
        self.assertEqual(har.software_components, [])

    def test_Hardware_NotInstalled_tLight(self):
        h_name = 'Ppp'
        h_type = "Heavy"
        capacity = 50
        memory = 100

        har = Hardware(h_name, h_type, capacity, memory)
        l_soft = LightSoftware('Hp', 70, 110)
        with self.assertRaises(Exception) as context:
            har.install(l_soft)
        self.assertEqual(str(context.exception), "Software cannot be installed")

    def test_Hardware_NotInstalled_Express(self):
        h_name = 'Ppp'
        h_type = "Heavy"
        capacity = 50
        memory = 100

        har = Hardware(h_name, h_type, capacity, memory)
        ex_soft = ExpressSoftware('Hp', 70, 110)
        with self.assertRaises(Exception) as context:
            har.install(ex_soft)
        self.assertEqual(str(context.exception), "Software cannot be installed")

    def test_HardwareInstalledLight(self):
        h_name = 'Ppp'
        h_type = "Heavy"
        capacity = 200
        memory = 100

        har = Hardware(h_name, h_type, capacity, memory)
        l_soft = LightSoftware('Hp', 40, 30)
        har.install(l_soft)
        self.assertEqual(len(har.software_components), 1)

    def test_HardwareInstalledExpress(self):
        h_name = 'Ppp'
        h_type = "Heavy"
        capacity = 200
        memory = 100

        har = Hardware(h_name, h_type, capacity, memory)
        ex_soft = ExpressSoftware('Hp', 40, 30)
        har.install(ex_soft)
        self.assertEqual(len(har.software_components), 1)

    def test_HardwareUninstallLight(self):
        h_name = 'Ppp'
        h_type = "Heavy"
        capacity = 200
        memory = 100

        har = Hardware(h_name, h_type, capacity, memory)
        l_soft = LightSoftware('Hp', 40, 30)
        har.install(l_soft)
        l_soft1 = LightSoftware('Hp', 40, 30)
        har.install(l_soft1)
        har.uninstall(l_soft)
        self.assertEqual(len(har.software_components), 1)
    def test_Install_whenMemoryNotEnough_RaiseError(self):
        h_name = 'h1'
        h_type = "Heavy"
        har = Hardware(h_name, h_type, 500, 500)
        exp_s = ExpressSoftware('exp_soft', 100, 600)
        with self.assertRaises(Exception) as context:
            har.install(exp_s)
        self.assertIsNotNone(context.exception)


    def test_HardwareCountLight_llLight(self):
        h_name = 'Ppp'
        h_type = "Heavy"
        capacity = 200
        memory = 100

        har = Hardware(h_name, h_type, capacity, memory)
        l_soft = LightSoftware('Hp', 40, 30)
        har.install(l_soft)
        ex_soft1 = ExpressSoftware('Hp', 40, 30)
        har.install(ex_soft1)
        l_soft2 = LightSoftware('Hp', 20, 10)
        har.install(l_soft2)
        count_l = har.get_light_software_components_count()
        count_ex = har.get_express_software_components_count()
        self.assertEqual(count_l, 2)
        self.assertEqual(count_ex, 1)

    def test_repr_name(self):
        h_name = repr('h1')
        h_type = "Heavy"
        capacity = 50
        memory = 100

        har = Hardware(h_name, h_type, capacity, memory)
        self.assertEqual(har.name, h_name)

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

    def test_beginner_inherits_1_player(self):
        self.assertTrue("Software" == ExpressSoftware.__bases__[0].__name__)


if __name__ == '__main__':
    unittest.main()
