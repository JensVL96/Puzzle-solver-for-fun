# -*- coding: utf-8 -*-
from __future__ import print_function
from config import *
from create_board import *
from solve_bloard import *
from display_board import *

from string import *
import pygame as pg
import numpy as np

def get_cord(pos): 
    global x 
    x = pos[0]//BLOCK_SIZE 
    global y 
    y = pos[1]//BLOCK_SIZE 

def valid()


def valid(grid, i, j, val): 
    for it in range(9): 
        if grid[i][it]== val: 
            return False
        if grid[it][j]== val: 
            return False
    it = i//3
    jt = j//3
    for i in range(it * 3, it * 3 + 3): 
        for j in range (jt * 3, jt * 3 + 3): 
            if m[i][j]== val: 
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

        flag1 = 0
        val = 0

        self.board = create_board().board
        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    flag1 = 1
                    pos = pg.mouse.get_pos()
                    get_cord(pos)
                if event.type == pg.KEYDOWN:
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
