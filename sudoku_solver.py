from pprint import pprint


# Find the empty cell for entering the number
def empty_cell(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return (r, c)
    return (None, None)  # If there are no empty spaces


# Check if the number in the cell is valid
def valid_entry(grid, row, col, num):

    # Check if number is in the current row
    if num in grid[row]:
        return False  # If the number is present in the row

    # Check if number is in the current column
    for r in range(9):
        if grid[r][col] == num:
            return False  # If the number is present in the column

    # Check if number is in the current 3x3 subgrid
    # Determine the start position from the 3 sets of rows and columns in the 9x9 grid
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if grid[r][c] == num:
                return False  # If the number is present in the 3x3 subgrid

    # If the number does not exist and is valid
    return True


# Solve the Sudoku grid using backtracking
def solver(grid):
    row, col = empty_cell(grid)

    if row is None:  # Grid is solved as there are no empty spaces
        return True

    # If there is an empty space, guess the number to place in that cell
    for num in range(1, 10):

        # Place the valid number returned to the empty cell position
        if valid_entry(grid, row, col, num):
            grid[row][col] = num

            if solver(grid):  # Recursively attempt to solve
                return True

        # If num does not solve the grid or no valid number is found, backtracking is triggered
        grid[row][col] = 0

    return False  # If none of the numbers work, it is unsolvable


if __name__ == "__main__":
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

print(solver(grid))
pprint(grid)
