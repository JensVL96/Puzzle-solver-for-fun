# -*- coding: utf-8 -*-
from __future__ import print_function
from config import *
from create_board import *
from solve_bloard import *
from display_board import *
from input_handler import *

from string import *
import pygame as pg
import numpy as np

def get_cord(pos): 
    global x 
    x = pos[0]//BLOCK_SIZE 
    global y 
    y = pos[1]//BLOCK_SIZE 

class Main():
    def __init__(self):
        self.board = []
        self.run()

    def run(self):
        pg.init()
        self.screen = pg.display.set_mode(SCREEN_RES)
        pg.display.set_caption('Sudoku solver')

        display = Display_board(self.screen)

        flag1 = 0
        val = 0

        self.board = create_board().board
        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    exit()
                
                if event.type == pg.KEYDOWN:
                    Input_handler.event_keys(event.key)
                if event.type == pg.MOUSEBUTTONDOWN:
                    flag1 = 1
                    pos = pg.mouse.get_pos()
                    get_cord(pos)

            if val != 0:
                display.draw_val(val, x, y)

                if valid(grid, int(x), int(y), val) == True:
                    grid[int(x)][int(y)] = val
                else:
                    grid[int(x)][int(y)] = 0
                    raise_error2()
                val = 0

            pg.draw.rect(self.screen, BLACK, (0, 0, self.screen.get_width(), self.screen.get_height()))
            self.screen.fill(BEIGE)

            display.draw(self.board)
            # display.draw_box()

            pg.display.update()


        self.solution = solve_board(self.board)

        self.solution.assign_flags(self.board)

if __name__ == '__main__':
    Main()
