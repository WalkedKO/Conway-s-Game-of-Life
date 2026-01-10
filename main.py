from gameoflife import GameOfLife
from tkobj import Cell
import tkinter as tk
import threading
from time import sleep

def turn(game_obj, cell_list):
    game_obj.turn()
    for cell in cell_list:
        cell.update()

def run(game_obj, cell_list):
    global go
    go = False
    while True:
        turn(game_obj, cell_list)
        sleep(1.5)
        while not go:
            pass
def run_start():
    global go
    go = True
def run_stop():
    global go
    go = False
if __name__ == "__main__":
    game = GameOfLife(10)
    game.activate([(0, 2), (2,4)])
    root = tk.Tk()
    root.title("Game Of Life")
    squares = []
    size = 10

    game_loop = threading.Thread(target=run, args=(game, squares))
    game_loop.start()

    game_map = tk.Frame(root, width=500, height=400)
    game_map.grid(row=0, column=0)

    buttons = tk.Frame(root)
    buttons.grid(row=1, column=0)

    startButton = tk.Button(buttons, text="Start", command=run_start)
    stopButton = tk.Button(buttons, text="Stop", command=run_stop)

    startButton.grid(row=0, column=0)
    stopButton.grid(row=0, column=1)

    for y in range(size):
        for x in range(size):
            new_obj = Cell(game_map, y, x, 'gray', 'white', game)
            new_obj.grid(row=y, column=x)
            squares.append(new_obj)



    root.mainloop()

