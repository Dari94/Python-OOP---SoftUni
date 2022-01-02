from inheritance_05.mix_it.project.capacity_mixin import CapacityMixin


class ParkingMall(CapacityMixin):
    def __init__(self, parking_lots: float):
        self.parking_lots = parking_lots

    def check_availability(self,lots):
        result = self.get_capacity(self.parking_lots,lots)
        if isinstance(result, str):
            return "There are no more parking lots!"
        self.parking_lots -= 1
        return f'Parking lots available: {result}'
