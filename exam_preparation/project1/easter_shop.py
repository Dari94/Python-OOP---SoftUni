from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory


class EasterShop():
    def __init__(self, name, chocolate_factory, egg_factory, paint_factory, storage = {}):
        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = storage

    def add_chocolate_ingredient(self, type: str, quantity: int):
        pass



    def add_egg_ingredient(self, type: str, quantity: int):
        pass

    def add_paint_ingredient(self, type: str, quantity: int):
        pass

    def make_chocolate(self, recipe: str):
        pass

    def paint_egg(self, color: str, egg_type: str):
        pass

    def __repr__(self):
        return

#choco = EasterShop('new_shop','Dari','ff','cc')
#print(choco.__dict__)
#choco.add_chocolate_ingredient('dark chocolate', 6)