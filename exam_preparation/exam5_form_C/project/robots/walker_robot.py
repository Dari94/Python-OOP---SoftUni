from project.robots.robot import Robot


class WalkerRobot(Robot):
    def __init__(self, name, energy, happiness, procedure_time):
        super().__init__(name, energy, happiness, procedure_time)