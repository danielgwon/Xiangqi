# Author: Daniel Gwon
# Date: 3/4/2020
# Description: implements classes to model a game of Xiangqi (Chinese Chess)


class XiangqiGame:
    """
    Creates a game of Xiangqi
    """

    def __init__(self):
        """
        init the game
        """
        self._game_state = 'UNFINISHED'                 # 'UNFINISHED', 'RED_WON', 'BLACK_WON'
        self._turn = 'red'                              # red starts
        self._board = Board()
        self._r_gen = self._board.get_piece(0, 4)       # red General
        self._b_gen = self._board.get_piece(9, 4)       # black General
        self._r_pieces = self._board.get_r_pieces()     # red's pieces
        self._b_pieces = self._board.get_b_pieces()     # black's pieces

    def make_move(self, start, to):
        """
        moves a piece from start position to to position
        :param start: str
        :param to: str
        :return: bool
        """

        # convert start and to to board indices
        pos_s = self._pos_to_int(start)
        pos_t = self._pos_to_int(to)
        row_s = pos_s[0]
        col_s = pos_s[1]
        row_t = pos_t[0]
        col_t = pos_t[1]

        # is game over?
        if self.get_game_state() != 'UNFINISHED':
            return False

        # piece at start?
        if not self._has_a_piece(row_s, col_s):
            return False

        # right player's piece?
        if not self._is_player_piece(row_s, col_s):
            return False

        # valid move?
        if not self._board.get_piece(row_s, col_s).is_valid(row_t, col_t):
            return False

        # # piece captured?
        # if self._board.get_piece(row_s, col_s).captured(row_t, col_t):
        #     self._update_list(self._board.get_piece(row_t, col_t).get_player(), self._board.get_piece(row_t, col_t))

        # record the move
        self._board.set_last_move([row_s, col_s, row_t, col_t])
        self._board.set_last_piece(self._board.get_piece(row_t, col_t))

        # update Piece
        self._board.get_piece(row_s, col_s).update_piece(row_t, col_t)

        # update Board
        self._board.update_board(row_t, col_t, self._board.get_piece(row_s, col_s))       # end
        self._board.update_board(row_s, col_s, '_')                                       # start

        # update player's active pieces
        if self._board.get_last_piece() != '_':
            if self._board.get_last_piece().get_player() == 'red':
                self._r_pieces.remove(self._board.get_last_piece())
            else:
                self._b_pieces.remove(self._board.get_last_piece())

        # flying general?
        if self._board.get_board()[row_t][col_t] == self._r_gen or \
                self._board.get_board()[row_t][col_t] == self._b_gen:
            if self._ax_from_gen(row_t, col_t) and not self._intervening_gen(row_t, col_t):
                self._board.undo()
                return False

        # move you in check?
        if self.is_in_check(self._turn):
            self._board.undo()
            return False

        # update player's turn
        self._update_turn()

        # update game state
        # if self._checkmate(self._turn):
        #     self._game_state = ''

        # TODO implement stalemate

        return True

    def get_game_state(self):
        """
        gives the current game state
        :return: str ('UNFINISHED', 'RED_WON', or 'BLACK_WON')
        """
        return self._game_state

    def is_in_check(self, player):
        """
        tells if given player is in check
        :param player: str ('red' or 'black')
        :return: bool
        """
        if player == 'red':
            for piece in self._b_pieces:
                if piece.is_valid(self._r_gen.get_row(), self._r_gen.get_col()):
                    return True             # black can capture red General
        else:
            for piece in self._r_pieces:
                if piece.is_valid(self._b_gen.get_row(), self._b_gen.get_col()):
                    return True             # red can capture black General
        return False

    # def _update_list(self, player, piece):
    #     """
    #     removes a captured Piece from the appropriate player
    #     :param player: str ('red' or 'black')
    #     :param piece: Piece
    #     :return: n/a
    #     """
    #     if player == 'red':
    #         self._l_red.remove(piece)
    #     else:
    #         self._l_black.remove(piece)

    # def _checkmate(self, player):
    #     """
    #     True if player is checkmated, False otherwise
    #     :param player: str ('red' or 'black')
    #     :return: bool
    #     """
    #     if player == 'red':
    #         for piece in self._l_red:
    #             for i in range(0, len(self._board.get_board())):
    #                 for j in range(0, len(self._board.get_board()[i])):
    #                     if piece.is_valid(i, j):
    #                         piece.make_move(i, j)
    #                         if self.is_in_check(player):   # if the piece makes this move, player still in check?
    #                             self._board.undo()
    #                             continue
    #                         return False
    #     else:
    #         for piece in self._l_black:
    #             for i in range(0, len(self._board.get_board())):
    #                 for j in range(0, len(self._board.get_board()[i])):
    #                     if piece.is_valid(i, j):
    #                         piece.make_move(i, j)
    #                         if self.is_in_check(player):   # if the piece makes this move, player still in check?
    #                             self._board.undo()
    #                             continue
    #                         return False
    #     return True

    def _ax_from_gen(self, r, c):
        """
        True if new pos across from General, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """
        # red General
        if r <= 2:
            if self._board.get_board()[9][c] is self._b_gen or \
                    self._board.get_board()[8][c] is self._b_gen or \
                    self._board.get_board()[7][c] is self._b_gen:
                return True
        # black General
        else:
            if self._board.get_board()[0][c] is self._r_gen or \
                    self._board.get_board()[1][c] is self._r_gen or \
                    self._board.get_board()[2][c] is self._r_gen:
                return True
        return False

    def _intervening_gen(self, r, c):
        """
        True if there is an intervening piece between generals, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """

        # red general
        if self._board.get_piece(r, c).get_player() == 'red':
            for i in range(r+1, self._b_gen.get_row()):
                if self._board.get_board()[i][c] != '_':
                    return True
        # black general
        else:
            for i in range(r-1, self._r_gen.get_row(), -1):
                if self._board.get_board()[i][c] != '_':
                    return True
        return False

    def _update_turn(self):
        """
        updates whose turn it is
        :return: n/a
        """
        if self._turn == 'red':
            self._turn = 'black'
        else:
            self._turn = 'red'

    def _has_a_piece(self, r, c):
        """
        True if piece at position, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """
        if self._board.get_piece(r, c) == '_':
            return False
        return True

    def _pos_to_int(self, pos):
        """
        converts pos in str to list indices
        :param start str
        :param to: str
        :return: [int row_s, int col_s, int row_t, int col_t]
        """

        col_to_int = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
                      'e': 4, 'f': 5, 'g': 6, 'h': 7,
                      'i': 8}

        pos_int = (int(pos[1:])-1, col_to_int[pos[0]])
        return pos_int

    def _is_player_piece(self, r, c):
        """
        True if right piece, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """
        if self._board.get_piece(r, c).get_player() != self._turn:
            return False
        return True


