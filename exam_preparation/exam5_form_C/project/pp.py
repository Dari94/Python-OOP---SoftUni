from project.robots.robot import Robot
from abc import ABC, abstractmethod
from project.robots.robot import Robot
from project.robots.pet_robot import PetRobot
class Procedure(ABC):
    def __init__(self, robot):
        self.robots = robot

    def history(self):
        result = f"{self.__class__.__name__}\n"
        result += f"Robot type: {Robot.__class__.__name__} - {Robot.name} - Happiness: {Robot.happiness} - " \
                  f"Energy: {Robot.energy}"
        for robot,res in self.robots.items():
            self.robots[robot].append(result)
