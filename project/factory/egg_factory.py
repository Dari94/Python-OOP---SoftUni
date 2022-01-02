from project.factory.factory import Factory


class EggFactory(Factory):
    def __init__(self, name, capacity,ingredients = {}):
        super().__init__(name, capacity, ingredients={})

    def add_ingredient(self, ingredient_type: str, quantity: int):
        pass

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        pass

    @property
    def products(self):
        return self.ingredients

