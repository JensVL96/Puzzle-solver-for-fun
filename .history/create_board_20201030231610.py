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