# -*- coding: utf-8 -*-
from __future__ import print_function
import pygame as pg
from random import sample
from config import *
from string import *
import numpy as np

class create_board():
    def __init__(self):
        self.base  = 3  # Will generate any size of random sudoku board in O(n^2) time
        self.side  = self.base * self.base
        self.nums  = sample(range(1, self.side + 1), self.side) # random numbers
        self.board = [[self.nums[(self.base * (r%self.base) + r//self.base + c)%self.side] for c in range(self.side) ] for r in range(self.side)]
        rows  = [ r for g in sample(range(self.base),self.base) for r in sample(range(g * self.base,(g + 1) * self.base), self.base) ] 
        cols  = [ c for g in sample(range(self.base),self.base) for c in sample(range(g * self.base,(g + 1) * self.base), self.base) ]            
        self.board = [[self.board[r][c] for c in cols] for r in rows]

        # print("\nInput:")
        # for line in self.board: print(line)

        squares = self.side * self.side
        empties = squares * 3//4
        for p in sample(range(squares),empties):
            self.board[p//self.side][p%self.side] = 0

        self.lines()

    def expandLine(self, line):
        return line[0]+line[5:9].join([line[1:5]*(self.base-1)]*self.base)+line[9:13]
        
    def lines(self):
        self.line0  = self.expandLine("╔═══╤═══╦═══╗")
        self.line1  = self.expandLine("║ . │ . ║ . ║")
        self.line2  = self.expandLine("╟───┼───╫───╢")
        self.line3  = self.expandLine("╠═══╪═══╬═══╣")
        self.line4  = self.expandLine("╚═══╧═══╩═══╝")

        self.draw()

    def draw(self):
        symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.nums   = [ [""]+[symbol[n] for n in row] for row in self.board ]
        print(self.line0)
        for r in range(1,self.side+1):
            print( "".join(n+s for n,s in zip(self.nums[r-1],self.line1.split("."))) )
            print([self.line2,self.line3,self.line4][(r%self.side==0)+(r%self.base==0)])

class solve_board():
    def __init__(self, board):
        self.row = []
        self.col = []
        self.cell = []
        self.row_list = []
        self.col_list = []
        self.cell_list = []

        for space in range(9):
            self.col.append([])
            self.cell.append([])

        row_idx = 0
        for line in board:

            self.row.append(line)

            cell_idx = 0
            if row_idx >= 3:
                cell_idx = 3
            if row_idx >= 6:
                cell_idx = 6

            
            for col_idx in range(9):

                self.col[col_idx].insert(row_idx, line[col_idx])

                if col_idx % 3 == 0:
                    for triple in range(0, 3):
                        self.cell[cell_idx].insert(len(self.cell[row_idx]) + triple, line[col_idx + triple])
                    cell_idx += 1

            self.row_list.append(self.row)
            self.col_list.append(self.col)
            self.cell_list.append(self.cell)
            row_idx += 1

        print("\nrow:")
        for row in self.row_list[0]:
            print(row)
        # print("\ncolumn:")
        # for col in self.col_list[0]:
        #     print(col)
        # print("\ncell:")
        # for cell in self.cell_list[0]:
        #     print(cell)

    def assign_flags(self, board):
        self.flags = []
        row_idx = 0
        cell_idx = 0

        print("\n")
        for line in board:
            cell_idx = 0
            if row_idx >= 3:
                cell_idx = 3
            if row_idx >= 6:
                cell_idx = 6

            for index in range(9):
                # print("position: ", index, "value: ", line[index])

                # print("row", row_idx, "col", index, "cell", cell_idx)
                if (index % 3 == 0 and index != 0):
                    cell_idx += 1

                if line[index] == 0:
                    flag_idx = 0
                    temp_flag = []
                    for value in range(1, 10):
                        # print(value)
                        if self.row_flag(value, row_idx):
                            # print("found in row")
                            pass
                        elif self.col_flag(value, index):
                            # print("found in column")
                            pass
                        elif self.cell_flag(value, cell_idx):
                            # print("found in cell")
                            pass
                        else:
                            temp_flag.append(value)
                            flag_idx += 1
                    print(temp_flag)
                    self.flags.append(temp_flag)
            row_idx += 1

    def check_row(self):
        pass

    def column(self, x):
        pass

    def cell(self, row, col):
        pass

    def row_flag(self, index, row_idx):
        for row in self.row_list[0][row_idx]:
            # print("comparing in row ", row, "with ", index, "row_idx ", row_idx)
            if row == index:
                return 1
        return 0
    
    def col_flag(self, index, col_idx):
        for col in self.col_list[0][col_idx]:
            # print("comparing in column ", col, "with ", index, "col_idx ", col_idx)
            if col == index:
                return 1
        return 0

    def cell_flag(self, index, cell_idx):
        for cell in self.cell_list[0][cell_idx]:
            # print("comparing in cell ", cell, "with ", index, "cell_idx ", cell_idx)
            if cell == index:
                return 1
        return 0


class Display_board():
    def __init__(self):

    def on_key_press(self, symbol, modifier):
        pass

    def on_key_release(self, symbol, modifier):
        pass

    def on_mouse_press(self, x, y, symbol, modifier):
        pass

    def on_draw(self):
        pass

    def draw_box(self):
        pg.draw.rect(self.screen, BLACK, (  (SCREEN_WIDTH / 2) - (BORDER_SIZE / 2), 
                                            (SCREEN_HEIGHT / 2) - (BORDER_SIZE / 2), 
                                            BORDER_SIZE, 
                                            BORDER_SIZE))
        pg.draw.rect(self.screen, WHITE, (  (SCREEN_WIDTH / 2) - (BOX_SIZE / 2), 
                                            350 - 205, 
                                            410, 
                                            410))

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

        self.flag1 = 0

        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    flag1 = 1
                    pos = pg.mouse.get_pos()
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
                draw_val(val)

                if valid(grid, int(x), int(y), val) == True:
                    grid[int(x)][int(y)] = val
                else:
                    grid[int(x)][int(y)] = 0
                    raise_error2()
                val = 0

            pg.draw.rect(self.screen, BLACK, (0, 0, self.screen.get_width(), self.screen.get_height()))
            self.screen.fill(BEIGE)

            pg.draw.rect(self.screen, BLACK, (350 * 1.6 - 210, 350 - 210, 420, 420))
            pg.draw.rect(self.screen, WHITE, (350 * 1.6 - 205, 350 - 205, 410, 410))

            pg.display.update()

        self.board = create_board().board

        self.solution = solve_board(self.board)

        self.solution.assign_flags(self.board)

if __name__ == '__main__':
    Main()
