from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory


class EasterShop():
    def __init__(self, name, storage = {}):
        self.name = name
        self._chocolate_factory = ChocolateFactory()
        self._egg_factory = EggFactory()
        self.paint_factory = paint_factory
        self.storage = storage

    def add_chocolate_ingredient(self, type: str, quantity: int):
        if not self.can_add(quantity):
            raise ValueError("Not enough space in factory")
        elif type not in ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]:
            raise TypeError(f"Ingredient of type {type} not allowed in {__class__.__name__.name}")
        elif self.can_add(quantity):
            if type not in __class__.__name__.ingredients:
                __class__.__name__.ingredients[ingredient_type] = quantity
            else:
                __class__.__name__.ingredients[ingredient_type] += quantity
            self.capacity -= quantity



    def add_egg_ingredient(self, type: str, quantity: int):
        self._egg_factory.add_ingredient(type,quantity)

    def add_paint_ingredient(self, type: str, quantity: int):
        pass

    def make_chocolate(self, recipe: str):
        pass

    def paint_egg(self, color: str, egg_type: str):
        pass

    def __repr__(self):
        return

choco = EasterShop('new_shop',{'ff'})
print(choco.__dict__)
#choco.add_chocolate_ingredient('dark chocolate', 6)