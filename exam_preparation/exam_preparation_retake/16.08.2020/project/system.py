from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        p_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(p_hardware)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        h_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(h_hardware)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware_list = [h for h in System._hardware if h.name == hardware_name]
        if hardware_list:
            hard = hardware_list[0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            try:
                hard.install(software)
            except Exception as ex:
                return str(ex)
            System._software.append(software)
        else:
            return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware_list = [h for h in System._hardware if h.name == hardware_name]
        if hardware_list:
            hard = hardware_list[0]
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
        hardware_list = [h for h in System._hardware if h.name == hardware_name]
        software_list = [s for s in System._software if s.name == software_name]
        if hardware_list and software_list:
            hard = hardware_list[0]
            software = software_list[0]
            hard.uninstall(software)
            System._software.remove(software)
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = f"System Analysis\n"
        result += f"Hardware Components: {len(System._hardware)}\n"
        result += f"Software Components: {len(System._software)}\n"
        result += f"Total Operational Memory: {sum([s.memory_consumption for s in System._software])} / {sum([h.memory for h in System._hardware])}\n"
        result += f"Total Capacity Taken: {sum([s.capacity_consumption for s in System._software])}" \
                  f" / {sum([h.capacity for h in System._hardware])}"
        return result

    @staticmethod
    def system_split():
        result = ""
        for h in System._hardware:
            if [o.name for o in h.software_components]:
                sc = ",".join([o.name for o in h.software_components])
            else:
                sc = "None"
            result += f"Hardware Component - {h.name}\n"\
                    f"Express Software Components: {len([o for o in h.software_components if o.type =='Express'])}\n"\
                    f"Light Software Components: {len([o for o in h.software_components if o.type=='Light'])}\n"\
                    f"Memory Usage: {sum([o.memory_consumption for o in h.software_components])} / {h.memory}\n"\
                    f"Capacity Usage: {sum([o.capacity_consumption for o in h.software_components])} / {h.capacity}\n"\
                    f"Type: {h.type}\n"\
                    f"Software Components: {sc}"
        return result



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


