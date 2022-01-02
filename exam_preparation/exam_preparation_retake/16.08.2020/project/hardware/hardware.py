from project.software.light_software import LightSoftware


class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if value in ["Heavy", "Power"]:
            self.__type = value

    def can_install(self, software):
        has_space = sum([s.capacity_consumption for s in self.software_components]) + software.capacity_consumption \
                    <= self.capacity
        has_memory = sum([s.memory_consumption for s in self.software_components]) + software.memory_consumption \
                     <= self.memory
        return has_space and has_memory

    def install(self, software):
        if self.can_install(software):
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software):
        self.software_components.remove(software)

# hw = Hardware('gg', "Heavy", 100, 100)
# lw = LightSoftware('l11', 10,10)
# hw.install(lw)
# print(hw.__dict__)
