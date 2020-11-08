from config import *
import pygame as pg

class Display_board():
    def __init__(self, screen):
        self.screen = screen
        self.font_num = pg.font.SysFont("comicsans", NUMBER_SIZE) 

    def draw_val(self, val, x, y):
        text1 = self.font_num.render(str(val), 1, BLACK)
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

    def update(self, grid, row, col, blk):
        font_val = pg.font.SysFont("comicsans", BOLD)

        if row != (0, 0):
            # Remove old number
            text1 = self.font_num.render(str(grid[row[0]][row[1]]), 1, WHITE)
            self.screen.blit(text1, (TOP_LX + row[0] * BLOCK_SIZE + 15, TOP_LY + row[1] * BLOCK_SIZE + 15))

            # Rewrite in bigger font
            text1 = font_val.render(str(grid[row[0]][row[1]]), 1, BLACK)
            self.screen.blit(text1, (TOP_LX + row[0] * BLOCK_SIZE + 14, TOP_LY + row[1] * BLOCK_SIZE + 10))
        
        if col != (0, 0):
            # Remove old number
            text1 = self.font_num.render(str(grid[col[0]][col[1]]), 1, WHITE)
            self.screen.blit(text1, (TOP_LX + col[0] * BLOCK_SIZE + 15, TOP_LY + col[1] * BLOCK_SIZE + 15))

            # Rewrite in bigger font
            text1 = font_val.render(str(grid[col[0]][col[1]]), 1, BLACK)
            self.screen.blit(text1, (TOP_LX + col[0] * BLOCK_SIZE + 14, TOP_LY + col[1] * BLOCK_SIZE + 10))

        if blk != (0, 0):
            # Remove old number
            text1 = self.font_num.render(str(grid[blk[0]][blk[1]]), 1, WHITE)
            self.screen.blit(text1, (TOP_LX + blk[0] * BLOCK_SIZE + 15, TOP_LY + blk[1] * BLOCK_SIZE + 15))

            # Rewrite in bigger font
            text1 = font_val.render(str(grid[blk[0]][blk[1]]), 1, BLACK)
            self.screen.blit(text1, (TOP_LX + blk[0] * BLOCK_SIZE + 14, TOP_LY + blk[1] * BLOCK_SIZE + 10))

    def glow(self, x, y):
        if x == 0 and y == 0:
            return
        start_pos_x = int(TOP_LX + x * BLOCK_SIZE + 1)
        start_pos_y = int(TOP_LY + y * BLOCK_SIZE + 1)
        end_pos_x = int(start_pos_x + BLOCK_SIZE - 1)
        end_pos_y = int(start_pos_y + BLOCK_SIZE - 1)
        print(BLOCK_SIZE, start_pos_x, start_pos_y, end_pos_x, end_pos_y)
        pg.draw.rect(self.screen, GREEN, (start_pos_x, start_pos_y, end_pos_x, end_pos_y))

