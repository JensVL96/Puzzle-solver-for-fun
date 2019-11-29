# -*- coding: utf-8 -*-
from __future__ import print_function
import pygame as pg
from random import sample
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

        # self.lines()

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
    
class cell():
    def __init__(self, board):
    def row():
        pass

    def col():
        pass

    def box():
        pass

    def flag():
        pass

class search():
    def row():
        pass

    def col():
        pass

    def box():
        pass

class flags():
    def assign_flags(self, board):
        self.flags = []
        row_idx = 0
        box_idx = 0

        print("\n")
        for line in board:
            box_idx = 0
            if row_idx >= 3:
                box_idx = 3
            if row_idx >= 6:
                box_idx = 6

            for index in range(9):
                # print("position: ", index, "value: ", line[index])

                # print("row", row_idx, "col", index, "box", box_idx)
                if (index % 3 == 0 and index != 0):
                    box_idx += 1

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
                        elif self.box_flag(value, box_idx):
                            # print("found in box")
                            pass
                        else:
                            temp_flag.append(value)
                            flag_idx += 1
                    print(temp_flag)
                    self.flags.append(temp_flag)
            row_idx += 1

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

    def box_flag(self, index, box_idx):
        for box in self.box_list[0][box_idx]:
            # print("comparing in box ", box, "with ", index, "box_idx ", box_idx)
            if box == index:
                return 1
        return 0


class solve_board():
    def create_lists(self, board):
        self.row = []
        self.col = []
        self.box = []
        self.row_list = []
        self.col_list = []
        self.box_list = []

        for space in range(9):
            self.col.append([])
            self.box.append([])

        row_idx = 0
        for line in board:

            self.row.append(line)

            box_idx = 0
            if row_idx >= 3:
                box_idx = 3
            if row_idx >= 6:
                box_idx = 6

            
            for col_idx in range(9):

                self.col[col_idx].insert(row_idx, line[col_idx])

                if col_idx % 3 == 0:
                    for triple in range(0, 3):
                        self.box[box_idx].insert(len(self.box[row_idx]) + triple, line[col_idx + triple])
                    box_idx += 1

            self.row_list.append(self.row)
            self.col_list.append(self.col)
            self.box_list.append(self.box)
            row_idx += 1

        print("\nrow:")
        for row in self.row_list[0]:
            print(row)
        # print("\ncolumn:")
        # for col in self.col_list[0]:
        #     print(col)
        # print("\nbox:")
        # for box in self.box_list[0]:
        #     print(box)


class Display_board():
    def print_lists(name, list):
        print("%s", name)
        for line in list:
            print(line)



class Main():
    def __init__(self):
        self.board = []
        self.run()

    def run(self):
        self.board = create_board().board

        self.solution = solve_board(self.board)

        self.solution.assign_flags(self.board)

if __name__ == '__main__':
    Main()
