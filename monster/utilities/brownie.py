import typing

class Handler(object):
    def __init__(self, scale_factor: int = 200) -> None:
        self.scale_factor = scale_factor

    def __calculate(self, a: float, b: float) -> float:
        k = sqrt(a + b) / 2
        factor = (a + b)/(200 * k/(a + b))
        return ciel(factor) - factor

    def game(winner: float, loser: float) -> typing.Tuple[float]:
        return (winner + self.__calculate(winner, loser), loser - self.__calculate(winner, loser))

    def set_scale_factor(self, scale_factor: int) -> None:
        self.scale_factor = scale_factor

