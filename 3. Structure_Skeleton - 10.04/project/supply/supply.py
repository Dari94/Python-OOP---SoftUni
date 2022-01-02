class Supply:
    def __init__(self, needs_increase):
        self.needs_increase = needs_increase
        if self.needs_increase < 0:
            raise ValueError("Needs increase cannot be less than zero.")

    def apply(self):
        pass

