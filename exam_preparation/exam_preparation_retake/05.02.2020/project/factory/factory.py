from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}

    @abstractmethod
    def add_ingredient(self, ingredient_type, quantity):
        pass

    @abstractmethod
    def remove_ingredient(self, ingredient_type, quantity):
        pass

    def can_add(self,value):
        return self.capacity - sum(self.ingredients.values()) - value >= 0

