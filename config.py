# window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 720
FPS = 60
TITLE = "Fix-It Felix Jr."

# building
TOTAL_FLOORS = 4
WINDOWS_PER_FLOOR = 4
BROKEN_WINDOWS = 8   #  updated  fixed number of broken windows
REPAIRS_REQUIRED = 3

# building, roof, window dimensions
BUILDING_RECT = (140, 190, 520, 460)    # x, y, width, height of the brick wall
ROOF_SIZE = (580, 44)
WINDOW_SIZE = (74, 84)

# play area (where Felix may walk)
PLAY_AREA = (95, 192, 610, 478)         # x, y, width, height
GROUND_Y = 650                          # top of the sidewalk in the background image

# time / difficulty
INTRO_DELAY = 5.0
GAME_DURATION = 60.0

EASY_END = 20.0
MEDIUM_END = 40.0

EASY_DEBRIS_SPEED = 120.0
MEDIUM_DEBRIS_SPEED = 190.0
HARD_DEBRIS_SPEED = 270.0

EASY_SPAWN_INTERVAL = 2.5
MEDIUM_SPAWN_INTERVAL = 1.8
HARD_SPAWN_INTERVAL = 1.2

# Felix (player)
FELIX_SIZE = (75, 98)
FELIX_SPEED = 260
PLAYER_INVULNERABILITY_TIME = 1.5       # seconds of immunity after being hit
FIX_TIME = 0.35                         # seconds the hammer swing takes
FIX_RANGE = 60                          # max distance (px) from a window centre to fix it
MAX_LIVES = 3

# Ralph
RALPH_SIZE = (140, 122)

# Bricks
BRICK_SIZE = (34, 22)

# colours
BACKGROUND_COLOR = (15, 35, 75)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 214, 64)
RED = (230, 60, 60)
GREEN = (80, 220, 90)
DARK = (20, 22, 32)