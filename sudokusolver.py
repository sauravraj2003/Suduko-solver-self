N=9

# We will create a function to check if the number can be placed at that position
def isPossible(sudoku,row,col,num):

    #check if the number is appearing in the given row
    for i in range(0,9):
        if sudoku[row][i]==num:
            return False

    #check if the number is appearing in the given column
    for i in range(0,9):
        if sudoku[i][col]==num:
            return False

    #Intialise the starting row and column of the 3x3 grid
    startingRow= (row//3)*3
    startingCol= (col//3)*3

    #check if the number is appearing in the 3x3 grid
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[startingRow+i][startingCol+j]==num:
                return False

    return True


def solveSudoku(sudoku,row,col):

    #check if we reached at the end of sudoku.If yes,we have solved sudoku and return true
    if row==N-1 and col==N:
        return True

    #check if we reached at last column but then we have to move to the next row and column=0
    if col==N:
        row+=1
        col=0

    #check if the given position is already solved.If yes,then we move to next column
    if sudoku[row][col]>0:
        return solveSudoku(sudoku,row,col+1)

    #If the given position is empty,iterate through numbers 1-9 to check
    for num in range(1,N+1):
        if isPossible(sudoku,row,col,num):
            sudoku[row][col]=num
            if solveSudoku(sudoku,row,col+1):
                return True
            sudoku[row][col]=0
    return False

# if the sudoku can be solved,return the modified sudoku.Else, return no.
def solver(sudoku):
    if solveSudoku(sudoku,0,0):
        return sudoku
    else:
        return "no"
