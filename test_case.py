import io
import unittest.mock
import unittest
from player import Player
from utils import Utils
from battlearea import BattleArea
from ship import Ship
from play import Play


# class for testing the utils package
class TestUtils(unittest.TestCase):
    # method to test the alpha to number mapping
    def test_get_rev_alpha(self):
        res = Utils.get_rev_alpha()
        self.assertEqual(res["A"], 1)
        self.assertEqual(res["Z"], 26)

    # method to test conversion to uppercase
    def test_upper(self):
        self.assertEqual(Utils.convert_to_upper('a'), 'A')
        self.assertEqual(Utils.convert_to_upper(['a', 'b']), ['A', 'B'])


# class for testing the battlearea package
class TestBattleArea(unittest.TestCase):
    # check blank battlearea creation
    def test_battle_area(self):
        ba = BattleArea(2, 'B')
        exp = [[None, None], [None, None]]
        self.assertEqual(ba.battle_area(), exp)


# class for testing the player package
class TestPlayer(unittest.TestCase):
    # check player name, getter and setter both
    def test_name(self):
        player1 = Player()
        my_name = "Kamal"
        player1.name = my_name
        self.assertEqual(player1.name, "Kamal", "Expected name of the player is " + my_name)
        self.assertNotEqual(player1.name, "Nayan")

    # check setting/getting battlearea for particular player
    def test_battle_area(self):
        player1 = Player()
        ba = BattleArea(2, 'B')
        exp = [[None, None], [None, None]]
        player1.battle_area = ba.battle_area()
        self.assertEqual(player1.battle_area, exp)

    # check the target for the player
    def test_targets(self):
        player1 = Player()
        player1.targets = 'A1 B2 B2 B3'.split()
        exp = ['A1', 'B2', 'B2', 'B3']
        self.assertEqual(player1.targets, exp)

    # check the total lives count of a player
    def test_count(self):
        player1 = Player()
        player1.count = 10
        self.assertEqual(player1.count, 10)
        player1.count -= 2
        self.assertEqual(player1.count, 8)


# class for testing the ship package
class TestShip(unittest.TestCase):
    # validate the type of ship
    def test_validate_ship_type(self):
        s = Ship("P")
        self.assertEqual(s.validate_ship_type(), True)
        s = Ship("Q")
        self.assertEqual(s.validate_ship_type(), True)
        s = Ship("R")
        self.assertEqual(s.validate_ship_type(), False)

    # check the permissible ships
    def test_get_permissible_ships(self):
        s = Ship()
        self.assertEqual(s.get_permissible_ships(), ["P", "Q"])

    # check mapping of ships to lives
    def test_get_ships_to_lives(self):
        s = Ship()
        exp = {'P': 1, 'Q': 2}
        self.assertEqual(s.get_ships_to_lives(), exp)

    # get the current ship type
    def test_get_ship_type(self):
        s = Ship("P")
        self.assertEqual(s.get_ship_type(), "P")
        s = Ship("Q")
        self.assertEqual(s.get_ship_type(), "Q")
        s = Ship("R")
        self.assertEqual(s.get_ship_type(), "R")
        s = Ship()
        self.assertEqual(s.get_ship_type(), None)


# class for testing the play package
class TestPlay(unittest.TestCase):
    # we are filling the battlearea for the player1
    # being just a test case, kept everything hard coded
    def _prefill_sample_ships(self, player1, p=Play()):
        ba = BattleArea(5, "E")
        player1.battle_area = ba.battle_area()
        p.fill_ship(Ship("Q"), 1, 1, 'A1', player1)
        p.fill_ship(Ship("P"), 2, 1, 'D4', player1)

    # get the lives at given location
    def test_get_lives(self):
        player1 = Player()
        p = Play()
        self._prefill_sample_ships(player1, p)
        self.assertEqual(p.get_lives(player1, "A1"), 2)

    # sets the lives at given location
    def test_set_lives(self):
        player1 = Player()
        p = Play()
        self._prefill_sample_ships(player1, p)
        self.assertEqual(p.get_lives(player1, "A1"), 2)
        p.set_lives(player1, "A1", 1)
        self.assertEqual(p.get_lives(player1, "A1"), 1)

    # check the ships at given location
    def test_get_ship_at_location(self):
        p = Play()
        player1 = Player()
        self._prefill_sample_ships(player1, p)
        exp = {'ship_type': 'Q', 'lives': 2}
        self.assertEqual(p.get_ship_at_location(player1, "A1"), exp)
        self.assertEqual(p.get_ship_at_location(player1, "A1")["ship_type"], "Q")
        self.assertEqual(p.get_ship_at_location(player1, "A1")["lives"], 2)

        self.assertEqual(p.get_ship_at_location(player1, "A5"), None)

        exp = {'ship_type': 'P', 'lives': 1}
        self.assertEqual(p.get_ship_at_location(player1, "D5"), exp)
        self.assertEqual(p.get_ship_at_location(player1, "D5")["ship_type"], "P")
        self.assertEqual(p.get_ship_at_location(player1, "D5")["lives"], 1)

    # check the proper filling of ship
    def test_fill_ship(self):
        player1 = Player()
        self._prefill_sample_ships(player1)
        exp = [
            [{'ship_type': 'Q', 'lives': 2}, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, {'ship_type': 'P', 'lives': 1}, {'ship_type': 'P', 'lives': 1}],
            [None, None, None, None, None]
        ]

        self.assertEqual(player1.battle_area, exp)

    # will check the actual output
    # as its written to console, we need to mock it and capture it
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, expected_output, mock_stdout):
        self.play_match()
        self.assertEqual(mock_stdout.getvalue().rstrip("\n"), expected_output)

    # test the start match
    def test_start_match(self):
        exp = [
            "Player-1 fires a missile with target A1 which got miss",
            "Player-2 fires a missile with target A1 which got hit",
            "Player-2 fires a missile with target B2 which got miss",
            "Player-1 fires a missile with target B2 which got hit",
            "Player-1 fires a missile with target B2 which got hit",
            "Player-1 fires a missile with target B3 which got miss",
            "Player-2 fires a missile with target B3 which got miss",
            "Player-1 has no more missiles left to launch",
            "Player-2 fires a missile with target A1 which got hit",
            "Player-2 fires a missile with target D1 which got miss",
            "Player-1 has no more missiles left to launch",
            "Player-2 fires a missile with target E1 which got miss",
            "Player-1 has no more missiles left to launch",
            "Player-2 fires a missile with target D4 which got hit",
            "Player-2 fires a missile with target D4 which got miss",
            "Player-1 has no more missiles left to launch",
            "Player-2 fires a missile with target D5 which got hit",
            "Player-2 won the battle"
        ]
        self.assert_stdout("\n".join(exp))

    # helper function
    def play_match(self):
        player1 = Player("Player-1")
        player2 = Player("Player-2")
        p = Play()
        ba = BattleArea(5, "E")
        player1.battle_area = ba.battle_area()
        player2.battle_area = ba.battle_area()

        s = Ship("Q")
        p.fill_ship(s, 1, 1, "A1", player1)
        p.fill_ship(s, 1, 1, "B2", player2)

        s = Ship("P")
        p.fill_ship(s, 2, 1, "D4", player1)
        p.fill_ship(s, 2, 1, "C3", player2)

        player1.targets = 'A1 B2 B2 B3'.split()
        player2.targets = 'A1 B2 B3 A1 D1 E1 D4 D4 D5 D5'.split()

        p.start_match(player1, player2)


if __name__ == '__main__':
    unittest.main()