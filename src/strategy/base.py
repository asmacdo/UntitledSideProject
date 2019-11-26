class Strategy:

    def __init__(self, state, drawer):
        self.S = state
        self.D = drawer

    def get_to_target(self):
        raise NotImplementedError()

    def calculate_target(self):
        pass
