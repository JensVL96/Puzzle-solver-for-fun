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

    def draw(self, grid, cell):
        for i in range (9):
            for j in range (9):
                if grid[i][j] != 0:
                    if type(grid[i][j]) != int:
                        self.draw_candidates(grid, cell)
                    else:
                        text1 = self.font_num.render(str(grid[i][j]), 1, BLACK)
                        self.screen.blit(text1, (TOP_LX + i * BLOCK_SIZE + 15, TOP_LY + j * BLOCK_SIZE + 14))

        size = 0
        for i in range(10):
            if i %3 == 0:
                thick = 7
            else:
                thick = 1

            if i % 3 == 1:
                size +=7

            # print("line: ", i, size)
            # print("Start: ", TOP_LX, TOP_LY + i * BLOCK_SIZE + size, "end: ", TOP_RX, TOP_RY + i * BLOCK_SIZE + size)
            # print("Start: ", TOP_LX + i * BLOCK_SIZE + size, TOP_LY, "end: ", BOT_LX + i * BLOCK_SIZE + size, BOT_LY)
            pg.draw.line(self.screen, BLACK, (TOP_LX, 
                                            TOP_LY + i * BLOCK_SIZE + size), 
                                            (TOP_RX + 21, 
                                            TOP_RY + i * BLOCK_SIZE + size), thick)
            pg.draw.line(self.screen, BLACK, (TOP_LX + i * BLOCK_SIZE + size, 
                                            TOP_LY), 
                                            (BOT_LX + i * BLOCK_SIZE + size, 
                                            BOT_LY + 21), thick)

            # For candidate placement
            # if i % 3 == 0:
            #     print(BLOCK_SIZE)
            #     pg.draw.line(self.screen, BLACK, (cell[0], 
            #                                     cell[1] + i * (cell[2] / 9)), 
            #                                     ((cell[0] + cell[2]), 
            #                                     cell[1] + i * (cell[2] / 9)), 1)
            #     pg.draw.line(self.screen, BLACK, (cell[0] + i * (cell[3] / 9), 
            #                                     cell[1]), 
            #                                     (cell[0] + i * (cell[3] / 9),
            #                                     cell[1] + cell[3]), 1)

    def draw_candidates(self, grid, cell):
        new_line = 1
        iteration = 1
        indent = 15
        for number in grid[i][j]:
            if iteration % 3 == 1:    # Checking if first in line: 1, 4, 7
                text1 = self.font_cdt.render(str(number), 1, BLACK)
                self.screen.blit(text1, (cell[0] + 3, cell[1] + ((new_line - 1) * indent) + 2))
            else:
                text1 = self.font_cdt.render(str(number), 1, BLACK)
                self.screen.blit(text1, (cell[0] + ((iteration - 1) * indent) + 3, cell[1] + ((new_line - 1) * indent) + 2))
            if iteration % 3 == 0:      # checking if last in line: 3, 6
                new_line += 1
                iteration = 0

            iteration += 1


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

