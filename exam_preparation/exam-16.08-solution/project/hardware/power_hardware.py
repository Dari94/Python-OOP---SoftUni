from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name, capacity, memory, type="Power"):
        Hardware.__init__(self, name, type, int(capacity*0.25), int(memory*1.75))
