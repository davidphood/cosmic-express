
class Locomotive:
    def __init__(self, numCarriages):
        self.carriages = [Carriage() for i in range(numCarriages)]