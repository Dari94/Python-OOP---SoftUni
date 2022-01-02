from abc import ABC, abstractmethod


class Robot(ABC):

    @abstractmethod
    def __init__(self, name, energy, happiness, procedure_time):
        self.name = name
        self.energy = energy
        self.happiness = happiness
        self.procedure_time = procedure_time
        self.owner = "Service"
        self.isBought = False
        self.isChipped = False
        self.isChecked = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def happiness(self):
        return self.__happiness

    @happiness.setter
    def happiness(self, value):
        if value < 0 or value > 100:
            raise ValueError("Invalid happiness")
        self.__happiness = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        if value < 0 or value > 100:
            raise ValueError("Invalid energy")
        self.__energy = value

    @property
    def procedure_time(self):
        return self.__procedure_time

    @procedure_time.setter
    def procedure_time(self, value):
        self.__procedure_time = value

    def __repr__(self):
        return f" Robot type: {self.__class__.__name__} - {self.name} - Happiness: {self.happiness} - Energy: " \
               f"{self.energy} "
