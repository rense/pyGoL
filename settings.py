CELL_WIDTH, CELL_HEIGHT = 24, 25

GAME_COLS, GAME_ROWS = 40, 40

GAME_WIDTH, GAME_HEIGHT = CELL_WIDTH * GAME_COLS, CELL_HEIGHT * GAME_ROWS

GAME_TITLE = "Conway's Game of Life"
GAME_BACKGROUND_COLOR = (255, 255, 255)
GAME_GRID_COLOR = (200, 200, 200)
GAME_CELL_COLOR = (0, 0, 0)
GAME_FPS = 60

GAME_SPEED = 5
GAME_MIN_SPEED = 1
GAME_MAX_SPEED = 30

GRID_CELL_THICKNESS = 1

GAME_STATE_QUIT = -1
GAME_STATE_SPLASH = 0
GAME_STATE_CONFIG = 1
GAME_STATE_RUNNING = 2
GAME_STATE_PAUSED = 3

GAME_STATES = {
    GAME_STATE_QUIT: 'quit',
    GAME_STATE_SPLASH: 'splash',
    GAME_STATE_CONFIG: 'config',
    GAME_STATE_RUNNING: 'running',
    GAME_STATE_PAUSED: 'paused',
}

CELL_STATE_DEAD = 0
CELL_STATE_ALIVE = 1

###

BLUE = (106, 159, 181)
WHITE = (255, 255, 255)