class Board:
    """
    Creates a Xiangqi board
    """

    def __init__(self):
        """
        init the board
        """

        # initialize board
        self._board = [['_' for _ in range(9)] for _ in range(10)]   # 10 rows x 9 cols

        # set up board
        self._board[0][4] = General('red', 0, 4, self._board, 'g')
        self._board[0][3] = Advisor('red', 0, 3, self._board, 'a')
        self._board[0][5] = Advisor('red', 0, 5, self._board, 'a')
        self._board[0][2] = Elephant('red', 0, 2, self._board, 'e')
        self._board[0][6] = Elephant('red', 0, 6, self._board, 'e')
        self._board[0][1] = Horse('red', 0, 1, self._board, 'h')
        self._board[0][7] = Horse('red', 0, 7, self._board, 'h')
        self._board[0][0] = Chariot('red', 0, 0, self._board, 'c')
        self._board[0][8] = Chariot('red', 0, 8, self._board, 'c')
        self._board[2][1] = Cannon('red', 2, 1, self._board, 'n')
        self._board[2][7] = Cannon('red', 2, 7, self._board, 'n')
        self._board[3][0] = Soldier('red', 3, 0, self._board, 's')
        self._board[3][2] = Soldier('red', 3, 2, self._board, 's')
        self._board[3][4] = Soldier('red', 3, 4, self._board, 's')
        self._board[3][6] = Soldier('red', 3, 6, self._board, 's')
        self._board[3][8] = Soldier('red', 3, 8, self._board, 's')
        self._board[9][4] = General('black', 9, 4, self._board, 'g')
        self._board[9][3] = Advisor('black', 9, 3, self._board, 'a')
        self._board[9][5] = Advisor('black', 9, 5, self._board, 'a')
        self._board[9][2] = Elephant('black', 9, 2, self._board, 'e')
        self._board[9][6] = Elephant('black', 9, 6, self._board, 'e')
        self._board[9][1] = Horse('black', 9, 1, self._board, 'h')
        self._board[9][7] = Horse('black', 9, 7, self._board, 'h')
        self._board[9][0] = Chariot('black', 9, 0, self._board, 'c')
        self._board[9][8] = Chariot('black', 9, 8, self._board, 'c')
        self._board[7][1] = Cannon('black', 7, 1, self._board, 'n')
        self._board[7][7] = Cannon('black', 7, 7, self._board, 'n')
        self._board[6][0] = Soldier('black', 6, 0, self._board, 's')
        self._board[6][2] = Soldier('black', 6, 2, self._board, 's')
        self._board[6][4] = Soldier('black', 6, 4, self._board, 's')
        self._board[6][6] = Soldier('black', 6, 6, self._board, 's')
        self._board[6][8] = Soldier('black', 6, 8, self._board, 's')

        # init list for player Pieces
        self._r_pieces = []
        self._b_pieces = []

        # populate lists
        for i in range(0, len(self._board)):
            for j in range(0, len(self._board[i])):
                if self._board[i][j] != '_':
                    if self._board[i][j].get_player() == 'red':
                        self._r_pieces.append(self._board[i][j])
                    else:
                        self._b_pieces.append(self._board[i][j])

        # init data members for undo()
        self._last_move = []            # [row_s, col_s, row_t, col_t]
        self._last_piece = '_'

    def get_r_pieces(self):
        """
        gives list of red pieces
        :return: []
        """
        return self._r_pieces

    def get_b_pieces(self):
        """
        gives list of red pieces
        :return: []
        """
        return self._b_pieces

    def remove_r_pieces(self, piece):
        """
        removes piece from list of red's active pieces
        :param piece: Piece
        :return: n/a
        """
        self._r_pieces.remove(piece)

    def remove_b_pieces(self, piece):
        """
        removes piece from list of black's active pieces
        :param piece: Piece
        :return: n/a
        """
        self._b_pieces.remove(piece)

    def get_piece(self, r, c):
        """
        gives the piece at the specified row and col
        :param r: int
        :param c: int
        :return: '_' or Piece
        """
        return self._board[r][c]

    def get_board(self):
        """
        gives the board
        :return: [[]]
        """
        return self._board

    def update_board(self, r, c, item):
        """
        updates the board with str at the given coordinates
        :param r: int
        :param c: int
        :param item: str or Piece
        :return: n/a
        """
        self._board[r][c] = item

    def set_last_move(self, last_list):
        """
        updates self._last_move
        :param last_list: [int row_s, int col_s, int row_t, int col_t]
        :return: n/a
        """
        self._last_move = last_list

    def get_last_piece(self):
        """
        gives the last piece removed from the board
        :return: Piece or str
        """
        return self._last_piece

    def set_last_piece(self, item):
        """
        updates self._last_piece
        :param item: Piece or '_'
        :return: n/A
        """
        self._last_piece = item

    def undo(self):
        """
        undo the last move
        :return: n/a
        """

        # return Piece to starting position and reset its row and col
        self._board[self._last_move[0]][self._last_move[1]] = self._board[self._last_move[2]][self._last_move[3]]
        self._board[self._last_move[2]][self._last_move[3]].update_piece(self._last_move[0], self._last_move[1])

        # return captured Piece or empty position
        self._board[self._last_move[2]][self._last_move[3]] = self._last_piece

        # return captured piece to list of pieces
        if self._last_piece != '_':
            if self._last_piece.get_player() == 'red':
                self._r_pieces.append(self._last_piece)
            else:
                self._b_pieces.append(self._last_piece)

    def print_board(self):
        """
        prints the board
        :return: n/a
        """

        for i in range(len(self._board)-1, -1, -1):
            for j in range(0, len(self._board[i])):
                if self._board[i][j] != '_':
                    if j == 8:
                        print(self._board[i][j].get_name())
                        continue
                    print(self._board[i][j].get_name(), end=" ")
                    continue

                if j == 8:
                    print(self._board[i][j])
                    continue
                print(self._board[i][j], end=" ")


