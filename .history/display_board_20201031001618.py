from config import *
import pygame as pg

class Display_board():
    def __init__(self, screen):
        self.screen = screen
        self.font_num = pg.font.SysFont("comicsans", 40) 

    def draw_val(self, val, x, y):
        text1 = self.font1.render(str(val), 1, BLACK)
        self.screen.blit(text1, (x * BLOCK_SIZE + 15, y * BLOCK_SIZE + 15))

    def on_mouse_press(self, x, y, symbol, modifier):
        pass

    def draw(self, grid):
        for i in range (9):
            for j in range (9):
                if grid[i][j] != 0:

                    text1 = self.font_num.render(str(grid[i][j]), 1, BLACK)
                    self.screen.blit(text1, (TOP_LX + i * BLOCK_SIZE + 15, TOP_LY + j * BLOCK_SIZE + 15))

        for i in range(10):
            if i %3 == 0:
                thick = 7
            else:
                thick = 1
            pg.draw.line(self.screen, BLACK, (TOP_LX, 
                                            TOP_LY + i * BLOCK_SIZE), 
                                            (TOP_RX, 
                                            TOP_RY + i * BLOCK_SIZE), thick)
            pg.draw.line(self.screen, BLACK, (TOP_LX + i * BLOCK_SIZE, 
                                            TOP_LY), 
                                            (BOT_LX + i * BLOCK_SIZE, 
                                            BOT_LY), thick)

    def update(self, dt):
        pass

