import numpy as np

# Part 1
input = [
    '..@@.@@@@.',
    '@@@.@.@.@@',
    '@@@@@.@.@@',
    '@.@@@@..@.',
    '@@.@@@@.@@',
    '.@@@@@@@.@',
    '.@.@.@.@@@',
    '@.@@@.@@@@',
    '.@@@@@@@@.',
    '@.@.@@@.@.'
]

input = []
with open('2025/additional_files/grid_of_rolls_of_paper.txt', 'r') as f:
    for line in f:
        input.append(line.rstrip())
# print(input)


def find_neighbours(grid, row, col):
    len_x, len_y = grid.shape
    x = (row, row, row-1, row+1, row-1, row-1, row+1, row+1)
    y = (col-1, col+1, col, col, col-1, col+1, col-1, col+1)
    neighbours = sorted([grid[i[0]][i[1]] for i in zip(x, y) if 0 <= i[0] <= len_x - 1 and 0 <= i[1] <= len_y - 1])
    return [str(e) for e in neighbours]

# preprocessing data
grid = []
for row in input:
    grid.append([e for e in row])
grid_array = np.array(grid)
print(grid_array)

# go through grid; and neighbours for each point
count_accesible_rolls = 0
for row, values in enumerate(grid_array):
    for col, point in enumerate(values):
        if point == '@':
            neighbours = find_neighbours(grid_array, row, col)
            # fewer than four rolls of paper in the eight adjacent positions
            if neighbours.count('@') < 4:
                count_accesible_rolls += 1
            else:
                continue

print(f'number of accesible rolls: {count_accesible_rolls}')

# Part 2

def removing_rolls_of_paper(grid_array):
    count_accesible_rolls = 0
    for row, values in enumerate(grid_array):
        for col, point in enumerate(values):
            if point == '@':
                neighbours = find_neighbours(grid_array, row, col)
                # fewer than four rolls of paper in the eight adjacent positions
                if neighbours.count('@') < 4:
                    count_accesible_rolls += 1
                    grid_array[row,col] = '.'
                else:
                    continue
    return grid_array, count_accesible_rolls

total_removed_rolls = 0
while count_accesible_rolls > 0:
    grid_array, count_accesible_rolls = removing_rolls_of_paper(grid_array)
    total_removed_rolls += count_accesible_rolls
    
print(f'Total removed rolls rolls: {total_removed_rolls}')
