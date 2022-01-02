class Hardware:




    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if value in ["Heavy", "Power"]:
            self.__type = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__capacity = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def can_install(self, software):
        has_space = sum(
            [s.capacity_consumption for s in self.software_components]) + software.capacity_consumption <= self.capacity
        has_memory = sum(
            [s.memory_consumption for s in self.software_components]) + software.memory_consumption <= self.memory
        return has_memory and has_space

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

    def __repr__(self):
        result = [f"Hardware Component - {self.name}",
                  f"Express Software Components: {self.get_express_software_components_count()}",
                  f"Light Software Components: {self.get_light_software_components_count()}",
                  f"Memory Usage: {sum([s.memory_consumption for s in self.software_components])} / {self.memory}",
                  f"Capacity Usage: {sum([s.capacity_consumption for s in self.software_components])} / {self.capacity}",
                  f"Type: {self.type}",
                  f"Software Components: {', '.join([str(s) for s in self.software_components]) if self.software_components else 'None'}"]

        return "\n".join(result)
