# Author: Daniel Gwon
# Date: 2/23/2020
# Description:


class XiangqiGame:
    """"""

    def __init__(self):
        """"""


    def get_game_state(self):
        """"""

        # 'UNFINISHED', 'RED_WON', 'BLACK_WON'


    def is_in_check(self, player):
        """

        :param player: 'red' or 'black'
        :return: True or False
        """


    def make_move(self, move_from, move_to):
        """

        :param move_from: string
        :param move_to: string
        :return: True or False
        """


# General - one point orthogonal, in castle only
# Advisor - one point diagonal, in castle only
# Elephant - two points diagonal, can't cross river
# Horse - one point orthogonal and one point diagonal, can be blocked
# Chariot - to any point orthogonally
# Cannon - to any point orthogonally, needs screen to capture
# Soldier - one point forward, never back; also horizontal after crossing river




# starting board: 1-4 (red)   7-10 (black)
#               x   x   x
# [ c , h , e , a , g , a , e , h , c ]   10  9   x     b
# [   ,   ,   ,   ,   ,   ,   ,   ,   ]   9   8   x     l
# [   , n ,   ,   ,   ,   ,   , n ,   ]   8   7   x     c
# [ s ,   , s ,   , s ,   , s ,   , s ]   7   6         k
# [   ,   ,   ,   ,   ,   ,   ,   ,   ]   6   5
#-----------------RIVER----------------
# [   ,   ,   ,   ,   ,   ,   ,   ,   ]   5   4
# [ s ,   , s ,   , s ,   , s ,   , s ]   4   3         r
# [   , n ,   ,   ,   ,   ,   , n ,   ]   3   2   x     e
# [   ,   ,   ,   ,   ,   ,   ,   ,   ]   2   1   x     d
# [ c , h , e , a , g , a , e , h , c ]   1   0   x     |
#   0   1   2   3   4   5   6   7   8
#   a   b   c   d   e   f   g   h   i      list pos
#               x   x   x

















