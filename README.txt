Kacper Osmola UJ FAIS 2026
Conway's Game Of Life

This is an implementation of Conway's game of life, the rules of the game are simple:
- there is a board of cells
- cells can be alive or dead
- if a dead cell has 3 alive neighbours, it will be alive in the next iteration
- if an alive cell has 2 or 3 alive neighbours, it stays alive, else it dies in the next iteration

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
    -