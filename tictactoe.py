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
        """ Innocent unless proven guilty """

        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.board[i][j].val() == Cell.EMPTY:
                    return False
        
        return True

if __name__ == '__main__':
    board = Board()

    while not board.full():
        board.move(Cell.X)
        board.move(Cell.O)

    board.repr()
