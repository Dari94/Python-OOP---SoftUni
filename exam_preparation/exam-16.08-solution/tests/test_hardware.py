import unittest

from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware

class test_hardware(unittest.TestCase):
    def test_init_hardware(self):
        hard = Hardware('nqma', 'Heavy', 100, 100)
        self.assertEqual([], hard.software_components)
        self.assertEqual(100, hard.memory)
        self.assertEqual(100, hard.capacity)
        self.assertEqual(hard.type, 'Heavy')

    def test_working_install(self):
        software = ExpressSoftware('s', 10, 10)
        hard = Hardware('nqma', 'hm', 100, 100)
        hard.install(software)
        self.assertEqual([software], hard.software_components)

    def test_not_working_installMemory(self):
        software = ExpressSoftware('s', 10, 100)
        hard = Hardware('nqma', 'hm', 11, 10)
        with self.assertRaises(Exception) as expect:
            hard.install(software)
        self.assertIsNotNone(expect)

    def test_not_working_install(self):
        software = ExpressSoftware('s', 100, 10)
        hard = Hardware('nqma', 'hm', 10, 11)
        with self.assertRaises(Exception) as expect:
            hard.install(software)
        self.assertIsNotNone(expect)

    def test_uninstall(self):
        software = ExpressSoftware('s', 10, 10)
        hard = Hardware('nqma', 'hm', 100, 100)
        hard.install(software)
        self.assertEqual([software], hard.software_components)
        hard.uninstall(software)
        self.assertEqual([], hard.software_components)

    def test_notworkingInstallMessage(self):
        software = ExpressSoftware('s', 100, 10)
        hard = Hardware('nqma', 'hm', 10, 11)
        try:
            hard.install(software)
        except Exception as ex:
            self.assertEqual(str(ex), "Software cannot be installed")