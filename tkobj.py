import tkinter as tk
class Cell:
    def __init__(self, master, row, col, game):
        self.row = row
        self.col = col
        self.game = game
        self.active = False
    def onclick(self):
        if self.active:
            self.active = False
        else:
            self.active = True
    @property
    def is_active(self):
        return self.active

    @property
    def x(self):
        return self.col

    @property
    def y(self):
        return self.row