# Tic-tac-toe

import random

class Cell():

    EMPTY = ' '
    X = 'X'
    O = 'O'

    def __init__(self):
        self._val = Cell.EMPTY
        self._winner = False

    def val(self, new_val=None):
        if new_val is None:  # get
            return self._val
        else:  # set
            self._val = new_val

    def winner(self, new_winner=None):
        if new_winner is None:  # get
            return self._winner
        else:  # set
            self._winner = new_winner

class Board():

    SIZE = 3

    def __init__(self):
        self.board = self._new_board(Board.SIZE)

    def _new_board(self, size):
        retval = []
        for i in range(size):
            retval.append([])
            for j in range(size):
                retval[i].append(Cell())
        return retval

    def repr(self):
        print
        for i in range(Board.SIZE):
            print ('+ - ' * Board.SIZE) + '+'
            line = ''
            for j in range(Board.SIZE):
                cell_padding = '-' if self.board[i][j].winner() else ' '
                cell_val = cell_padding + self.board[i][j].val() + cell_padding
                line += '|' + cell_val
            line += '|'
            print line
        print '+ - ' * Board.SIZE + '+'

    def move(self, value):
        if self.full():
            return

        while True:
            i_rand = random.choice(range(3))
            j_rand = random.choice(range(3))
            if self.board[i_rand][j_rand].val() == Cell.EMPTY:
                self.board[i_rand][j_rand].val(value)
                break

    def full(self):
        """ Innocent until proven guilty """

        for i in range(Board.SIZE):
            for j in range(Board.SIZE):
                if self.board[i][j].val() == Cell.EMPTY:
                    return False
        return True

    def done(self):
        winner = self.winner()
        full = self.full()
        return { 'done': winner or full,
                 'winner': winner }

    def winner(self):
        winner = None

        # horizontal
        for i in range(3):
            if self.board[i][0].val() == self.board[i][1].val() == self.board[i][2].val() != Cell.EMPTY:
                winner = self.board[i][0].val()
                self.board[i][0].winner(True)
                self.board[i][1].winner(True)
                self.board[i][2].winner(True)
        
        # vertical
        for j in range(3):
            if self.board[0][j].val() == self.board[1][j].val() == self.board[2][j].val() != Cell.EMPTY:
                winner = self.board[0][j].val()
                self.board[0][j].winner(True)
                self.board[1][j].winner(True)
                self.board[2][j].winner(True)

        # diagonal
        if self.board[0][0].val() == self.board[1][1].val() == self.board[2][2].val() != Cell.EMPTY:
            winner = self.board[0][0].val()
            self.board[0][0].winner(True)
            self.board[1][1].winner(True)
            self.board[2][2].winner(True)
        if self.board[0][2].val() == self.board[1][1].val() == self.board[2][0].val() != Cell.EMPTY:
            winner = self.board[0][2].val()
            self.board[0][2].winner(True)
            self.board[1][1].winner(True)
            self.board[2][0].winner(True)

        return winner

if __name__ == '__main__':
    board = Board()
    player = Cell.X  # X goes first
    done = board.done()

    while not done['done']:
        if player != Cell.X:
            player = Cell.X
        else:
            player = Cell.O
        
        board.move(player)
        done = board.done()

    board.repr()
    print
    print 'winner:', done['winner']
