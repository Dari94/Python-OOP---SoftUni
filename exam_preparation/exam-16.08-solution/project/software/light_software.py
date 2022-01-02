from project.software.software import Software


class LightSoftware(Software):
    def __init__(self,name, capacity_consumption, memory_consumption, type='Light'):
        Software.__init__(self, name, type, int(capacity_consumption*1.5), int(memory_consumption//2))
