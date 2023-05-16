GAME_NAME = "Utopia"

#game window scaler
GRID_SIZE = 20

MOVEMENT = 8

#coins collected by the player
coins = 0

#game map (grid) creation (not auto generated)
grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 7, 0, 0, 0, 5, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 5, 
5, 8, 8, 8, 8, 8, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 7, 0, 0, 0, 0, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 5, 7, 0, 0, 4, 5, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 5, 7, 0, 0, 4, 0, 0, 0], [0, 0, 0, 9, 10, 2, 11, 
11, 12, 0, 12, 2, 2, 2, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 5, 7, 0, 0, 4, 11, 12, 0], [0, 0, 0, 13, 14, 8, 15, 15, 16, 15, 0, 8, 8, 8, 5, 5, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 5, 7, 0, 0, 4, 15, 16, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 2, 2, 2, 2, 2, 2, 
2, 5, 5, 2, 2, 2, 0, 0, 5, 7, 0, 0, 0, 0, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 5, 5, 0, 0, 5, 7, 0, 0, 4, 5, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 5, 7, 0, 0, 4, 5, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 5, 7, 0, 0, 4, 11, 0, 0], [0, 5, 5, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 5, 7, 0, 0, 4, 0, 0, 0], [0, 8, 8, 8, 8, 8, 8, 8, 17, 18, 8, 8, 8, 8, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 20, 0, 0, 5, 5, 5, 5, 5, 5, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 21, 22, 22, 22, 23, 0, 0, 0, 0, 23, 0, 0, 0, 0, 23, 22, 22, 22, 24, 25, 0, 0, 8, 8, 8, 5, 5, 5, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 20, 19, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 25, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 25, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 23, 
23, 0, 0, 0, 0, 23, 23, 23, 0, 0, 0, 23, 23, 23, 23, 23, 25, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0], [0, 1, 2, 2, 2, 2, 2, 2, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 23, 23, 0, 0, 0, 0, 23, 23, 23, 0, 0, 0, 23, 23, 23, 23, 23, 25, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0], [0, 4, 5, 5, 5, 5, 5, 5, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 23, 23, 0, 0, 0, 0, 23, 23, 0, 0, 0, 0, 23, 23, 23, 23, 23, 21, 0, 0, 0, 5, 5, 5, 5, 5, 7, 0], [0, 4, 5, 0, 0, 0, 0, 0, 27, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 20, 0, 0, 0, 5, 5, 5, 5, 5, 7, 0], [0, 4, 5, 0, 0, 0, 0, 0, 27, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 25, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0], [0, 4, 5, 0, 0, 0, 0, 0, 27, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 23, 23, 23, 23, 23, 0, 0, 0, 0, 23, 23, 23, 23, 23, 23, 23, 23, 25, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0], [0, 4, 5, 0, 0, 0, 0, 0, 27, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 23, 23, 23, 23, 23, 0, 0, 0, 0, 23, 23, 23, 23, 23, 23, 23, 23, 25, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0], [0, 4, 5, 0, 0, 0, 0, 0, 27, 28, 2, 2, 2, 2, 2, 2, 2, 2, 2, 21, 29, 24, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0], [0, 4, 5, 2, 2, 2, 2, 2, 30, 18, 8, 8, 8, 8, 5, 5, 5, 5, 5, 20, 31, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 
32, 19, 20, 32, 32, 0, 0, 0, 0, 5, 5, 2, 2, 2, 0, 0], [0, 33, 8, 8, 8, 8, 8, 8, 8, 34, 0, 0, 0, 0, 5, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0, 5, 5, 18, 17, 
5, 5, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 5, 5, 18, 30, 5, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 35, 5, 28, 5, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 30, 30, 5, 5, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 5, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 4, 0, 0, 0, 
0, 0, 4, 5, 5, 5, 5, 5, 5, 6, 0], [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 30, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 4, 6, 0, 0, 0, 8, 5, 5, 5, 5, 5, 5, 5, 6, 0], [0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 4, 6, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
4, 6, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 36, 5, 37, 5, 5, 38, 5, 39, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 4, 28, 2, 2, 2, 2, 2, 2, 5, 5, 2, 2, 2, 3, 0], [0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 
2, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 4, 18, 8, 8, 17, 5, 18, 5, 17, 28, 30, 30, 5, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 30, 28, 30, 28, 28, 17, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 4, 6, 0, 0, 27, 5, 28, 17, 28, 30, 18, 30, 5, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0, 5, 5, 5, 18, 30, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 4, 6, 0, 
0, 27, 18, 8, 8, 17, 18, 8, 8, 17, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 0, 0, 27, 7, 0, 0, 33, 34, 0, 0, 4, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 0, 0, 27, 7, 0, 0, 40, 41, 0, 0, 4, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 0, 0, 33, 34, 0, 0, 42, 43, 0, 0, 33, 34, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 30, 6, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 34, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#game map width and height
GRID_WIDTH = len(grid[0]) * GRID_SIZE
GRID_HEIGHT = len(grid) * GRID_SIZE

# window width and height
WIDTH = int((len(grid[0]) * 1.5) * GRID_SIZE)
HEIGHT = int(len(grid) * GRID_SIZE)

#used colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG_GRAY = (20,20,18)
TERM_GRAY = (10,10,9)

# text field history
command_history = [""]
command_index = 0

# zoom factor
ZOOM = 3

CHANGE_THRESHOLD = 0.1

# zoom implementation
def zoomify(_number):
    # i guess 500 was magic, who knew
    return ZOOM*_number+(25*GRID_SIZE)
