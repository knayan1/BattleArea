from utils import Utils


class Play:
    """
    Actual class to play the match
    """
    def __init__(self):
        self._rev_alpha = Utils.get_rev_alpha()

    # Returns True if hits target ship otherwise False
    def _is_hit(self, target_player, location):
        lives = self.get_lives(target_player, location)
        if lives:
            self.set_lives(target_player, location, lives - 1)
            target_player.count -= 1
            return True
        return False

    # Its time to attack on victim, returns message to be outputted
    def _target_shot(self, attacker, victim):
        msg = ""
        if victim.count > 0:
            if attacker.targets:
                target = attacker.targets.pop(0)
                msg = ("%s fires a missile with target %s which got " % (attacker.name, target))
                if not self._is_hit(victim, target):
                    msg += "miss"
                else:
                    msg += "hit"
                    msg = msg + "\n" + self._target_shot(attacker, victim)
            else:
                msg = ("%s has no more missiles left to launch" % attacker.name)
        return msg

    # lets begin the fun
    # starts the match, and iterates until its over
    def start_match(self, p1, p2):
        match_over = False
        while not match_over:
            print(self._target_shot(p1, p2).strip("\n"))
            if p2.count == 0:
                print("%s won the battle" % p1.name)
                match_over = True
                break

            print(self._target_shot(p2, p1).strip("\n"))
            if p1.count == 0:
                print("%s won the battle" % p2.name)
                match_over = True
                break

    # Fills ships to the given location in battle area for given player
    def fill_ship(self, s, dim1, dim2, p1_cord, player):
        ship_type = s.get_ship_type()
        if not s.validate_ship_type():
            exit("Invalid ship type, allowed ones are: %s. Quitting..." % s.get_permissible_ships())

        lives = s.get_ships_to_lives()
        for i in range(self._rev_alpha[p1_cord[0]] - 1, self._rev_alpha[p1_cord[0]] - 1 + int(dim2)):
            for j in range(int(p1_cord[1]) - 1, int(p1_cord[1]) + int(dim1) - 1):
                try:
                    player.battle_area[i][j] = {"ship_type": ship_type, "lives": lives[ship_type]}
                    player.count += lives[ship_type]
                except IndexError as e:
                    exit("Ship dimension is more than the area allotted. Quitting...")

    # Returns remaining lives of ships at given location for given player
    def get_lives(self, target_player, location):
        ship_at_loc = self.get_ship_at_location(target_player, location)
        if ship_at_loc is not None and ship_at_loc["lives"]:
            return ship_at_loc["lives"]
        return 0

    # Updates lives of ships at given location for given player
    def set_lives(self, target_player, location, value):
        ship_at_loc = self.get_ship_at_location(target_player, location)
        if ship_at_loc is not None and ship_at_loc["lives"]:
            ship_at_loc["lives"] = value

    # Returns tha ship at given location
    def get_ship_at_location(self, target_player, location):
        return target_player.battle_area[int(self._rev_alpha[location[0]]) - 1][int(location[1]) - 1]