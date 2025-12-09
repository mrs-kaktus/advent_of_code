import math
import itertools
import numpy

#  Part 1

# which junction boxes to connect so that electricity can reach every junction box
# one line, one junction box coordinates X,Y,Z
junction_boxes = [
    [162,817,812],
    [57,618,57],
    [906,360,560],
    [592,479,940],
    [352,342,300],
    [466,668,158],
    [542,29,236],
    [431,825,988],
    [739,650,466],
    [52,470,668],
    [216,146,977],
    [819,987,18],
    [117,168,530],
    [805,96,715],
    [346,949,466],
    [970,615,88],
    [941,993,340],
    [862,61,35],
    [984,92,344],
    [425,690,689]]

junction_boxes = []
with open("2025/additional_files/junction_boxes.txt", "r") as f:
    for line in f:
        junction_boxes.append([int(e) for e in line.split(',')])

# print(junction_boxes[0:10])

# join circuits if there is common junction box
def update_circuits_join_intersecting_circuits(circuits):   
    for ind, cir in enumerate(circuits):
        if ind < len(circuits)-1:
            for cir2 in circuits[ind+1:]:
                if set(cir).intersection(set(cir2)) != set():
                    joined_circuits = set(cir).union(set(cir2))
                    circuits[ind] = list(joined_circuits)
                    circuits.remove(cir2)
                else:
                    pass
    return circuits

# connect boxes as close together as possible, create circuits
def connect_boxes_to_circuits(box_1,box_2, circuits):
    if len(circuits) == 0: # no existing circuits
        circuits.append([box_1,box_2])
        # print(circuits)
    elif len(circuits) > 0: # check if pair of boxes are connected in other circuits 
        is_added_box_to_any_circuit = False
        for cir in circuits:
            if any(box_1 == x for x in cir) and all(box_2 != x for x in cir): 
                cir.append(box_2)
                is_added_box_to_any_circuit = True
            elif any(box_2 == x for x in cir) and all(box_1 != x for x in cir): 
                cir.append(box_1)
                is_added_box_to_any_circuit = True
            elif any(box_1 == x for x in cir) and any(box_2 == x for x in cir):
                is_added_box_to_any_circuit = True
        else: # add new circuit
            if is_added_box_to_any_circuit == False: 
                circuits.append([box_1,box_2])
        if are_any_circuits_intersecting(circuits):
            circuits = update_circuits_join_intersecting_circuits(circuits)
    return circuits

def are_any_circuits_intersecting(circuits):
    list_of_all_points = list(itertools.chain(*circuits))
    set_of_all_points = set(list_of_all_points)
    if len(list_of_all_points) == len(set_of_all_points):
        return False
    else:
        return True

list_of_boxes_combination = list(itertools.combinations(junction_boxes, 2))

# distance calculation
distances_with_coords = []
for pair in list_of_boxes_combination:
    distances_with_coords.append([math.dist(pair[0],pair[1]), tuple(pair[0]),tuple(pair[1])]) # converting coords list to tuple (for later usage in sets)

# connecting boxes to circuit(s)
circuits = []
sorted_dist = sorted(distances_with_coords)
is_added_box_to_any_circuit = False
for dist_n_coords in sorted_dist[0:1000]:
    circuits = connect_boxes_to_circuits(dist_n_coords[1],dist_n_coords[2], circuits)

# add single junction boxes (as separate circuits)
# for box in junction_boxes:
#     if all(tuple(box) != x for x in list(itertools.chain.from_iterable(circuits))):
#         circuits.append(box)

# what do you get if you multiply together the sizes of the three largest circuits?
three_largest_circuits = sorted([len(x) for x in circuits],reverse=True)[0:3]
product = numpy.prod(three_largest_circuits)
print(product)

# Part 2