class Piece:
    """
    Creates a Xiangqi piece on the board
    """

    def __init__(self, player, r, c, board, name):
        """
        init the Piece
        :param player: str ('red' or 'black')
        :param r: int
        :param c: int
        :param board: [[]]
        """
        self._player = player
        self._row = r
        self._col = c
        self._board = board
        self._name = name

    def get_player(self):
        """
        gives the owner of the Piece
        :return: str ('red' or 'black')
        """
        return self._player

    def get_row(self):
        """
        gives the row of the Piece
        :return: int
        """
        return self._row

    def get_col(self):
        """
        gives the col of the Piece
        :return: int
        """
        return self._col

    def get_name(self):
        """
        gives the name of the Piece
        :return: str
        """
        return self._name

    def update_piece(self, r, c):
        """
        updates the position of the Piece
        :param r: int
        :param c: int
        :return: bool
        """
        self._row = r
        self._col = c

    def is_orthogonal(self, r, c):
        """
        True if move is orthogonal, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """
        return self.get_row() == r or self.get_col() == c

    def is_diagonal(self, r, c):
        """
        True if move is diagonal, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """
        return abs(self._row - r) == abs(self._col - c)

    def is_vertical(self, c):
        """
        True if move is vertical, False if horizontal
        :param c: int
        :return: bool
        """
        return self._col == c

    def vertical_way(self, r):
        """
        True if move up, False if move down
        :param r: int
        :return: bool
        """
        return r > self._row

    def horizontal_way(self, c):
        """
        True if move right, False if move left
        :param c: int
        :return: bool
        """
        return c > self._col

    def one_point(self, r, c):
        """
        True if move is one point from current position, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """
        return abs(self._row - r) <= 1 and abs(self._col - c) <= 1

    def in_castle(self, r, c):
        """
        True if move within castle, False otherwise.
        Used by General and Advisor only
        :param r: int
        :param c: int
        :return: bool
        """

        # all castles:
        #   3 <= c <= 5
        # red castle:
        #   r <= 2
        # black castle:
        #   r >= 7

        if c < 3 or c > 5:
            return False
        else:               # col within bounds
            if self.get_player() == 'red':
                return r <= 2
            else:           # black
                return r >= 7

    def river(self, r):
        """
        True if across the river, False otherwise
        Elephant and Soldier only
        :param r: int
        :return: bool
        """

        # red
        if self._player == 'red':
            return r > 4
        else:       # black
            return r < 5

    def blocked(self, r, c):
        """
        True if another piece in given position, False otherwise
        Used to determine if Piece in path from start pos to desired
        pos
        :param r: int
        :param c: int
        :return: bool
        """
        return self._board[r][c] != '_'

    def intervening(self, r, c):
        """
        True if Piece in way, False otherwise
        Chariot and Cannon only
        :param r: int
        :param c: int
        :return: int
        """
        result = 0

        if self.is_vertical(c):            # vertical move
            if self.vertical_way(r):       # up
                for i in range(self._row+1, r):
                    if self.blocked(i, c):
                        result += 1
            else:                           # down
                for i in range(self._row-1, r, -1):
                    if self.blocked(i, c):
                        result += 1
        else:                               # horizontal move
            if self.horizontal_way(c):     # right
                for i in range(self._col+1, c):
                    if self.blocked(r, i):
                        result += 1
            else:                           # left
                for i in range(self._col-1, c, -1):
                    if self.blocked(r, i):
                        result += 1

        return result

    def captured(self, r, c):
        """
        True if opponent's piece is captured, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """
        return self._board[r][c] != '_'

    def is_valid(self, r, c):
        """

        :param r:
        :param c:
        :return:
        """

        # own piece in to position?
        if self._board[r][c] == '_':
            return False
        else:
            return self._board[r][c].get_player() == self.get_player()


