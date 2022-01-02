from inheritance_05.mix_it.project.technology.technology import Technology


class Laptop(Technology):
    def __init__(self, memory: float, memory_taken: float):
        super().__init__(memory, memory_taken)

    def install_software(self, software, software_memory):
        free_capacity = self.memory - self.memory_taken
        result = self.get_capacity(free_capacity,software_memory)
        if isinstance(result,int):
            return f"You don't have enough space for {software}!"
        self.memory_taken += software_memory
        return result

