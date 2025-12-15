from networkx.classes import neighbors

def copy_two_dim(board):
    return [[i for i in j] for j in board]
class GameOfLife:
    def __init__(self, board_size):
        self.board = [[False for i in range(board_size)] for j in range(board_size)]
        self.board_size = board_size

    @classmethod
    def from_list(cls, board):
        new = cls(len(board))
        new.board = copy_two_dim(board)
        return new
    def __str__(self):
        describe = lambda x : "1" if x else "0"
        line = "\n".join([" ".join([describe(j) for j in i]) for i in self.board])
        return line

    def __repr__(self):
        return str(self.board)

    def active_neighbours(self, x, y):
        count = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i != x and j != y:
                    if 0 <= i < self.board_size and 0 <= j < self.board_size:
                        count += 1
        return count

    def activate(self, points: list):
        for point in points:
            x, y = point
            self.board[y][x] = True

    def __copy__(self):
        return GameOfLife.from_list(self.board)

    def turn(self):
        new_board = copy_two_dim(self.board)
        for y, row in enumerate(self.board):
            for x, element in enumerate(row):
                neigh = self.active_neighbours(y, x)
                if neigh != 2 and neigh != 3:
                    new_board[y][x] = False
        return new_board

    @property
    def size(self):
        return self.board_size