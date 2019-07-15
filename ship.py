class Ship:
    """
    Manages ships and its lives
    """
    def __init__(self, ship_type=None):
        self._ship_to_live = {"P": 1, "Q": 2}
        self._ship_type = ship_type
        self._live = self._ship_to_live[ship_type] if self.validate_ship_type() else None

    # validates whether ship is valid
    def validate_ship_type(self):
        return True if self._ship_type in list(self._ship_to_live.keys()) else False

    # returns permissible ship names
    def get_permissible_ships(self):
        return list(self._ship_to_live.keys())

    # returns the lives with current ship
    def get_ships_to_lives(self):
        return self._ship_to_live

    # returns the type of ship
    def get_ship_type(self):
        return self._ship_type
