
class ComputationResult:
    def __init__(self, count, vector) -> None:
        super().__init__()
        self.count = count
        self.vector = vector

    def __str__(self) -> str:
        return "Iterations: " + str(self.count) + ", \n" + "Vector: " + str(self.vector)