class General(Piece):
    """
    Creates a General Piece
    """

    def __init__(self, player, r, c, board, name):
        """
        init the General
        :param player: str ('red' or 'black')
        :param r: int
        :param c: int
        :param board: Board
        """

        # inherits from Piece
        super().__init__(player, r, c, board, name)

    def is_valid(self, r, c):
        """
        True if move is valid, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """
        # one point orthogonal?
        # in castle?
        # across from general?

        if super().is_valid(r, c):
            return False

        # one point orthogonal?
        if not self._one_orthogonal(r, c):
            return False

        # within castle?
        if not self.in_castle(r, c):
            return False

        return True

    def move(self, r, c):
        """
        moves the General to the given position
        :param r: int
        :param c: int
        :return: bool
        """
        result = self.is_valid(r, c)

        if result:
            self.update_piece(r, c)     # update self
            return True
        return False

    def _one_orthogonal(self, r, c):
        """
        True if move is one space orthogonally, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """
        return self.is_orthogonal(r, c) and self.one_point(r, c)


class Advisor(Piece):
    """
    Creates an Advisor Piece
    """

    def __init__(self, player, r, c, board, name):
        """
        init the Advisor
        :param player: str ('red' or 'black')
        :param r: int
        :param c: int
        :param board: Board
        """

        # inherits from Piece
        super().__init__(player, r, c, board, name)

    def _one_diagonal(self, r, c):
        """
        True if one position diagonally, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """
        return self.is_diagonal(r, c) and self.one_point(r, c)

    def is_valid(self, r, c):
        """
        True if move is valid, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """

        # 1. single space diagonal
        # 2. castle only

        if super().is_valid(r, c):
            return False

        # single space diagonally?
        if not self._one_diagonal(r, c):
            return False

        # in castle?
        if not self.in_castle(r, c):
            return False

        return True

    def move(self, r, c):
        """
        moves the Advisor to the given position
        :param r: int
        :param c: int
        :return: bool
        """
        result = self.is_valid(r, c)

        if result:
            self.update_piece(r, c)     # update self
            return True
        return False


