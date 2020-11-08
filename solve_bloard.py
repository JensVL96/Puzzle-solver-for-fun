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