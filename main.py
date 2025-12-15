from gameoflife import GameOfLife
if __name__ == "__main__":
    game = GameOfLife(5)
    game.activate([(0, 2), (2,4)])
    print(game.turn())

