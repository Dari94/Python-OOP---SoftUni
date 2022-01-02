from project.survivor import Survivor
class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_supplies = [obj for obj in self.supplies if obj.__class__.__name__ == "FoodSupply"]
        if len(food_supplies) == 0:
            raise IndexError("There are no food supplies left!")
        return food_supplies

    @property
    def water(self):
        water_supplies = [obj for obj in self.supplies if obj.__class__.__name__ == "WaterSupplies"]
        if len(water_supplies) == 0:
            raise IndexError("There are no water supplies left!")
        return water_supplies

    @property
    def painkillers(self):
        painkillers_medicine = [obj for obj in self.medicine if obj.__class__.__name__ == "Painkiller"]
        if len(painkillers_medicine) == 0:
            raise IndexError("There are no painkillers left!")
        return painkillers_medicine

    @property
    def salves(self):
        salves_medicine = [obj for obj in self.medicine if obj.__class__.__name__ == "Salves"]
        if len(salves_medicine) == 0:
            raise IndexError("There are no salves left!")
        return salves_medicine

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if not survivor.needs_healing:
            return
        if medicine_type == "Painkiller":
            pill = self.painkillers.pop(-1)
        else:
            pill = self.salves.pop(-1)
        pill.apply(survivor)
        self.medicine.remove(pill)
        return f"{survivor.name} sustained successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if not survivor.needs_sustenance:
            return
        if sustenance_type == "FoodSupply":
            supp = self.food.pop(-1)
        else:
            supp = self.food.pop(-1)
        supp.apply(survivor)
        self.supplies.remove(supp)
        return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for s in self.survivors:
            s.needs -= 2 * s.age

        for s in self.survivors:
            self.sustain(s, 'FoodSupply')
            self.sustain(s, 'WaterSupply')


