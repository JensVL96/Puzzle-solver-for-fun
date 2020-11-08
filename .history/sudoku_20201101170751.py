# -*- coding: utf-8 -*-
from __future__ import print_function
from config import *
from create_board import *
from solve_bloard import *
from display_board import *

from string import *
from math import floor
import pygame as pg
import numpy as np

# For error highlighting
def set_highlight(row, col, blk, lock):
    global input_lock
    input_lock = lock
    global row_index
    row_index = row
    global col_index
    col_index = blk
    global blk_index
    blk_index = col

def get_cord(pos): 
    global box_index_x 
    box_index_x = (pos[0] - TOP_LX)//BLOCK_SIZE 
    global box_index_y 
    box_index_y = (pos[1] - TOP_LY)//BLOCK_SIZE 


def valid(grid, x, y, val): 
    input_lock = 0
    row = col = blk = (0, 0)

    for index in range(9): 
        # Check if value in column
        if grid[x][index] == val: 
            col = (x, index)
            input_lock = 1

        # Check if value in row
        if grid[index][y] == val: 
            row = (index, y)
            input_lock = 1

    # Finds the block
    index_x = x // 3 # integer division
    index_y = y // 3

    # Check if value in block
    for i in range(index_x * 3, index_x * 3 + 3): 
        for j in range (index_y * 3, index_y * 3 + 3): 
            if grid[i][j] == val: 
                blk = (i, j)
                input_lock = 1

    if input_lock == 1:
        set_highlight(row, col, blk, input_lock)
        return False

    return True

class Main():
    def __init__(self):
        self.board = []
        self.run()

    def run(self):
        pg.init()
        self.screen = pg.display.set_mode(SCREEN_RES)
        pg.display.set_caption('Sudoku solver')

        display = Display_board(self.screen)

        val = 0
        blink = False
        alpha = 1
        a_change = True
        blink_color = GREEN
        candidates = []
        
        get_cord(INITIAL_CORDS)
        set_highlight(INITIAL_CORDS, INITIAL_CORDS, INITIAL_CORDS, INITIAL_LOCK)

        board = create_board().board

        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN and input_lock != 1:
                    pos = pg.mouse.get_pos()
                    get_cord(pos)

                    # Checks if selection is on the board
                    if pos[0] < TOP_LX or pos[1] < TOP_LY or pos[0] > int(BOT_RX) or pos[1] > int(BOT_RY):
                        blink = False
                    else:
                        blink = True
                if event.type == pg.KEYDOWN and input_lock != 1:
                    if event.key == pg.K_1:
                        val = 1
                    if event.key == pg.K_2:
                        val = 2
                    if event.key == pg.K_3:
                        val = 3
                    if event.key == pg.K_4:
                        val = 4
                    if event.key == pg.K_5:
                        val = 5
                    if event.key == pg.K_6:
                        val = 6
                    if event.key == pg.K_7:
                        val = 7
                    if event.key == pg.K_8:
                        val = 8
                    if event.key == pg.K_9:
                        val = 9
                    if event.key == pg.K_BACKSPACE:
                        board[int(box_index_x)][int(box_index_y)] = 0
                elif event.type == pg.KEYDOWN and input_lock == 1:
                    if event.key == pg.K_BACKSPACE:
                        val = 0
                        set_highlight(INITIAL_CORDS, INITIAL_CORDS, INITIAL_CORDS, INITIAL_LOCK)
                        blink_color = GREEN
                        board[int(box_index_x)][int(box_index_y)] = 0

            if val != 0:
                # display.draw_val(val, box_index_x, box_index_y)
                print(board[int(box_index_x)][int(box_index_y)])

                board_index = board[int(box_index_x)][int(box_index_y)]
                if valid(board, int(box_index_x), int(box_index_y), val) and board[int(box_index_x)][int(box_index_y)] != 0:
                    if type(board_index) == int:
                        candidates[0] = board_index
                        candidates[1] = val
                        board[int(box_index_x)][int(box_index_y)] = candidates
                    else:
                        board_index.append(val)
                elif valid(board, int(box_index_x), int(box_index_y), val):
                    board[int(box_index_x)][int(box_index_y)] = val
                else:
                    board[int(box_index_x)][int(box_index_y)] = val
                

            # Draws the screen
            pg.draw.rect(self.screen, BLACK, (0, 0, self.screen.get_width(), self.screen.get_height()))
            self.screen.fill(BEIGE)

            # Draws the board
            display.draw(board)

            # Check if cell is selected
            if blink:
                cell = display.find_cell(box_index_x, box_index_y)
                blink = display.blink(alpha, a_change)
                alpha = blink[0]
                a_change = blink[1]
                myRect = pg.Rect(cell)
                
                rectSurf = pg.Surface(myRect.size, pg.SRCALPHA)
                rectSurf.fill(blink_color)
                rectSurf.set_alpha(alpha)
                self.screen.blit(rectSurf, (myRect.x, myRect.y))

            # Check if incorrect input
            if input_lock == 1 and val != 0:
                display.update(board, row_index, col_index, blk_index)
                blink_color = RED
            
            val = 0

            # display.draw_box()

            pg.display.update()


        self.solution = solve_board(board)

        self.solution.assign_flags(board)

if __name__ == '__main__':
    Main()
