import tkinter as tk
class Cell:
    def __init__(self, master, row, col, game):
        """
        Representation of a single cell in the game
        :param tk.Canvas master: master object
        :param int row: row id of the cell
        :param int col: column id of the cell
        :param game: Game of Life class
        """
        self.row = row
        self.col = col
        self.game = game
        self.active = False
        self.color = "black"
    def onclick(self):
        """
        Method which is called when the cell is clicked
        """
        if self.active:
            self.active = False
        else:
            self.active = True
    @property
    def is_active(self):
        """
        Tells if the cell is active
        :return: If the cell is active
        """
        return self.active

    @property
    def x(self):
        """
        X coordinate of the cell
        :return: x coordinate of the cell
        """
        return self.col

    @property
    def y(self):
        """
        Y coordinate of the cell
        :return: y coordinate of the cell
        """
        return self.row