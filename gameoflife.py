from random import randint
def copy_two_dim(board):
    """
    These methods copies 2D list
    :param list[list] board: the 2D list
    :return: copy of the 2D list
    """
    return [[i for i in j] for j in board]
class GameOfLife:
    def __init__(self, board_size_x, board_size_y):
        """
        Main logic behind the game of life class. Contains a 2D list of boolean which represent cells.
        :param board_size_x: number of cells in horizontal
        :param board_size_y: number of cells in vertical
        """
        self.board = [[False for i in range(board_size_x)] for j in range(board_size_y)]
        self.board_size_x = board_size_x
        self.board_size_y = board_size_y

    @classmethod
    def from_list(cls, board):
        """
        Copying constructor.
        :param list[list[boolean]] board: 2D list of booleans
        :return: A new object of the GameOfLife class
        :rtype: GameOfLife
        """
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
        """
        Returns number of activated neighbours of a cell of coordinates x and y
        :param int x: x coordinate of the cell
        :param int y: y coordinate of the cell
        :return: number of neighbours
        :rtype: int
        """
        count = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i != x or j != y:
                    if 0 <= i < self.board_size_x and 0 <= j < self.board_size_y:
                        if self.board[j][i]:
                            count += 1
        return count

    def turn_off(self, x, y):
        """
        Kills a cell
        :param x: x coordinate of the cell
        :param y: y coordinate of the cell
        """
        self.board[y][x] = False
    def __copy__(self):
        return GameOfLife.from_list(self.board)

    def is_active(self, x, y):
        """
        Tells if a cell is active or not
        :param x: x coordinate of the cell
        :param y: y coordinate of the cell
        :return: If the cell is active
        :rtype: boolean
        """
        return self.board[y][x]

    def turn(self):
        """
        A single turn in the game of life.
        :return: list of cells that changed
        :rtype: list[tuple[int,int]]
        """
        new_board = copy_two_dim(self.board)
        to_return = []
        for y, row in enumerate(self.board):
            for x, element in enumerate(row):
                neigh = self.active_neighbours(x, y)
                if element:
                    new_board[y][x] = (neigh == 2 or neigh == 3)
                else:
                    new_board[y][x] = (neigh == 3)
                if new_board[y][x] != self.board[y][x]:
                    to_return.append((x,y))
        self.board = new_board
        return to_return
    @property
    def empty(self):
        """
        Tells if the board is empty, which means no cell is active.
        :return: If the board is empty
        :rtype: boolean
        """
        for i in self.board:
            for element in i:
                if element:
                    return False
        return True
    @property
    def size(self):
        """
        Size of the board in horizontal and vertical
        :return: horizontal size, vertical size
        :rtype: tuple[int]
        """
        return self.board_size_x, self.board_size_y
    def run(self):
        """
        Used for testing without GUI. Runs and prints every turn till the board is empty, which means there are no active cells
        """
        while not self.empty:
            print()
            self.turn()
            print(self)
    def click_cell(self, x, y):
        """
        Method which is called when a cell is clicked
        :param x: x coordinate of the cell
        :param y: y coordinate of the cell
        """
        self.board[y][x] = not self.board[y][x]

    def reset(self):
        """
        Resets the game to the initial state
        """
        for y, row in enumerate(self.board):
            for x, col in enumerate(row):
                self.board[y][x] = False
    def random(self, chance):
        to_color = []
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                choice = randint(0, 100)
                if choice < chance:
                    self.board[y][x] = True
                    to_color.append((x, y))
        return to_color