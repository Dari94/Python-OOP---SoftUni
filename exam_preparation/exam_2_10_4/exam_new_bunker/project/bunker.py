from project.survivor import Survivor
from project.supply.supply import Supply
from project.medicine.medicine import Medicine


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
        water_supplies = [obj for obj in self.supplies if obj.__class__.__name__ == "WaterSupply"]
        if len(water_supplies) == 0:
            raise IndexError("There are no water supplies left!")
        return water_supplies

    @property
    def painkillers(self):
        painkillers_medicines = [obj for obj in self.medicine if obj.__class__.__name__ == "PainKiller"]
        if len(painkillers_medicines) == 0:
            raise IndexError("There are no painkillers left!")
        return painkillers_medicines

    @property
    def salves(self):
        salves_medicines = [obj for obj in self.medicine if obj.__class__.__name__ == "Salve"]
        if len(salves_medicines) == 0:
            raise IndexError("There are no salves left!")
        return salves_medicines

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type):
        if not survivor.needs_healing:
            return
        if medicine_type == "Painkiller":
            pill = self.painkillers.pop()
        else:
            pill = self.salves.pop()
        self.medicine.remove(pill)
        pill.apply(survivor)
        # survivor.health += pill.health_increase
        return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type):
        if not survivor.needs_sustenance:
            return
        if sustenance_type == "FoodSupply":
            supp = self.food.pop()
        else:
            supp = self.water.pop()
        self.supplies.remove(supp)
        supp.apply(survivor)
        return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
        for survivor in self.survivors:
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")
