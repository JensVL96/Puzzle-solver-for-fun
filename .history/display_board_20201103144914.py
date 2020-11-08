from config import *
import pygame as pg

class Display_board():
    def __init__(self, screen):
        self.screen = screen
        self.font_num = pg.font.SysFont("comicsans", NUMBER_SIZE) 
        self.font_cdt = pg.font.SysFont("comicsans", CANDIDATE_SIZE) 

    def draw_val(self, val, x, y):
        text1 = self.font_num.render(str(val), 1, BLACK)
        self.screen.blit(text1, (x * BLOCK_SIZE + 15, y * BLOCK_SIZE + 15))

    def draw_cdt(self, val, x, y):
        text1 = self.font_cdt.render(str(val), 1, BLACK)
        self.screen.blit(text1, (x * BLOCK_SIZE + 1, y * BLOCK_SIZE + 1))

    def on_mouse_press(self, x, y, symbol, modifier):
        pass

    def draw(self, grid):
        for i in range (9):
            for j in range (9):
                if grid[i][j] != 0:
                    if type(grid[i][j]) != int:
                        new_line = 1
                        iteration = 1
                        indent_h = 7
                        indent_v = 7
                        for number in grid[i][j]:
                            if iteration % 3 == 0:      # checking if last in line: 3, 6
                                new_line += 1
                                iteration = 0
                            elif iteration % 3 == 1:    # Checking if first in line: 1, 4, 7
                                text1 = self.font_cdt.render(str(number), 1, BLACK)
                                self.screen.blit(text1, ((TOP_LX + i * BLOCK_SIZE) + iteration * indent_h, (TOP_LY + j * BLOCK_SIZE) + new_line * indent_v))
                            else:
                                text1 = self.font_cdt.render(str(number), 1, BLACK)
                                self.screen.blit(text1, ((TOP_LX + i * BLOCK_SIZE) + iteration * indent_h, (TOP_LY + j * BLOCK_SIZE) + new_line * indent_v))

                            iteration += 1
                    else:
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

        if row != (-1, -1):
            # Remove old number
            text1 = self.font_num.render(str(grid[row[0]][row[1]]), 1, WHITE)
            self.screen.blit(text1, (TOP_LX + row[0] * BLOCK_SIZE + 15, TOP_LY + row[1] * BLOCK_SIZE + 15))

            # Rewrite in bigger font
            text1 = font_val.render(str(grid[row[0]][row[1]]), 1, BLACK)
            self.screen.blit(text1, (TOP_LX + row[0] * BLOCK_SIZE + 14, TOP_LY + row[1] * BLOCK_SIZE + 10))
        
        if col != (-1, -1):
            # Remove old number
            text1 = self.font_num.render(str(grid[col[0]][col[1]]), 1, WHITE)
            self.screen.blit(text1, (TOP_LX + col[0] * BLOCK_SIZE + 15, TOP_LY + col[1] * BLOCK_SIZE + 15))

            # Rewrite in bigger font
            text1 = font_val.render(str(grid[col[0]][col[1]]), 1, BLACK)
            self.screen.blit(text1, (TOP_LX + col[0] * BLOCK_SIZE + 14, TOP_LY + col[1] * BLOCK_SIZE + 10))

        if blk != (-1, -1):
            # Remove old number
            text1 = self.font_num.render(str(grid[blk[0]][blk[1]]), 1, WHITE)
            self.screen.blit(text1, (TOP_LX + blk[0] * BLOCK_SIZE + 15, TOP_LY + blk[1] * BLOCK_SIZE + 15))

            # Rewrite in bigger font
            text1 = font_val.render(str(grid[blk[0]][blk[1]]), 1, BLACK)
            self.screen.blit(text1, (TOP_LX + blk[0] * BLOCK_SIZE + 14, TOP_LY + blk[1] * BLOCK_SIZE + 10))

    def find_cell(self, x, y):
        # Only applies glow when a cell is selected
        if x == -1 and y == -1:
            return
        
        width = BLOCK_SIZE
        height = BLOCK_SIZE

        # Adjustment in size if bordering a thick line
        if x % 3 == 0:  # If thick line on the left
            start_pos_x = TOP_LX + x * BLOCK_SIZE + 4
            width = BLOCK_SIZE - 4
        else:
            start_pos_x = TOP_LX + x * BLOCK_SIZE + 1

        if (x + 1) % 3 == 0:    # If thick line on the right
            width = BLOCK_SIZE - 3.5

        if y % 3 == 0:  # If thick line on the top
            start_pos_y = TOP_LY + y * BLOCK_SIZE + 4
            height = BLOCK_SIZE - 4
        else:
            start_pos_y = TOP_LY + y * BLOCK_SIZE + 1

        if (y + 1) % 3 == 0:    # If thick line on the bottom
            height = BLOCK_SIZE - 3.5

        return (start_pos_x, start_pos_y, width, height)

    def blink(self, alpha, a_change):
        if a_change:
            alpha += BLINK_SPEED
            if alpha >= 175:
                a_change = False
        elif a_change == False:
            alpha += -BLINK_SPEED
            if alpha <= 30:
                a_change = True
        
        return (alpha, a_change)

