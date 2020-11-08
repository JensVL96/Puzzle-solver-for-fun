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
            print("\nline: ---", i, "---")
            if i % 3 == 0:
                print("thick")
                thick = THICK_LINE
            else:
                print("thin")
                thick = THIN_LINE

            if i % 2 == 0:
                print("odd number: ", i)
                indent = (i - 1) * BOX_INDENT
            else:
                indent = i * BOX_INDENT

            pg.draw.line(self.screen, BLACK, (TOP_LX, 
                                            TOPLY + i * BLOCK_SIZE + indent), 
                                            (TOP_RX, 
                                            TOPRY + i * BLOCK_SIZE + indent), thick)
            pg.draw.line(self.screen, BLACK, (TOPLX + i * BLOCK_SIZE + indent, 
                                            TOP_LY), 
                                            (BOTLX + i * BLOCK_SIZE + indent, 
                                            BOT_LY), thick)

        # 3.5 * -- 0 -- 1 -- 1 -- 2 -- 3 -- 3 -- 4 -- 5 -- 5 -- 6
        # 0 --- 45 * 1 + 3.5 --- 45 * 2 + 3.5 --- 45 * 3 + 7 --- 45 * 4 + 10.5 --- 45 * 5 + 10.5 --- 45 * 6 + 14 --- 45 * 7 + 17.5 --- 45 * 8 + 17.5 --- 45 * 9 + 21
        pg.draw.line(self.screen, BLACK, (TOP_LX, TOP_LY), (TOP_RX + 21, TOP_RY), 7)
        pg.draw.line(self.screen, BLACK, (TOP_LX, TOP_LY + 45 * 1 + 3.5), (TOP_RX + 21, TOP_RY + 45 * 1 + 3.5), 1)
        pg.draw.line(self.screen, BLACK, (TOP_LX, TOP_LY + 45 * 1 + 1 * 3.5), (TOP_RX + 21, TOP_RY + 48.5 + 45), 1)
        pg.draw.line(self.screen, BLACK, (TOP_LX, TOP_LY + 52 + 45 + 45), (TOP_RX + 21, TOP_RY + 52 + 45 + 45), 7)
        pg.draw.line(self.screen, BLACK, (TOP_LX, TOP_LY + 52 + 45 + 45 + 48.5), (TOP_RX + 21, TOP_RY + 52 + 45 + 45 + 48.5), 1)
        pg.draw.line(self.screen, BLACK, (TOP_LX, TOP_LY + 52 + 45 + 45 + 48.5 + 45), (TOP_RX + 21, TOP_RY + 52 + 45 + 45 + 48.5 + 45), 1)
        pg.draw.line(self.screen, BLACK, (TOP_LX, TOP_LY + 52 + 45 + 45 + 52 + 45 + 45), (TOP_RX + 21, TOP_RY + 52 + 45 + 45 + 52 + 45 + 45), 7)
        pg.draw.line(self.screen, BLACK, (TOP_LX, TOP_LY + 52 + 45 + 45 + 52 + 45 + 45 + 48.5), (TOP_RX + 21, TOP_RY + 52 + 45 + 45 + 52 + 45 + 45 + 48.5), 1)
        pg.draw.line(self.screen, BLACK, (TOP_LX, TOP_LY + 52 + 45 + 45 + 52 + 45 + 45 + 48.5 + 45), (TOP_RX + 21, TOP_RY + 52 + 45 + 45 + 52 + 45 + 45 + 48.5 + 45), 1)
        pg.draw.line(self.screen, BLACK, (TOP_LX, TOP_LY + 52 + 45 + 45 + 52 + 45 + 45 + 52 + 45 + 45), (TOP_RX + 21, TOP_RY + 52 + 45 + 45 + 52 + 45 + 45 + 52 + 45 + 45), 7)
        
        pg.draw.line(self.screen, BLACK, (TOP_LX, TOP_LY), (BOT_LX, BOT_LY + 21), 7)
        pg.draw.line(self.screen, BLACK, (TOP_LX + 48.5, TOP_LY), (BOT_LX + 48.5, BOT_LY + 21), 1)
        pg.draw.line(self.screen, BLACK, (TOP_LX + 48.5 + 45, TOP_LY), (BOT_LX + 48.5 + 45, BOT_LY + 21), 1)
        pg.draw.line(self.screen, BLACK, (TOP_LX + 52 + 45 + 45, TOP_LY), (BOT_LX + 52 + 45 + 45, BOT_LY + 21), 7)
        pg.draw.line(self.screen, BLACK, (TOP_LX + 52 + 45 + 45 + 48.5, TOP_LY), (BOT_LX + 52 + 45 + 45 + 48.5, BOT_LY + 21), 1)
        pg.draw.line(self.screen, BLACK, (TOP_LX + 52 + 45 + 45 + 48.5 + 45, TOP_LY), (BOT_LX + 52 + 45 + 45 + 48.5 + 45, BOT_LY + 21), 1)
        pg.draw.line(self.screen, BLACK, (TOP_LX + 52 + 45 + 45 + 52 + 45 + 45, TOP_LY), (BOT_LX + 52 + 45 + 45 + 52 + 45 + 45, BOT_LY + 21), 7)
        pg.draw.line(self.screen, BLACK, (TOP_LX + 52 + 45 + 45 + 52 + 45 + 45 + 48.5, TOP_LY), (BOT_LX + 52 + 45 + 45 + 52 + 45 + 45 + 48.5, BOT_LY + 21), 1)
        pg.draw.line(self.screen, BLACK, (TOP_LX + 52 + 45 + 45 + 52 + 45 + 45 + 48.5 + 45, TOP_LY), (BOT_LX + 52 + 45 + 45 + 52 + 45 + 45 + 48.5 + 45, BOT_LY + 21), 1)
        pg.draw.line(self.screen, BLACK, (TOP_LX + 52 + 45 + 45 + 52 + 45 + 45 + 52 + 45 + 45, TOP_LY), (BOT_LX + 52 + 45 + 45 + 52 + 45 + 45 + 52 + 45 + 45, BOT_LY + 21), 7)

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
        block_x = block_y = 1

        # Adjustment in size if bordering a thick line
        print("cell: ", x, y)
        if x % 3 == 0:  # If thick line on the left
            print("column 1, 4 or 7")
        # else:
        #     start_pos_x = TOP_LX + x * BLOCK_SIZE + block * 3.5

        temp_x = x
        for i in range(3):
            if temp_x - 3 >= 0:
                block_x += 2
            temp_x += -3
            i += 1
        print("block x: ", block_x)

        print("extra indent x:", block_x * 3.5)
        start_pos_x = TOP_LX + x * BLOCK_SIZE + block_x * 3.5

        if (x + 1) % 3 == 0:    # If thick line on the right
            print("column 3, 6 or 9")

        if y % 3 == 0:  # If thick line on the top
            print("row 1, 4 or 7")
        # else:
        #     start_pos_y = TOP_LY + y * BLOCK_SIZE# + 1

        if (y + 1) % 3 == 0:    # If thick line on the bottom
            print("row 3, 6 or 9")

        temp_y = y
        for i in range(3):
            if temp_y - 3 >= 0:
                block_y += 2
            temp_y += -3
            i += 1
        print("block y: ", block_y)

        print("extra indent y:", block_x * 3.5)
        start_pos_y = TOP_LY + y * BLOCK_SIZE + block_y * 3.5

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

