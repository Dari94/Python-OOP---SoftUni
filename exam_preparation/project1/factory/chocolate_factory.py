from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name, capacity, ingredients={}):
        super().__init__(name, capacity, ingredients={})
        self.recipes = {}
        self.products = {}
        self.ingredients = ingredients

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
        elif recipe_name in self.recipes:
            self.recipes[recipe_name].update(recipe)

    def make_chocolate(self, recipe_name: str):
        if recipe_name not in self.recipes:
            raise TypeError("No such recipe")
        else:

            if recipe_name not in self.products:
                dict_products = [x for x in self.recipes.values()][0]
                self.products[recipe_name] = dict_products
                for key, value in dict_products.items():
                    if self.ingredients[key] - value > 0:
                        self.ingredients[key] -= value
                    else:
                        self.ingredients.pop(key)
            else:
                dict_products = [x for x in self.products.values()][0]

                for key, value in dict_products.items():
                    dict_products[key] = value
                    print(key, value)
                    if self.ingredients[key] - value > 0:
                        self.ingredients[key] -= value
                    else:
                        self.ingredients.pop(key)

# choco = ChocolateFactory('Dari', 15)
# print(choco.__dict__)
# choco.add_ingredient('dark chocolate', 6)
# choco.add_ingredient('sugar', 2)
# choco.add_ingredient('milk chocolate', 3)
# choco.add_recipe('new', {'dark chocolate': 2, 'sugar': 1})
# print(choco.__dict__)
# choco.add_recipe('new1', {'dark chocolate': 3, 'milk chocolate': 1})
# print(choco.__dict__)
# choco.make_chocolate('new')
# choco.make_chocolate('new1')

# print(choco.__dict__)
