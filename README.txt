Kacper Osmola UJ FAIS 2026
Conway's Game Of Life

This is an implementation of Conway's game of life.
I used Python with tkinter to implement the game.
The rules of the game are simple:
- there is a board of cells
- cells can be alive or dead
- if a dead cell has 3 alive neighbours, it will be alive in the next iteration
- if an alive cell has 2 or 3 alive neighbours, it stays alive, else it dies in the next iteration

In the main window there is a canvas with cells. If you click on a cell, you will change its state.
There are 4 buttons:
- Start - starts the game of life algorithm
- Stop - stops the algorithm
- Next - performs one iteration
- Reset - resets the game
- Random - creates a random board
You can also choose the sleep time between the iterations in the main loop, by passing the time in
milliseconds in the entry at the bottom.

The project is written in three files:
- main.py - only runs the whole algorithm
- gameoflife.py - contains the class responsible for the game's logic: GameOfLife
    It takes two arguments:
    - board_size_x - number of cells in horizontal axis
    - board_size_y: number of cells in vertical
    We can also create the game from the board list using from_list method, it takes a 2D list
    Rest of the methods are:
    - active_neighbours(x,y) - Returns number of activated neighbours of a cell of coordinates x and y
    - turn_off(x,y) - Kills a cell
    - is_active(x, y) - Tells if a cell is active or not (boolean, false or true)
    - turn() -  A single turn in the game of life.
    - run() -  Used for testing without GUI.
    - click_cell(x,y) - Method which is called when a cell is clicked
    - reset() - Resets the game to the initial state
    - random() - Makes a random board state.
    Runs and prints every turn till the board is empty, which means there are no active cells
    There are also properties:
    - empty - Tells if the board is empty, which means no cell is active.
    - size - Size of the board in horizontal and vertical
- tkwindow.py - contains the wrapper class WindowWrapper for the whole "tkinter part" of the project.
    It creates the GUI and the window
    The class takes 3 parameters:
    - width_cells: number of cells in the horizontal line
    - height_cells: number of cells in the vertical line
    - cell_size: size of a single cell
    It also has methods:
    - turn() - One single iteration of the game
    - run_start() - Start the game loop
    - run_stop() - Stop the game loop
    - run() - Run the whole window application (so tkinter mainloop())
    - create_cell(self, x, y, color) -  Creates a cell on the board on coordinates x and y
    - color_cell(self, x, y, color) -  Color a single cell on the board (of coordinates x and y)
    - on_mouse_down() - OnClick event of the canvas.
    Calculates which cell has been clicked and sets it active.
    - reset() - Resets the whole game, it means that it deactivates each cell
    - random() - Makes a random board state.