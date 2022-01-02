from inheritance_05.project.beverage.hot_beverage import HotBeverage


class Tea(HotBeverage):

    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)
