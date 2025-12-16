import itertools

# Part 1

red_tiles = [
    [7,1],
    [11,1],
    [11,7],
    [9,7],
    [9,5],
    [2,5],
    [2,3],
    [7,3]
]

red_tiles = []
with open("2025/additional_files/red_tiles_in_grid.txt", "r") as f:
    for line in f:
        red_tiles.append([int(e) for e in line.rstrip().split(',')])


def rectangle_area(corner1, corner2):
    max_x = max([corner1[0], corner2[0]])
    min_x = min([corner1[0], corner2[0]])
    max_y = max([corner1[1], corner2[1]])
    min_y = min([corner1[1], corner2[1]])
    area = (max_x - min_x + 1) * (max_y - min_y + 1)
    return area

corners_combinations = list(itertools.combinations(red_tiles, 2))
areas = []
for corners in corners_combinations:
        areas.append(rectangle_area(corners[0], corners[1]))

print(f'maximal area of rectangle: {max(areas)}')

# Part 2

def get_edges_of_polygon(tiles):
    edges = []
    for i in range(0,len(tiles)-1):
        for point1, point2 in zip(tiles[i:len(tiles)-2], tiles[i+1:]):
            edges.append([point1, point2])
    # add first-last points as edge
    edges.append([tiles[0],tiles[len(tiles)-1]])
    return edges

def nested_rectangle(corner1, corner2):
    adj_corner1 = []
    adj_corner2 = []
    for i in [0, 1]:
        if corner1[i] < corner2[i]:
            adj_corner1.append(corner1[i] + 1)
            adj_corner2.append(corner2[i] - 1)
        elif corner1[i] > corner2[i]:
            adj_corner1.append(corner1[i] - 1)
            adj_corner2.append(corner2[i] + 1)
        else:    
            adj_corner1.append(corner1[i])
            adj_corner2.append(corner2[i])
    return adj_corner1, adj_corner2
    
def is_rectangle_intersecting_polygon(rect_corner1, rect_corner2, polygon_edges):
    for edge in polygon_edges:
        edge_point1 = edge[0]
        edge_point2 = edge[1]
        max_x = max([corner1[0], rect_corner2[0]])
        min_x = min([rect_corner1[0], rect_corner2[0]])
        max_y = max([rect_corner1[1], rect_corner2[1]])
        min_y = min([rect_corner1[1], rect_corner2[1]])
        # edges are outside of rectangular or on side of rectangular
        edge_is_out_of_x = (edge_point1[0] <= min_x and edge_point2[0] <= min_x) or (edge_point1[0] >= max_x and edge_point2[0] >= max_x)
        edge_is_out_of_y = (edge_point1[1] <= min_y and edge_point2[1] <= min_y) or (edge_point1[1] >= max_y and edge_point2[1] >= max_y)
        if edge_is_out_of_x or edge_is_out_of_y:
            continue
        # edge is inside rectangle
        else:
            return True
    return False

# get edges of polygon
edges = get_edges_of_polygon(red_tiles)

# find out areas of rectanngle (as we are looking for largest-> sorting)
areas_n_corners = []
for corners in corners_combinations:
        areas.append(rectangle_area(corners[0], corners[1]))
        areas_n_corners.append([rectangle_area(corners[0], corners[1]),corners[0], corners[1]])
areas_n_corners.sort(reverse=True)

# check intersection of polygon and rectangles (with red tiles in corners)
largest_area = 0
for area_n_corners in areas_n_corners:
        area = area_n_corners[0]
        corner1 = area_n_corners[1]
        corner2 = area_n_corners[2]
        nested_corner1, nested_corner2 = nested_rectangle(corner1, corner2)
        if corner1 == corner2:
            continue
        elif not(is_rectangle_intersecting_polygon(nested_corner1, nested_corner2, edges)):
            largest_area = area
            break

print(f'maximal area of rectangle: {largest_area}')
