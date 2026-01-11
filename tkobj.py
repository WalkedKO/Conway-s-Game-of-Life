import tkinter as tk
class Cell(tk.Button):
    def __init__(self, master, row, col, default_color, clicked_color, game):
        self.row = row
        self.col = col
        self.default_color = default_color
        self.clicked_color = clicked_color
        self.game = game
        self.active = False
        super().__init__(master, width=3,height=1,bg=self.default_color, command= lambda:self.onclick())
    def onclick(self):
        if self.active:
            self.game.turn_off((self.col, self.row))
            self.active = False
            self.config(bg = self.default_color)
        else:
            self.game.activate([(self.col, self.row)])
            self.active = True
            self.config(bg = self.clicked_color)
    def update(self):
        if self.game.is_active((self.col, self.row)):
            self.active = True
            self.config(bg=self.clicked_color)
        else:
            self.active = False
            self.config(bg=self.default_color)