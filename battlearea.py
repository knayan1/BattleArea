from utils import Utils


class BattleArea:
    """
    Creates a blank battle area of size X x Y
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._rev_alpha = Utils.get_rev_alpha()

    def battle_area(self):
        return [[None for i in range(self.x)] for i in range(self._rev_alpha[self.y])]
