# Tic-tac-toe

class Cell():

    def __init__(self):
        self.val = ' '

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
        for i in range(self.SIZE):
            print ('+ - ' * self.SIZE) + '+'
            print '| ' + ' | '.join([self.board[i][j].val for j in range(self.SIZE)]) + ' |'
        print '+ - ' * self.SIZE + '+'

if __name__ == '__main__':
    board = Board() 
    board.repr()