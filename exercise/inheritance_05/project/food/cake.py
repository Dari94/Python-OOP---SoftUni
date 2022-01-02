from inheritance_05.project.food.dessert import Dessert


class Cake(Dessert):
    CAKE_GRAMS = 250
    CAKE_CALORIES = 1000
    CAKE_PRICE = 5

    # def __init__(self, name, price, grams,calories):
    #   super().__init__(name, price, grams)
    #   self.__calories = calories

    def __init__(self, name):
        super().__init__(name, Cake.CAKE_PRICE,Cake.CAKE_GRAMS,Cake.CAKE_CALORIES)

#inheritance_05.restaurant_