from inheritance_05.zoo.project.animal import Animal


class Mammal(Animal):
    def __init__(self, name: str):
        super().__init__(name)
