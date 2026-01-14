from gameoflife import GameOfLife
import tkinter as tk
import threading
from time import sleep

class WindowWrapper:
    def __init__(self, width_cells, height_cells, cell_size):
        """
        Wrapper class for the whole "tkinter part" of the project. It creates the GUI and the window
        :param int width_cells: number of cells in the horizontal line
        :param int height_cells: number of cells in the vertical line
        :param int cell_size: size of a single cell
        """
        # tells if the game loop should go or be stopped
        self.go = False
        self.root = tk.Tk()
        self.root.title("Game Of Life")
        self.cell_size = cell_size
        # canvas size
        self.width = width_cells * self.cell_size
        self.height = height_cells * self.cell_size
        # number of cells in the canvas
        self.height_cells = height_cells
        self.width_cells = width_cells

        self.game = GameOfLife(self.width_cells, self.height_cells)
        self.game_loop = threading.Thread(target=self.run_game)
        self.game_loop.start()

        self.game_map = tk.Canvas(width=self.width, height=self.height, bg="gray")
        self.game_map.bind("<1>", self.on_mouse_down)
        self.game_map.grid(row=0, column=0)
        # buttons
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
        # prepares the board
        for y in range(self.height_cells):
            for x in range(self.width_cells):
                self.color_cell(x, y, "black")

    def turn(self):
        """
        One single iteration of the game
        """
        to_update = self.game.turn()
        for cell in to_update:
            x, y = cell
            if self.game.is_active(x, y):
                self.color_cell(x, y, "white")
            else:
                self.color_cell(x, y, "black")
    def run_game(self):
        """
        Run the game with 1.5 second breaks between iterations
        """
        while True:
            self.turn()
            sleep(1.5)
            while not self.go:
                pass

    def run_start(self):
        """
        Start the game loop
        """
        self.go = True

    def run_stop(self):
        """
        Stop the game loop
        """
        self.go = False

    def run(self):
        """
        Run the whole window application
        """
        self.root.mainloop()

    def color_cell(self, x, y, color):
        """
        Color a single cell on the board
        :param int x: x coordinate of the cell
        :param int y: y coordinate of the cell
        :param str color: color of the cell
        """
        x0 = x * self.cell_size
        x1 = (x + 1) * self.cell_size
        y0 = y * self.cell_size
        y1 = (y + 1) * self.cell_size
        self.game_map.create_rectangle(x0, y0, x1, y1, outline="white", fill=color)

    def on_mouse_down(self, event):
        """
        OnClick event of the canvas. Calculates which cell has been clicked and sets it active.
        :param event: click event
        """
        x = int(event.x / self.cell_size)
        y = int(event.y / self.cell_size)
        self.game.click_cell(x, y)
        if self.game.is_active(x,y):
            self.color_cell(x, y, "white")
        else:
            self.color_cell(x, y, "black")

    def reset(self):
        """
        Resets the whole game, it means that it deactivates each cell
        """
        self.game.reset()
        for y in range(self.height_cells):
            for x in range(self.width_cells):
                self.color_cell(x, y, "black")

