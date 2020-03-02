# Author: Daniel Gwon
# Date: 2/23/2020
# Description:


class XiangqiGame:
    """"""

    def __init__(self):
        """"""

        self._game_state = ''
        self._red_in_check = ''
        self._black_in_check = ''
        self._turn = ''

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


class Board:
    """a Board object that holds pieces of the game"""

    def __init__(self):
        """"""
        self._board = [['' for _ in range(9)] for _ in range(10)]   # 10 rows x 9 cols

        # set up the board
        self._board[0][4] = gen_b = General('black', 'e1')
        self._board[0][3] = adv_b_1 = Advisor('black', 'd1')
        self._board[0][5] = adv_b_2 = Advisor('black', 'f1')
        self._board[0][2] = ele_b_1 = Elephant('black', 'c1')
        self._board[0][6] = ele_b_2 = Elephant('black', 'g1')
        self._board[0][1] = hor_b_1 = Horse('black', 'b1')
        self._board[0][7] = hor_b_2 = Horse('black', 'h1')
        self._board[0][0] = cha_b_1 = Chariot('black', 'a1')
        self._board[0][8] = cha_b_2 = Chariot('black', 'i1')
        self._board[2][1] = can_b_1 = Cannon('black', 'b3')
        self._board[2][7] = can_b_2 = Cannon('black', 'h3')
        self._board[3][0] = sol_b_1 = Soldier('black', 'a4')
        self._board[3][2] = sol_b_2 = Soldier('black', 'c4')
        self._board[3][4] = sol_b_3 = Soldier('black', 'e4')
        self._board[3][6] = sol_b_4 = Soldier('black', 'g4')
        self._board[3][8] = sol_b_5 = Soldier('black', 'i4')
        self._board[9][4] = gen_r = General('red', 'e10')
        self._board[9][3] = adv_r_1 = Advisor('red', 'd10')
        self._board[9][5] = adv_r_2 = Advisor('red', 'f10')
        self._board[9][2] = ele_r_1 = Elephant('red', 'c10')
        self._board[9][6] = ele_r_2 = Elephant('red', 'g10')
        self._board[9][1] = hor_r_1 = Horse('red', 'b10')
        self._board[9][7] = hor_r_2 = Horse('red', 'h10')
        self._board[9][0] = cha_r_1 = Chariot('red', 'a10')
        self._board[9][8] = cha_r_2 = Chariot('red', 'i10')
        self._board[7][1] = can_r_1 = Cannon('red', 'b8')
        self._board[7][7] = can_r_2 = Cannon('red', 'h8')
        self._board[6][0] = sol_r_1 = Soldier('red', 'a7')
        self._board[6][2] = sol_r_2 = Soldier('red', 'c7')
        self._board[6][4] = sol_r_3 = Soldier('red', 'e7')
        self._board[6][6] = sol_r_4 = Soldier('red', 'g7')
        self._board[6][8] = sol_r_5 = Soldier('red', 'i7')

    def update_board(self):
        pass

    def get_board(self):
        pass

    def print_board(self):
        pass


class Piece:
    """"""

    def __init__(self, player, pos):
        """"""
        self._player = player
        self._pos = pos

    def get_player(self):
        return self._player

    def set_pos(self, new_pos):
        self._pos = new_pos

    def get_pos(self):
        return self._pos


class General(Piece):
    """"""

    def __init__(self, player, pos):
        """"""
        self._player = player
        self._pos = pos

    def make_move(self, new_pos):
        """"""
        # TODO check if move is valid
        # if new_pos is valid, self.set_pos(new_pos)
        # else return False


class Advisor(Piece):
    """"""

    def __init__(self, player, pos):
        """"""
        self._player = player
        self._pos = pos

    def make_move(self, new_pos):
        """"""
        # TODO check if move is valid - see General


class Elephant(Piece):
    """"""

    def __init__(self, player, pos):
        """"""
        self._player = player
        self._pos = pos

    def make_move(self, new_pos):
        """"""
        # TODO check if move is valid - see General


class Horse(Piece):
    """"""

    def __init__(self, player, pos):
        """"""
        self._player = player
        self._pos = pos

    def make_move(self, new_pos):
        """"""
        # TODO check if move is valid - see General


class Chariot(Piece):
    """"""

    def __init__(self, player, pos):
        """"""
        self._player = player
        self._pos = pos

    def make_move(self, new_pos):
        """"""
        # TODO check if move is valid - see General


class Cannon(Piece):
    """"""

    def __init__(self, player, pos):
        """"""
        self._player = player
        self._pos = pos

    def make_move(self, new_pos):
        """"""
        # TODO check if move is valid - see General


class Soldier(Piece):
    """"""

    def __init__(self, player, pos):
        """"""
        self._player = player
        self._pos = pos

    def make_move(self, new_pos):
        """"""
        # TODO check if move is valid - see General


# General - one point orthogonal, in castle only
# Advisor - one point diagonal, in castle only
# Elephant - two points diagonal, can't cross river
# Horse - one point orthogonal and one point diagonal, can be blocked
# Chariot - to any point orthogonally
# Cannon - to any point orthogonally, needs screen to capture
# Soldier - one point forward, never back; also horizontal after crossing river

















