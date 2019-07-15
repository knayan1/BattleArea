class Player:
    """
    Creates a player and provides getters setters to access properties.
    Additional property count is maintained to keep track number of ships available with the player
    """
    def __init__(self, name=None):
        self._name = name
        self._targets = None
        self._count = 0
        self._battle_area = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def battle_area(self):
        return self._battle_area

    @battle_area.setter
    def battle_area(self, value):
        self._battle_area = value

    @property
    def targets(self):
        return self._targets

    @targets.setter
    def targets(self, value):
        self._targets = value

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
