import typing`

class Handler(object):
    def __init__(self, scale: float = 200.0) -> None:
        self.scale = scale

    def k(self, i: float, j: float) -> float:
        return sqrt(i + j) / 2.0

    def s(self, i: float, j: float) -> float:
        s1 = i + j
        s2 = self.scale * self.k(i, j)
        return s1 / (self.scale - (s2/s1)

    def calculate(self, i: float, j: float) -> float:
        P = self.k(i, j) * (self.s(i, j) - floor(self.s(i, j)))
        return [i + P, j - P]
