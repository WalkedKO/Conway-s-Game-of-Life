from gameoflife import GameOfLife
from tkobj import Cell
import tkinter as tk
import threading
from time import sleep

class WindowWrapper:
    def __init__(self, size, width, height):
        self.size = size
        self.go = False
        self.game = GameOfLife(self.size)
        self.root = tk.Tk()
        self.root.title("Game Of Life")
        self.cells = []

        self.game_loop = threading.Thread(target=self.run_game)
        self.game_loop.start()

        self.game_map = tk.Frame(self.root, width=width, height=height)
        self.game_map.grid(row=0, column=0)

        self.buttons = tk.Frame(self.root)
        self.buttons.grid(row=1, column=0)

        self.startButton = tk.Button(self.buttons, text="Start", command=self.run_start)
        self.stopButton = tk.Button(self.buttons, text="Stop", command=self.run_stop)

        self.startButton.grid(row=0, column=0)
        self.stopButton.grid(row=0, column=1)

        for y in range(self.size):
            for x in range(self.size):
                new_obj = Cell(self.game_map, y, x, 'gray', 'white', self.game)
                new_obj.grid(row=y, column=x)
                self.cells.append(new_obj)

    def turn(self):
        self.game.turn()
        for cell in self.cells:
            cell.update()

    def run_game(self):
        while True:
            self.turn()
            sleep(1.5)
            while not self.go:
                pass

    def run_start(self):
        self.go = True

    def run_stop(self):
        self.go = False

    def run(self):
        self.root.mainloop()