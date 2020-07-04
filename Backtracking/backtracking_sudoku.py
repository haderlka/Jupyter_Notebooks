import copy

# sudoku example, empty cells get the value 0
sudoku = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          #
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          #
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9],
         ]


# Function which checks if value is allowed in cell r=row, c=column for the given sudoku state
def check_constraints(r, c, value, sudoku):  
    # check row
    for i in range(0,9):
        if value == sudoku[r][i]:
            #print("Row violation")
            return False
            
    # check column
    for i in range(0,9):
        if value == sudoku[i][c]:
            #print("Column violation")
            return False
    
    # check square
    r_s = (r // 3) * 3
    c_s = (c // 3) * 3
    for i in range(r_s, r_s+3):
         for j in range(c_s, c_s+3):
            if value == sudoku[i][j]:
                #print("Square violation")
                return False
                
    return True
            
# Function which solves the sudoku
def backtrack_sudoku(sudoku):
    # find not solved cell / find next step to solve towards solution
    sudoku_solved = True
    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku[i][j] == 0:
                r = i
                c = j
                sudoku_solved = False
                break    
        if not sudoku_solved:
            break
    
    if sudoku_solved:
        # solution is found, print it out
        print(sudoku)
        return True
    
    success = False
    for val in range(1,10):
        if check_constraints(r, c, val, sudoku):
            evolved_sudoku = copy.deepcopy(sudoku) #deepcopy was necessary since list.copy was not sufficient to create an independent copy
            evolved_sudoku[r][c] = val
            success = backtrack_sudoku(evolved_sudoku)
            if success:
                break
    
    # For the sake of simplicity the solution is only printed out, but not returned
    return success
        


backtrack_sudoku(sudoku)