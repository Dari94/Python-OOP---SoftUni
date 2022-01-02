from abc import ABC, abstractmethod
class Gun(ABC):
    @abstractmethod
    def __init__(self,name,bullets_count):
        self.name = name
        self.bullets_count = bullets_count

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        if value == "" or value == 0:
            raise ValueError("Gun cannot be null or empty.")
        self.__name = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == 0:
            raise ValueError("Gun cannot be null or empty.")
        self.__name = value


