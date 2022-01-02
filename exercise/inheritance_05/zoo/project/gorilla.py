from inheritance_05.zoo.project.mammal import Mammal


class Gorilla(Mammal):
    def __init__(self, name: str):
        super().__init__(name)

# inheritance_05.zoo.