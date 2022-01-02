class Software:
    def __init__(self, name, type, capacity_consumption, memory_consumption):
        self.name = name
        self.type = type
        self.capacity_consumption = capacity_consumption
        self.memory_consumption = memory_consumption

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
        if value in ["Express", "Light"]:
            self.__type = value

    @property
    def capacity_consumption(self):
        return self.__capacity_consumption

    @capacity_consumption.setter
    def capacity_consumption(self, value):
        self.__capacity_consumption = value

    @property
    def memory_consumption(self):
        return self.__memory_consumption

    @memory_consumption.setter
    def memory_consumption(self, value):
        self.__memory_consumption = value


