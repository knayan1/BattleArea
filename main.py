from player import Player
from battlearea import BattleArea
from ship import Ship
from utils import Utils
from play import Play


if __name__ == '__main__':
    x, y = Utils.convert_to_upper(input().split())
    x = int(x)

    player1 = Player("Player-1")
    player2 = Player("Player-2")
    p = Play()

    # prepare the blank battlearea
    ba = BattleArea(x, y)
    player1.battle_area = ba.battle_area()
    player2.battle_area = ba.battle_area()

    # fills ships to the battlearea
    for i in range(int(input())):
        ship_type, dim1, dim2, p1_cord, p2_cord = Utils.convert_to_upper(input().split())
        s = Ship(ship_type)
        p.fill_ship(s, dim1, dim2, p1_cord, player1)
        p.fill_ship(s, dim1, dim2, p2_cord, player2)

    # set targets for the players
    player1.targets = input().split()
    player2.targets = input().split()

    # let the match begin now...
    p.start_match(player1, player2)
