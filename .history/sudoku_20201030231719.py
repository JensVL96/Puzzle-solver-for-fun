# -*- coding: utf-8 -*-
from __future__ import print_function
import pygame as pg

from config import *
from string import *
import numpy as np

def get_cord(pos): 
    global x 
    x = pos[0]//BLOCK_SIZE 
    global y 
    y = pos[1]//BLOCK_SIZE 


class Display_board():
    def __init__(self, screen):
        self.screen = screen
        self.font1 = pg.font.SysFont("comicsans", 40) 
        

    def draw_val(self, val):
        text1 = self.font1.render(str(val), 1, BLACK)
        self.screen.blit(text1, (x * BLOCK_SIZE + 15, y * BLOCK_SIZE + 15))

    def on_mouse_press(self, x, y, symbol, modifier):
        pass

    def draw(self, grid):
        for i in range (9):
            for j in range (9):
                if grid[i][j] != 0:

                    text1 = self.font1.render(str(grid[i][j]), 1, BLACK)
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
                display.draw_val(val)

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
