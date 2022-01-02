from project.factory.factory import Factory


class EggFactory(Factory):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    def add_ingredient(self, ingredient_type, quantity):
        ingredients = ["chicken egg", "quail egg"]
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
        elif ingredient_type not in self.ingredients.keys():
            raise KeyError("No such product in the factory")
        else:
            self.ingredients[ingredient_type] -= quantity

    @property
    def products(self):
        return self.ingredients
