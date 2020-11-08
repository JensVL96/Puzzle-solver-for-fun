

#   Screen info
SCREEN_HEIGHT = 700
SCREEN_WIDTH = int(SCREEN_HEIGHT * 1.6)
SCREEN_RES = (SCREEN_WIDTH, SCREEN_HEIGHT)

#   Colours
BLACK = (0,0,0)
GREY = (50,50,50)
GREEN = (0,255,0)
RED = (255, 0, 0)
WHITE = (255,255,255)
BEIGE = (242,234,224)

# Box info
BORDER_SIZE = 420
BLOCK_SIZE = BORDER_SIZE / 9
# Corner coordinates
TOP_LX = (SCREEN_WIDTH / 2) - (BORDER_SIZE / 2)
TOP_LY = (SCREEN_HEIGHT / 2) - (BORDER_SIZE / 2)
TOP_RX = (SCREEN_WIDTH / 2) + (BORDER_SIZE / 2)
TOP_RY = (SCREEN_HEIGHT / 2) - (BORDER_SIZE / 2)
BOT_LX = (SCREEN_WIDTH / 2) - (BORDER_SIZE / 2)
BOT_LY = (SCREEN_HEIGHT / 2) + (BORDER_SIZE / 2)
BOT_RX = (SCREEN_WIDTH / 2) + (BORDER_SIZE / 2)
BOT_RY = (SCREEN_HEIGHT / 2) + (BORDER_SIZE / 2)

# Numbers
NUMBER_SIZE = 40
BOLD = 50

# Blinking
BLINK_SPEED = 0.3
BLINK_COLOR = GREEN
ERROR_COLOR = RED

INITIAL_CORDS = (-1, -1)
INITIAL_LOCK = 0