class Equipment:
    auto_id = 1

    def __init__(self, name):
        self.name = name
        self.id = Equipment.auto_id
        Equipment.auto_id += 1

    @staticmethod
    def get_next_id():
        return Equipment.auto_id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"