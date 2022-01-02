from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory


class EasterShop:
    def __init__(self, name, chocolate_factory, egg_factory, paint_factory):
        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = dict()

    def add_chocolate_ingredient(self, ingredient_type: str, quantity: int):
        self.chocolate_factory.add_ingredient(ingredient_type, quantity)

    def add_egg_ingredient(self, ingredient_type: str, quantity: int):
        self.egg_factory.add_ingredient(ingredient_type, quantity)

    def add_paint_ingredient(self, ingredient_type: str, quantity: int):
        self.paint_factory.add_ingredient(ingredient_type, quantity)

    def make_chocolate(self, recipe: str):
        if self.chocolate_factory.make_chocolate(recipe) != "No such recipe":
            if recipe not in self.storage:
                self.storage[recipe] = 1
            else:
                self.storage[recipe] += 1

    def paint_egg(self, color: str, egg_type: str):
        if color in self.paint_factory.products and egg_type in self.egg_factory.products:
            key = f"{color} {egg_type}"
            if key not in self.storage:
                self.storage[key] = 1
            else:
                self.storage[key] += 1
            self.paint_factory.remove_ingredient(color, 1)
            self.egg_factory.remove_ingredient(egg_type, 1)

        else:
            raise ValueError("Invalid commands")

    def __repr__(self):
        result = f"Shop name: {self.__class__.__name__}\n"
        result += f"Shop Storage:\n"

        for name, quantity in self.storage.items():
            result += f"{name}: {quantity}\n"

        return result

# choco = EasterShop('new_shop','Dari','ff','cc')
# print(choco.__dict__)
# choco.add_chocolate_ingredient('dark chocolate', 6)
