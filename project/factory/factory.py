from abc import ABC, abstractmethod


class Factory(ABC):

    def __init__(self, name, capacity, ingredients={}):
        self.name = name
        self.capacity = capacity
        self.ingredients = ingredients

    @abstractmethod
    def add_ingredient(self, ingredient_type: str, quantity: int):
        pass

    @abstractmethod
    def remove_ingredient(self, ingredient_type: str, quantity: int):
        pass

    def can_add(self, value: int):
        pass
