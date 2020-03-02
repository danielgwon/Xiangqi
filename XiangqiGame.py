# Author: Daniel Gwon
# Date: 3/1/2020
# Description:


class XiangqiGame:
    """"""

    def __init__(self):
        """"""
        self._game_state = 'UNFINISHED'         # 'UNFINISHED', 'RED_WON', 'BLACK_WON'
        self._red_in_check = ''
        self._black_in_check = ''
        self._turn = 'red'
        self._board = Board()

    def get_game_state(self):
        """"""
        return self._game_state

    def is_in_check(self, player):
        """

        :param player: 'red' or 'black'
        :return: True or False
        """

    def update_turn(self):
        """"""
        if self._turn == 'red':
            self._turn = 'black'
        else:
            self._turn = 'red'

    def make_move(self, start, to):
        """
        Moves a piece from a start position to a to position
        :param start: str
        :param to: str
        :return: bool or n/a
        """

        # convert start to board indices
        row_s = int(start[1])
        col_s = int(start[0])
        row_t = int(to[1])
        col_t = int(to[0])

        # game over
        if self.get_game_state == 'RED_WON' or self.get_game_state == 'BLACK_WON':
            return False
        elif self._board.get_piece(row_s, col_s) == '':     # no piece at pos
            return False
        # wrong player's piece
        elif self._board.get_piece(row_s, col_s).get_player() != self._turn:
            return False
        elif row_t < 0 or row_t > 9:                        # row pos out of bounds
            return False
        elif col_t < 0 or col_t > 8:                        # col pos out of bounds
            return False

        # make the move
        result = self._board.make_move(row_s, col_s, row_t, col_t)

        # check if piece able to make move
        if not result:
            return False

        # update player's turn
        self.update_turn()

        # update game state
        # TODO update the game state after making a move


class Board:
    """a Board object that holds pieces of the game"""

    def __init__(self):
        """"""
        self._board = [['' for _ in range(9)] for _ in range(10)]   # 10 rows x 9 cols

        # set up the board
        self._board[0][4] = gen_b = General('black', 0, 4)
        self._board[0][3] = adv_b_1 = Advisor('black', 0, 3)
        self._board[0][5] = adv_b_2 = Advisor('black', 0, 5)
        self._board[0][2] = ele_b_1 = Elephant('black', 0, 2)
        self._board[0][6] = ele_b_2 = Elephant('black', 0, 6)
        self._board[0][1] = hor_b_1 = Horse('black', 0, 1)
        self._board[0][7] = hor_b_2 = Horse('black', 0, 7)
        self._board[0][0] = cha_b_1 = Chariot('black', 0, 0)
        self._board[0][8] = cha_b_2 = Chariot('black', 0, 8)
        self._board[2][1] = can_b_1 = Cannon('black', 2, 1)
        self._board[2][7] = can_b_2 = Cannon('black', 2, 7)
        self._board[3][0] = sol_b_1 = Soldier('black', 3, 0)
        self._board[3][2] = sol_b_2 = Soldier('black', 3, 2)
        self._board[3][4] = sol_b_3 = Soldier('black', 3, 4)
        self._board[3][6] = sol_b_4 = Soldier('black', 3, 6)
        self._board[3][8] = sol_b_5 = Soldier('black', 3, 8)
        self._board[9][4] = gen_r = General('red', 9, 4)
        self._board[9][3] = adv_r_1 = Advisor('red', 9, 3)
        self._board[9][5] = adv_r_2 = Advisor('red', 9, 5)
        self._board[9][2] = ele_r_1 = Elephant('red', 9, 2)
        self._board[9][6] = ele_r_2 = Elephant('red', 9, 6)
        self._board[9][1] = hor_r_1 = Horse('red', 9, 1)
        self._board[9][7] = hor_r_2 = Horse('red', 9, 7)
        self._board[9][0] = cha_r_1 = Chariot('red', 9, 0)
        self._board[9][8] = cha_r_2 = Chariot('red', 9, 8)
        self._board[7][1] = can_r_1 = Cannon('red', 7, 1)
        self._board[7][7] = can_r_2 = Cannon('red', 7, 7)
        self._board[6][0] = sol_r_1 = Soldier('red', 6, 0)
        self._board[6][2] = sol_r_2 = Soldier('red', 6, 2)
        self._board[6][4] = sol_r_3 = Soldier('red', 6, 4)
        self._board[6][6] = sol_r_4 = Soldier('red', 6, 6)
        self._board[6][8] = sol_r_5 = Soldier('red', 6, 8)

    def make_move(self, row_s, col_s, row_t, col_t):
        """"""

        result = self._board[row_s][col_s].make_move(row_t, col_t)

        if not result:
            return False

    def get_piece(self, r, c):
        """"""
        return self._board[r][c]

    def get_board(self):
        pass

    def print_board(self):
        """"""
        for i in range(len(self._board)-1, -1, -1):
            print(self._board[i])


class Piece:
    """"""

    def __init__(self, player, r, c):
        """"""
        self._player = player
        self._row = r
        self._col = c

    def get_player(self):
        return self._player

    def get_row(self):
        return self._row

    def get_col(self):
        return self._col


class General(Piece):
    """"""

    def __init__(self, player, r, c):
        """"""
        super().__init__(player, r, c)

    def make_move(self, new_pos):
        """"""
        # TODO check if move is valid
        # if new_pos is valid, self.set_pos(new_pos)
        # else return False


class Advisor(Piece):
    """"""

    def __init__(self, player, r, c):
        """"""
        super().__init__(player, r, c)

    def make_move(self, new_pos):
        """"""
        # TODO check if move is valid - see General


class Elephant(Piece):
    """"""

    def __init__(self, player, r, c):
        """"""
        super().__init__(player, r, c)

    def make_move(self, new_pos):
        """"""
        # TODO check if move is valid - see General


class Horse(Piece):
    """"""

    def __init__(self, player, r, c):
        """"""
        super().__init__(player, r, c)

    def make_move(self, new_pos):
        """"""
        # TODO check if move is valid - see General


class Chariot(Piece):
    """"""

    def __init__(self, player, r, c):
        """"""
        super().__init__(player, r, c)

    def make_move(self, r, c):
        """"""
        if r == self._row and c > self._col:        # move right
            for (i in range(self._col, c)):
                if
        elif r == self._row and c < self._col:      # move left

        elif r < self._row and c == self._col:      # move forward
            for (i in range())
        elif r > self._row and c == self._col:      # move backward



class Cannon(Piece):
    """"""

    def __init__(self, player, r, c):
        """"""
        super().__init__(player, r, c)

    def make_move(self, new_pos):
        """"""
        # TODO check if move is valid - see General


class Soldier(Piece):
    """"""

    def __init__(self, player, r, c):
        """"""
        super().__init__(player, r, c)

    def make_move(self, r, c):
        """"""
        if self._player == 'black':
            if r > 4:                   # before crossing river
                if r == self._row - 1:  # vertical move
                    self._row = r
                else:
                    return False
            else:                       # after crossing river
                if r == self._row - 1:
                    self._row = r
                elif c == self._col + 1 or c == self._col - 1:      # horizontal moves
                    self._col = c
                else:
                    return False
        else:                           # self._player == 'red'
            if r < 5:                   # before crossing river
                if r == self._row + 1:  # vertical move
                    self._row = r
                else:
                    return False
            else:                       # after crossing river
                if r == self._row + 1:
                    self._row = r
                elif c == self._col + 1 or c == self._col - 1:      # horizontal moves
                    self._col = c
                else:
                    return False
