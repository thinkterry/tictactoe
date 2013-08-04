# Tic-tac-toe

import random

class Cell():

    EMPTY = ' '
    X = 'X'
    O = 'O'

    def __init__(self):
        self._val = Cell.EMPTY

    def val(self, new_val=None):
        if new_val is None:  # get
            return self._val
        else:  # set
            self._val = new_val

class Board():

    def __init__(self):
        self.SIZE = 3
        self.board = self._new_board(self.SIZE)

    def _new_board(self, size):
        retval = []
        for i in range(size):
            retval.append([])
            for j in range(size):
                retval[i].append(Cell())
        return retval

    def repr(self):
        print
        for i in range(self.SIZE):
            print ('+ - ' * self.SIZE) + '+'
            print '| ' + ' | '.join([self.board[i][j].val() for j in range(self.SIZE)]) + ' |'
        print '+ - ' * self.SIZE + '+'

    def move(self, player):
        i_rand = random.choice(range(3))
        j_rand = random.choice(range(3))
        self.board[i_rand][j_rand].val(player)

    def full(self):
        """ Innocent until proven guilty """

        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.board[i][j].val() == Cell.EMPTY:
                    return False
        return True

    def done(self):
        return self.winner() or self.full()

    def winner(self):
        horizontal = (
            (self.board[0][0].val() == self.board[0][1].val() == self.board[0][2].val() != Cell.EMPTY) or
            (self.board[1][0].val() == self.board[1][1].val() == self.board[1][2].val() != Cell.EMPTY) or
            (self.board[2][0].val() == self.board[2][1].val() == self.board[2][2].val() != Cell.EMPTY)
        )
        vertical = (
            (self.board[0][0].val() == self.board[1][0].val() == self.board[2][0].val() != Cell.EMPTY) or
            (self.board[0][1].val() == self.board[1][1].val() == self.board[2][1].val() != Cell.EMPTY) or
            (self.board[0][2].val() == self.board[1][2].val() == self.board[2][2].val() != Cell.EMPTY)
        )
        diagonal = (
            (self.board[0][0].val() == self.board[1][1].val() == self.board[2][2].val() != Cell.EMPTY) or
            (self.board[0][2].val() == self.board[1][1].val() == self.board[2][0].val() != Cell.EMPTY)
        )

        return horizontal or vertical or diagonal

if __name__ == '__main__':
    board = Board()

    while not board.done():
        board.move(Cell.X)
        board.move(Cell.O)

    board.repr()
