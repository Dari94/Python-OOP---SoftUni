from inheritance_05.mix_it.project.vehicle.vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, available_seats, tickets_price):
        self.tickets_sold = 0
        self.ticket_price = tickets_price
        super().__init__(available_seats)

    def get_ticket(self, tickets_count):
        result = Bus.get_capacity(self.available_seats, tickets_count)
        if isinstance(result, int):
            self.tickets_sold += tickets_count
            self.available_seats -= tickets_count
        return result

    def get_total_profit(self):
        return self.tickets_sold * self.ticket_price
