# Part 1

example = [
    [7,1],
    [11,1],
    [11,7],
    [9,7],
    [9,5],
    [2,5],
    [2,3],
    [7,3]
]

tiles = []
with open("2025/additional_files/red_tiles_in_grid.txt", "r") as f:
    for line in f:
        tiles.append([int(e) for e in line.rstrip().split(',')])

sorted_tiles = sorted(tiles)

def rectangle_area(corner1, corner2):
    pass
    max_x = max([corner1[0], corner2[0]])
    min_x = min([corner1[0], corner2[0]])
    max_y = max([corner1[1], corner2[1]])
    min_y = min([corner1[1], corner2[1]])
    area = (max_x - min_x + 1) * (max_y - min_y + 1)
    return area

areas = []
for corner1 in sorted_tiles:
    for corner2 in sorted_tiles:
        areas.append(rectangle_area(corner1, corner2))

print(max(areas))

# Part 2
