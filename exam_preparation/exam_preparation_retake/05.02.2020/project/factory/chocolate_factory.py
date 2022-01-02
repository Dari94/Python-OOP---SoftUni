from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)
        self.recipes = {}
        self.products = {}

    def add_ingredient(self, ingredient_type, quantity):
        ingredients = ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]
        if not self.can_add(quantity):
            raise ValueError("Not enough space in factory")
        elif ingredient_type not in ingredients:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")
        elif self.can_add(quantity):
            if ingredient_type not in self.ingredients:
                self.ingredients[ingredient_type] = quantity
            else:
                self.ingredients[ingredient_type] += quantity

    def remove_ingredient(self, ingredient_type, quantity):
        if self.ingredients[ingredient_type] - quantity < 0:
            raise ValueError("Ingredient quantity cannot be less than zero")
        elif ingredient_type not in self.ingredients:
            raise KeyError("No such product in the factory")
        else:
            self.ingredients[ingredient_type] -= quantity

    def add_recipe(self, recipe_name, recipe):
        if recipe_name not in self.recipes:
            self.recipes[recipe_name] = recipe
        else:
            self.recipes[recipe_name].update(recipe)

    def make_chocolate(self, recipe_name):
        if recipe_name not in self.recipes:
            raise TypeError("No such recipe")
        else:
            if recipe_name in self.recipes:
                self.products[recipe_name] += 1
            else:
                self.products[recipe_name] = 1

# cc = ChocolateFactory('ff', 40)
# cc.add_ingredient('dark chocolate', 2)
# cc.remove_ingredient('dark chocolate', 3)
# print(cc.__dict__)
