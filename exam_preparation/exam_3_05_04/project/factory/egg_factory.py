from project.factory.factory import Factory


class EggFactory(Factory):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if not self.can_add(quantity):
            raise ValueError("Not enough space in factory")
        elif ingredient_type not in ["chicken egg", "quail egg"]:
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

    @property
    def products(self):
        return self.ingredients
