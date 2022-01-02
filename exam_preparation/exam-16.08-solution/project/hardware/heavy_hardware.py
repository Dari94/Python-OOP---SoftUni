from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name, capacity, memory, type= "Heavy"):
        Hardware.__init__(self, name, type, int(capacity*2), int(memory*0.75))
