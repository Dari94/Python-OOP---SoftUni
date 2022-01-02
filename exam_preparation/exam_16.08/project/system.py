from project.hardware.hardware import Hardware
from project.software.software import Software
from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        a = PowerHardware(name, capacity, memory)
        System._hardware.append(a)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        a = HeavyHardware(name, capacity, memory)
        System._hardware.append(a)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        list_hardware = [hardware for hardware in System._hardware if hardware.name == hardware_name]
        if not list_hardware:
            return "Hardware does not exist"
        else:
            if list_hardware[0].name == hardware_name:
                express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
                har = list_hardware[0]
                har.install(express_software)
                try:
                    har.install(express_software)
                except Exception as ex:
                    return str(ex)
                System._software.append(express_software)
                System._software.append(express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        list_hardware = [hardware for hardware in System._hardware if hardware.name == hardware_name]
        if not list_hardware:
            return "Hardware does not exist"
        else:
            light_software = LightSoftware(name, capacity_consumption, memory_consumption)
            har = list_hardware[0]
            try:
                har.install(light_software)
                System._software.append(light_software)
            except Exception as ex:
                return str(ex)
            System._software.append(light_software)
            System._software.append(light_software)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardware = [o for o in System._hardware if o.name == hardware_name]
        software = [o for o in System._software if o.name == software_name]
        if hardware and software:
            hardware[0].uninstall(software)
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
