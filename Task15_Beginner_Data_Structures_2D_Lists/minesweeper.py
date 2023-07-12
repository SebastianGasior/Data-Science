#This is a Python function called `mine_sweeper` that takes a 2D grid of characters as its input 
#and returns the same grid with every "-" replaced by the number of adjacent "#" characters, 
#representing mines. 
#The function first finds the number of rows and columns in the input grid using 
#the `len()` function. Then it loops through each spot in the grid using nested for-loops. 
#If the current spot is a mine ("-"), the function counts the number of surrounding mines 
#by looping through neighboring spots using another set of for-loops. 
#The function replaces the current spot with the count of surrounding mines, 
#and finally returns the modified grid.
#An example input grid is defined at the bottom of the code, 
#and the `mine_sweeper` function is called on this input to generate a modified grid, 
#which is stored in a variable called `output`. 
#Finally, the resulting modified grid is printed to the console using the `print()` function.

# This function takes a grid as input and returns the same grid with every "-" replaced by the number of adjacent mines ("#").
def mine_sweeper(grid):
    row_length = len(grid)       # Get the number of rows in the grid.
    col_length = len(grid[0])    # Get the number of columns in the grid.
    for row_index, row in enumerate(grid):   # Loop through each row of the grid.
        for col_index, spot in enumerate(row):    # Loop through each column of the grid.
            if spot == "-":    # If the current spot is a mine ("-"), count the surrounding mines.
                count = 0
                for i in range(max(0, row_index - 1), min(row_index + 2, row_length)):
                    for j in range(max(0, col_index - 1), min(col_index + 2, col_length)):
                        if grid[i][j] == "#":
                            count += 1
                grid[row_index][col_index] = str(count)   # Replace the current spot with the count of surrounding mines.
    return grid   # Return the modified grid.

# Example usage 
input_grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

output = mine_sweeper(input_grid)   # Run the mine_sweeper function on the example input_grid.
print(output)   # Print the resulting modified grid to the console.
