class PizzaDelivery:
    ordered = False

    def __init__(self, name: str, price: float,ingredients = {}):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        elif ingredient in self.ingredients.keys():
            self.ingredients[ingredient] += quantity
            self.price += ingredient_price * quantity
        elif ingredient not in self.ingredients.keys():
            self.ingredients[ingredient] = quantity
            self.price += ingredient_price * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        elif ingredient not in self.ingredients.keys():
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        elif self.ingredients[ingredient] - quantity < 0:
            return f"Please check again the desired quantity of {ingredient}!"
        self.ingredients[ingredient] -= quantity
        self.price -= quantity * ingredient_price

    def repr_ingredients_and_quantity(self):
        formated_ing_list = []
        for ing, quantity in self.ingredients.items():
            formated_ing_list.append(f"{ing}: {quantity}")
        return formated_ing_list

    def pizza_ordered(self):
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with " \
               f"{', '.join(self.repr_ingredients_and_quantity())} and the price will be {self.price}lv."


Margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
Margarita.add_extra('mozzarella', 1, 0.5)
Margarita.add_extra('cheese', 1, 1)
Margarita.remove_ingredient('cheese', 1, 1)
print(Margarita.remove_ingredient('bacon', 1, 2.5))
print(Margarita.remove_ingredient('tomatoes', 2, 0.5))
Margarita.remove_ingredient('cheese', 2, 1)
print(Margarita.pizza_ordered())
print(Margarita.add_extra('cheese', 1, 1))