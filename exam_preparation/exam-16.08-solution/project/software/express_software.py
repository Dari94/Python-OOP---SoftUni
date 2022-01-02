from project.software.software import Software


class ExpressSoftware(Software):
    def __init__(self,name, capacity_consumption, memory_consumption, type='Express'):
        Software.__init__(self, name, type, int(capacity_consumption), int(memory_consumption*2))
