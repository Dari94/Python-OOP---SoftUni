from project.factory.factory import Factory


class ChocolateFactory(Factory):

    def __init__(self, name, capacity):
        super().__init__(name, capacity)
        self.recipes = {}
        self.products = {}

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if not self.can_add(quantity):
            raise ValueError("Not enough space in factory")
        elif ingredient_type not in ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")
        elif self.can_add(quantity):
            if ingredient_type not in self.ingredients:
                self.ingredients[ingredient_type] = quantity
            else:
                self.ingredients[ingredient_type] += quantity

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in self.ingredients:
            raise KeyError("No such product in the factory")
        elif self.ingredients[ingredient_type] - quantity < 0:
            raise ValueError("Ingredient quantity cannot be less than zero")
        self.ingredients[ingredient_type] -= quantity

    def add_recipe(self, recipe_name: str, recipe: dict):
        if recipe_name not in self.recipes:
            self.recipes[recipe_name] = recipe

        self.recipes[recipe_name].update(recipe)

    def make_chocolate(self, recipe_name: str):
        if recipe_name not in self.recipes:
            raise TypeError("No such recipe")
        if recipe_name in self.products:
            self.products[recipe_name] += 1
        else:
            self.products[recipe_name] = 1

#choco = ChocolateFactory('Dari', 15)
#print(choco.__dict__)
#print(choco.__class__.__name__)
# choco.add_ingredient('dark chocolate', 6)

# choco.add_ingredient('sugar', 2)
# print(choco.__dict__)
# choco.remove_ingredient('sugar', 1)
# print(choco.__dict__)
# print(choco.__dict__)
# choco.add_recipe('new', {'dark chocolate': 2, 'sugar': 1})
# print(choco.__dict__)
# choco.add_recipe('new1', {'dark chocolate': 3, 'milk chocolate': 1})
# print(choco.__dict__)
# choco.make_chocolate('new')
# choco.make_chocolate('new1')

# print(choco.__dict__)
