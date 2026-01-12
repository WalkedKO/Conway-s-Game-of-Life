from gameoflife import GameOfLife
from tkobj import Cell
import tkinter as tk
import threading
from time import sleep

class WindowWrapper:
    def __init__(self, size, width_cells, height_cells, cell_size):
        self.size = size
        self.go = False
        self.root = tk.Tk()
        self.root.title("Game Of Life")
        self.cell_size = cell_size
        self.cells = []
        self.width = width_cells * self.cell_size
        self.height = height_cells * self.cell_size
        self.height_cells = height_cells
        self.width_cells = width_cells
        self.game = GameOfLife(self.width_cells, self.height_cells)

        self.game_loop = threading.Thread(target=self.run_game)
        self.game_loop.start()

        self.game_map = tk.Canvas(width=self.width, height=self.height, bg="gray")
        self.game_map.bind("<1>", self.on_mouse_down)
        self.game_map.grid(row=0, column=0)

        self.buttons = tk.Frame(self.root)
        self.buttons.grid(row=1, column=0)

        self.startButton = tk.Button(self.buttons, text="Start", command=self.run_start)
        self.stopButton = tk.Button(self.buttons, text="Stop", command=self.run_stop)
        self.nextButton = tk.Button(self.buttons, text="Next", command=self.turn)
        self.resetButton = tk.Button(self.buttons, text="Reset", command=self.reset)

        self.startButton.grid(row=0, column=0)
        self.stopButton.grid(row=0, column=1)
        self.nextButton.grid(row=0, column=2)
        self.resetButton.grid(row=0,column=3)

        for y in range(self.height_cells):
            row = []
            for x in range(self.width_cells):
                new_obj = Cell(self.game_map, y, x, self.game)
                row.append(new_obj)
                self.color_cell(x, y, "black")
            self.cells.append(row)

    def turn(self):
        self.game.turn()
        threads = []
        for row in self.cells:
            new_thread = threading.Thread(target=self.paint_row, kwargs={"row":row})
            new_thread.run()
            threads.append(new_thread)
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

    def color_cell(self, x, y, color):
        x0 = x * self.cell_size
        x1 = (x + 1) * self.cell_size
        y0 = y * self.cell_size
        y1 = (y + 1) * self.cell_size
        self.game_map.create_rectangle(x0, y0, x1, y1, outline="white", fill=color)

    def on_mouse_down(self, event):
        x = int(event.x / self.cell_size)
        y = int(event.y / self.cell_size)
        clicked = self.cells[y][x]
        clicked.onclick()
        self.game.click_cell(x, y)
        if clicked.is_active:
            self.color_cell(x, y, "white")
        else:
            self.color_cell(x, y, "black")

    def reset(self):
        self.game.reset()
        for y in range(self.height_cells):
            for x in range(self.width_cells):
                self.color_cell(x, y, "black")
                self.cells[y][x].active = False
    def paint_row(self, row):
        for cell in row:
            x = cell.x
            y = cell.y
            cell.active = self.game.is_active(x, y)
            if cell.active:
                self.color_cell(x, y, "white")
            else:
                self.color_cell(x, y, "black")