class Elephant(Piece):
    """
    Creates an Elephant Piece
    """

    def __init__(self, player, r, c, board, name):
        """
        init the Elephant
        :param player: str ('red' or 'black')
        :param r: int
        :param c: int
        :param board: Board
        """

        # inherit from Piece
        super().__init__(player, r, c, board, name)

    def _two_diagonal(self, r, c):
        """
        True if two points diagonally, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """
        return self.is_diagonal(r, c) and abs(self._row - r) == 2

    def is_valid(self, r, c):
        """
        True if move is valid, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """

        if super().is_valid(r, c):
            return False

        # across river?
        if self.river(r):
            return False        # Elephant can't cross river

        # two points diagonal?
        if not self._two_diagonal(r, c):
            return False

        # intervening piece?
        if

        return True

    def move(self, r, c):
        """
        moves the Elephant to the given position
        :param r: int
        :param c: int
        :return: bool
        """
        result = self.is_valid(r, c)

        if result:
            self.update_piece(r, c)     # update self
            return True
        return False


class Horse(Piece):
    """
    Creates a Horse Piece
    """

    def __init__(self, player, r, c, board, name):
        """
        init the Horse
        :param player: str ('red' or 'black')
        :param r: int
        :param c: int
        :param board: Board
        """

        # inherit from Piece
        super().__init__(player, r, c, board, name)
        self._valid_moves = [[self._row+2, self._col-1], [self._row+2, self._col+1],
                             [self._row-2, self._col-1], [self._row+2, self._col+1],
                             [self._row+1, self._col+2], [self._row-1, self._col+2],
                             [self._row+1, self._col-2], [self._row-1, self._col-2]]

    def _is_vertical(self, r):
        """
        True if move is two points vertically, False otherwise
        :param r: int
        :return: bool
        """
        return abs(self._row - r) == 2

    def _blocked(self, r, c):
        """
        True if Horse blocked for given move, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """
        # vertical move
        if self._is_vertical(r):
            if r > self._row:
                return self.blocked(r-1, self._col)    # up position
            else:
                return self.blocked(r+1, self._col)    # down position
        else:
            if c > self._col:
                return self.blocked(self._row, c-1)    # right position
            else:
                return self.blocked(self._row, c+1)    # left position

    def is_valid(self, r, c):
        """
        True if move is valid, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """

        # 1. one point orthogonally, one point diagonally
        # 2. can be blocked

        if super().is_valid(r, c):
            return False

        # is the move valid?
        if [r, c] not in self._valid_moves:
            return False

        # move blocked?
        if self._blocked(r, c):
            return False

        return True

    def move(self, r, c):
        """
        moves the Horse to the given position
        :param r: int
        :param c: int
        :return: bool
        """
        result = self.is_valid(r, c)

        if result:
            self.update_piece(r, c)     # update self
            return True
        return False


