# -*- coding: utf-8 -*-
from __future__ import print_function
import pygame as pg
import sys
import pprint
from random import sample
from string import *
import numpy as np

class Create_board():
    def __init__(self):
        self.base  = 3  # Will generate any size of random sudoku board in O(n^2) time
        self.side  = self.base * self.base
        self.nums  = sample(range(1, self.side + 1), self.side) # random numbers
        self.board = [[self.nums[(self.base * (r%self.base) + r//self.base + c)%self.side] for c in range(self.side) ] for r in range(self.side)]
        rows  = [ r for g in sample(range(self.base),self.base) for r in sample(range(g * self.base,(g + 1) * self.base), self.base) ] 
        cols  = [ c for g in sample(range(self.base),self.base) for c in sample(range(g * self.base,(g + 1) * self.base), self.base) ]            
        self.board = [[self.board[r][c] for c in cols] for r in rows]

        print("\nInput:")
        for line in self.board: print(line)
        print("\n\n\n")

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
    
class Cell():
    def __init__(self, board, lists, flags, index):
        self.board = board
        self.lists = lists
        self.digit = board[index]
        naked = "Contains a digit"

        self.flag = self.find_flag(flags, index)

        if not self.flag:
            self.flag = naked

    def create_cell(self, board, lists, flags, index):
        self.board = board
        self.lists = lists
        self.flags = flags
        naked = "Contains a digit"

        self.row = self.find_row(index)
        self.col = self.find_col(index)
        self.box = self.find_box(index)
        self.flag = self.find_flag(index)

        if not self.flag:
            self.flag = naked

        return self

    def find_row(self, index):
        return self.lists.ret_row_list(index % len(self.board[0]))

    def find_col(self, index):
        return self.lists.ret_col_list(index % len(self.board[0]))

    def find_box(self, index):
        return self.lists.ret_box_list(index % len(self.board[0]))

    def find_flag(self, flags,  index):
        return flags.ret_flag_list(index)

    def search_flag(self, index):
        print(self.row, self.col, self.box, self.flag)

        search_inst = Search()

        search_inst.row(self.flag, self.row, index)



class Search():
    def __init__(self):
        cell_list = []
        """ while(1):
            cell_list.append(Cell(self.board, lists.ret_row_list(index), lists.ret_col_list(index), lists.ret_box_list(index))
            print(cell_list[1]) """

    # Very easy to medium
    def intersections(box_list):
        result = [ target for target in box_list if box_list.count(target) == 1 ]

    def forced_moves():
        pass

    def pinned_squares():
        pass

    # Hard
    def Locked_sets():
        pass

    def intersection_removal():
        pass

    # Very hard
    def x_wing():
        pass

    def swordfish():
        pass

    def remote_pairs():
        pass

    def unique_rectangles_1():
        pass

    def hidden_sets():
        pass

    # Super hard
    def unique_rectangles_2():
        pass

    def xy_wing():
        pass

    def xyz_wing():
        pass

    def BUG_removal():
        pass

class Candidates():
    flags = []

    def assign_flags(self, board, lists):
        
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
                        if self.line_contains(lists.ret_row_list(row_idx), value, row_idx):
                            # print("found in row")
                            pass
                        elif self.line_contains(lists.ret_col_list(index), value, index):
                            # print("found in column")
                            pass
                        elif self.line_contains(lists.ret_box_list(box_idx), value, box_idx):
                            # print("found in box")
                            pass
                        else:
                            temp_flag.append(value)
                            flag_idx += 1
                    self.flags.append(temp_flag)
                else:
                    self.flags.append([])
            row_idx += 1
        print(self.flags)

    def line_contains(self, line, digit, line_idx):
        for index in line:
            # print("comparing in row ", row, "with ", index, "row_idx ", row_idx)
            if index == digit:
                return 1
        return 0

    def ret_flag_list(self, index):
        # print("idx: ", index, "<- there", self.flags[index])
        return flags[index]

    def ret_list(self):
        return flags


class Lists():
    row_list = []
    col_list = []
    box_list = []

    def init_lists(self, board):
        self.row = []
        self.col = []
        self.box = []
        

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

        display = Display_board()

        display.print_lists("rows: ", self.row_list)
        display.print_lists("columns: ", self.col_list)
        display.print_lists("boxes: ", self.box_list)
        
    def ret_row_list(self, index):
        return self.row_list[0][index]

    def ret_col_list(self, index):
        return self.col_list[0][index]

    def ret_box_list(self, index):
        return self.box_list[0][index]

    def ret_rows(self):
        return self.row_list[0]

    def ret_cols(self):
        return self.col_list[0]

    def ret_boxes(self):
        return self.box_list[0]

class Display_board():
    def print_lists(self, name, lists):
        print(name)
        for line in lists[0]:
            print(line)

    def print_flags(self, flags):
        """ temp_line = []

        for space in range(9):
            temp_line.append([])

        print(flags)
        cell_idx = 0
        for cell in flags:
            max_len = 0

            if cell_idx == 9:
                for i in range(9):
                    print(flags[0][i])
                    if max_len < len(flags[i]):
                        max_len = len(flags[i])

            print(max_len) """
        new_line = -1
        one_time = 0
        for i in range(81):
            new_line += 1
            flags = cell.find_flag(i)

            temp_idx = i % 9

            if i % 9 == 0:
                max_len = 0
                new_line = 0
                print("\n")
                for j in range(9):
                    index = temp_idx * 9 + j
                    print(i, temp_idx, j, index, cell.find_flag(j))
                    if max_len < len(cell.find_flag(index)):
                        max_len = len(cell.find_flag(index))

            if new_line == 0:
                print("length: ",max_len)
            #go though lenght of falgs on one row and check for longest (tabbing print)

            
            if max_len > 5:
                tab = 0
            elif (2 < max_len < 6):
                tab = 2
            else:
                tab = 3
            print(flags, '\t' * tab, end='')
            
            # print(max_len, flags)
            
            # print(new_line, flags)
            temp_line[new_line].insert(new_line, flags)
            
        print("\n")
        # pp = pprint.PrettyPrinter(width=100)
        # for i in range(len(temp_line)):
        #     pp.pprint(temp_line[i])
        #     print(np.matrix(temp_line[i]))
        #     pass

        # flag_list = flag_inst.ret_list()
        # print(flag_list)
        # a = np.array(flag_list, dtype=object)
        # print(a)

        # flags.ret_flag_list(index)
        # print(flags, ", ", end = '')
        # pp = pprint.PrettyPrinter(indent=3)
        # pp.pprint(flags)



class Main():
    def __init__(self):
        self.board = []
        self.board = Create_board().board
        self.list_inst = Lists()
        self.flag_inst = Candidates()
        self.run()

    def run(self):
        self.list_inst.init_lists(self.board)
        self.flag_inst.assign_flags(self.board, self.list_inst)
        display = Display_board()
        # display.print_flags(self.flag_inst)


        # cell_inst = Cell()
        # for i in range(len(self.board[0]) * len(self.board)):

        #     cell_inst.create_cell(self.board, self.list_inst, self.flag_inst, i)

        #     cell_inst.search_flag(i)

        



if __name__ == '__main__':
    Main()



# Search methods

# only instance of number on row/ on column/ in box

# Sharing a tuple/ triple/+ with others in same row/ column with the same length in both