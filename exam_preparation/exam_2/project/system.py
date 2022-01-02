from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = [o for o in System._hardware if o.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        else:
            hard = hardware[0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            if hard.install(software) != "Software cannot be installed":
                hard.install(software)
                System._software.append(software)


    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = [o for o in System._hardware if o.name == hardware_name]
        if hardware:
            hard = hardware[0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            try:
                hard.install(software)
            except Exception as ex:
                return str(ex)
            System._software.append(software)
        else:
            return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardware = [o for o in System._hardware if o.name == hardware_name]
        software = [o for o in System._software if o.name == software_name]
        if hardware and software:
            hardware[0].uninstall(software[0])
            System._software.remove(software[0])
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {sum([o.memory_consumption for o in System._software])} / {sum([o.memory for o in System._hardware])}\n" \
               f"Total Capacity Taken: {sum([o.capacity_consumption for o in System._software])} / {sum([o.capacity for o in System._hardware])}"

    @staticmethod
    def system_split():
        string = ""
        for h in System._hardware:
            if [o.name for o in h.software_components]:
                sc = ', '.join([o.name for o in h.software_components])
            else:
                sc = 'None'
            string += f"Hardware Component - {h.name}\n" \
                      f"Express Software Components: {len([o for o in h.software_components if o.type == 'Express'])}\n" \
                      f"Light Software Components: {len([o for o in h.software_components if o.type == 'Light'])}\n" \
                      f"Memory Usage: {sum([o.memory_consumption for o in h.software_components])} / {h.memory}\n" \
                      f"Capacity Usage: {sum([o.capacity_consumption for o in h.software_components])} / {h.capacity}\n" \
                      f"Type: {h.type}\n" \
                      f"Software Components: {sc}"
        return string

System.register_power_hardware("HDD", 200, 200)
System.register_heavy_hardware("SSD", 400, 400)
print(System.analyze())
System.register_light_software("HDD", "Test", 0, 10)
print(System.register_express_software("HDD", "Test2", 100, 100))
System.register_express_software("HDD", "Test3", 50, 100)
System.register_light_software("SSD", "Windows", 20, 50)
System.register_express_software("SSD", "Linux", 50, 100)
System.register_light_software("SSD", "Unix", 20, 50)
print(System.analyze())
System.release_software_component("SSD", "Linux")
print(System.system_split())
