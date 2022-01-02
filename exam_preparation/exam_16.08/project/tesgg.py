class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software):
        if self.can_install(software):
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software):
        self.software_components.remove(software)

    def get_light_software_components_count(self):
        return len([s for s in self.software_components if s.type == "Light"])

    def get_express_software_components_count(self):
        return len([s for s in self.software_components if s.type == "Express"])

    def can_install(self, software):
        has_space = sum(
            [s.capacity_consumption for s in self.software_components]) + software.capacity_consumption <= self.capacity
        has_memory = sum(
            [s.memory_consumption for s in self.software_components]) + software.memory_consumption <= self.memory
        return has_memory and has_space

    def __repr__(self):
        result = [f"Hardware Component - {self.name}",
                  f"Express Software Components: {self.get_express_software_components_count()}",
                  f"Light Software Components: {self.get_light_software_components_count()}",
                  f"Memory Usage: {sum([s.memory_consumption for s in self.software_components])} / {self.memory}",
                  f"Capacity Usage: {sum([s.capacity_consumption for s in self.software_components])} / {self.capacity}",
                  f"Type: {self.type}",
                  f"Software Components: {', '.join([str(s) for s in self.software_components]) if self.software_components else 'None'}"]

        return "\n".join(result)


class Software:
    def __init__(self, name: str, type: str, capacity_consumption: int, memory_consumption: int):
        self.name = name
        self.type = type
        self.capacity_consumption = capacity_consumption
        self.memory_consumption = memory_consumption

    def __repr__(self):
        return self.name


from project.software.software import Software


class ExpressSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, "Express", int(capacity_consumption), int(memory_consumption * 2))


from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware


class Test:
    def test_initHardwareAttributes(self):
        h_name = 'h1'
        h_type = "Heavy"
        capacity = 50
        memory = 100

        har = Hardware(h_name, h_type, capacity, memory)
        self.assertEqual(har.name, h_name)
        self.assertEqual(har.type, "Heavy")
        self.assertEqual(har.capacity, capacity)
        self.assertEqual(len(har.software_components), 0)

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


if __name__ == '__main__':
    unittest.main()
