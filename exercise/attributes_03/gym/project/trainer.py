class Trainer:
    auto_id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Trainer.auto_id
        Trainer.auto_id += 1

    @staticmethod
    def get_next_id():
        return Trainer.auto_id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"