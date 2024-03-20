import numpy as np
with open('data.txt', 'r') as file:
    # Turn lines of data.txt into a list
    lines = file.readlines()

    # Make each line in the list equal to the nth row of the grid
    row_list = []
    for i in range(0,20):
        row = lines[i].strip()
        row_of_strings = row.split(' ')
        row_of_ints = []
        for string in row_of_strings:
            row_of_ints.append(int(string))
        row_list.append(row_of_ints)

    grid = np.array(row_list)
    products = []

    # Left and Right:
    for m in range(0,20):
        for i in range(0,17):
            product = grid[m,i] * grid[m,i+1] * grid[m,i+2] * grid[m,i+3]
            products.append(product)

    # Up and Down:
    for n in range(0,20):
        for i in range(0,17):
            product = grid[i,n] * grid[i+1,n] * grid[i+2,n] * grid[i+3,n]
            products.append(product)

    # Diagonal Down and to the Left:
    for i in range(0,17):
        for j in range(0,17):
            product = grid[i,j] * grid[i+1,j+1] * grid[i+2,j+2] * grid[i+3,j+3]
            products.append(product)

    # Diagonal Up and to the Right:
    for i in range(3,20):
        for j in range(0,17):
            product = grid[i,j] * grid[i-1,j+1] * grid[i-2,j+2] * grid[i-3,j+3]
            products.append(product)

    print(max(products))