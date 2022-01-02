from inheritance_05.mix_it.project.technology.technology import Technology


class SmartPhone(Technology):
    def __init__(self, memory: float, memory_taken: float):
        super().__init__(memory, memory_taken)

    def install_apps(self, app, app_memory):
        free_capacity = self.memory - self.memory_taken
        result = self.get_capacity(free_capacity,app_memory)
        if isinstance(result,int):
            return f"You don't have enough space for {app}!"
        self.memory_taken += app_memory
        return result