from networkx.classes import neighbors

def copy_two_dim(board):
    return [[i for i in j] for j in board]
class GameOfLife:
    def __init__(self, board_size_x, board_size_y):
        self.board = [[False for i in range(board_size_x)] for j in range(board_size_y)]
        self.board_size_x = board_size_x
        self.board_size_y = board_size_y

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
                if i != x or j != y:
                    if 0 <= i < self.board_size_x and 0 <= j < self.board_size_y:
                        if self.board[j][i]:
                            count += 1
        return count

    def turn_off(self, x, y):
        self.board[y][x] = False
    def __copy__(self):
        return GameOfLife.from_list(self.board)

    def is_active(self, x, y):
        return self.board[y][x]

    def turn(self):
        new_board = copy_two_dim(self.board)
        for y, row in enumerate(self.board):
            for x, element in enumerate(row):
                neigh = self.active_neighbours(x, y)
                if element:
                    new_board[y][x] = (neigh == 2 or neigh == 3)
                else:
                    new_board[y][x] = (neigh == 3)
        self.board = new_board
    @property
    def empty(self):
        to_return = False
        for i in self.board:
            for element in i:
                to_return |= element
        return not to_return
    @property
    def size(self):
        return self.board_size_x, self.board_size_y
    def run(self):
        while not self.empty:
            print()
            self.turn()
            print(self)
    def click_cell(self, x, y):
        self.board[y][x] = not self.board[y][x]

    def reset(self):
        for y, row in enumerate(self.board):
            for x, col in enumerate(row):
                self.board[y][x] = False