class Chariot(Piece):
    """
    Creates a Chariot Piece
    """

    def __init__(self, player, r, c, board, name):
        """
        init the Chariot
        :param player: str ('red' or 'black')
        :param r: int
        :param c: int
        :param board: Board
        """

        # inherit from Piece
        super().__init__(player, r, c, board, name)

    def is_valid(self, r, c):
        """
        True if move is valid, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """

        # 1. any point orthogonally

        if super().is_valid(r, c):
            return False

        # orthogonal?
        if not self.is_orthogonal(r, c):
            return False

        # piece in way?
        if self.intervening(r, c):
            return False

        return True

    def move(self, r, c):
        """
        moves the Chariot to the given position
        :param r: int
        :param c: int
        :return: bool
        """
        result = self.is_valid(r, c)

        if result:
            self.update_piece(r, c)     # update self
            return True
        return False


class Cannon(Piece):
    """
    Creates a Cannon Piece
    """

    def __init__(self, player, r, c, board, name):
        """
        init the Cannon
        :param player: str ('red' or 'black')
        :param r: int
        :param c: int
        :param board: Board
        """

        # inherit from Piece
        super().__init__(player, r, c, board, name)

    def _opponent_piece(self, r, c):
        """
        True if the opponent's piece resides in the position, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """
        return self._player != self._board[r][c].get_player()

    def is_valid(self, r, c):
        """
        True if move is valid, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """

        # 1. any point orthogonally
        # 2. needs screen to capture (screen can be opponent's Piece)

        if super().is_valid(r, c):
            return False

        # orthogonal?
        if not self.is_orthogonal(r, c):
            return False

        # move to capture?
        if self._opponent_piece(r, c):
            # screen in place?
            if self.intervening(r, c) > 1:
                return False

        # piece in way?
        if self.intervening(r, c):
            return False

        return True

    def move(self, r, c):
        """
        moves the Cannon to the given position
        :param r: int
        :param c: int
        :return: bool
        """
        result = self.is_valid(r, c)

        if result:
            self.update_piece(r, c)     # update self
            return True
        return False


class Soldier(Piece):
    """
    Creates a Soldier Piece
    """

    def __init__(self, player, r, c, board, name):
        """
        init the Soldier
        :param player: str ('red' or 'black')
        :param r: int
        :param c: int
        :param board: Board
        """

        # inherit from Piece
        super().__init__(player, r, c, board, name)

    def _is_forward(self, r, c):
        """
        True if one point forward, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """
        if self._player == 'red':
            if r < self._row:
                return False
        else:
            if r > self._row:
                return False
        return True

    def _is_to_side(self, r, c):
        """
        True if one point to side, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """
        return abs(self._col - c) == 1

    def is_valid(self, r, c):
        """
        True if move is valid, False otherwise
        :param r: int
        :param c: int
        :return: bool
        """

        # 1. one point forward
        # 2. one point horizontal after crossing river
        # 4. never back

        if super().is_valid(r, c):
            return False

        # moving forward?
        if not self._is_forward(r, c):
            return False

        # one point?
        if not self.one_point(r, c):
            return False

        # orthogonal?
        if not self.is_orthogonal(r, c):
            return False

        # crossed river?
        if self.river(r):
            # move forward or to side
            if not self._is_forward(r, c) and not self._is_to_side(r, c):
                return False
        else:
            # forward only
            if not self._is_forward(r, c) or self._is_to_side(r, c):
                return False

        return True

    def move(self, r, c):
        """
        moves the Soldier to the given position
        :param r: int
        :param c: int
        :return: bool
        """
        result = self.is_valid(r, c)

        if result:
            self.update_piece(r, c)     # update self
            return True
        return False


game = XiangqiGame()
game.get_board().print_board()
print(game.make_move('e1', 'e2'))
print(game.make_move('a7', 'a6'))
print(game.make_move('a4', 'b4'))
print(game.make_move('a4', 'a5'))
print(game.make_move('a6', 'a5'))
print(game.make_move('c4', 'c5'))
print(game.make_move('a5', 'b5'))
game.get_board().print_board()
