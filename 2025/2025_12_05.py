import itertools
import numpy

# Part 1
# input
# fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs

fresh_ranges = []
fresh_ranges_raw = [
    '3-5',
    '10-14',
    '16-20',
    '12-18']
for ranges in fresh_ranges_raw:
    fresh_ranges.append([float(x) for x in ranges.split('-') ])

available_ingrediend_ids = [
    1,
    5,
    8,
    11,
    17,
    32]

# How many of the available ingredient IDs are fresh?
fresh_ranges = []
available_ingrediend_ids = []
after_black_line = False
with open("2025/additional_files/inventory_management_system_ingredients.txt", "r") as f:
    for line in f:
        if line.rstrip() == '':
            after_black_line = True
            continue
        elif after_black_line == False:
            fresh_ranges.append([float(x) for x in line.rstrip().split('-')])
        elif after_black_line == True:
            available_ingrediend_ids.append(int(line.rstrip()))

sorted_fresh_ranges = sorted(fresh_ranges)

def is_ingredient_fresh(ingredient,fresh_ranges):
    for range in fresh_ranges: 
        if (ingredient >= range[0]) and (ingredient <= range[1]):
            return True
    else:
        return False

counter = 0
for id in available_ingrediend_ids:
    if is_ingredient_fresh(id, sorted_fresh_ranges):
        counter += 1

print(f'number of spoiled ingredients: {counter}')

# Part 2
# How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges

def union_intersecting_ranges_from_index(fresh_ranges,i):
    intersecting_lists = []
    for range1, range2 in itertools.zip_longest(fresh_ranges[i:-1],fresh_ranges[i+1:]):
        if range1[1] >= range2[0] or range1[1] >= range2[1]: # range1 and range2 have intersect - add to intersecting_lists
            intersecting_lists.extend(range1)
            intersecting_lists.extend(range2)
            index = fresh_ranges.index(range2)
        elif range1[1] < range2[0] and fresh_ranges.index(range1) == 0: # first range has no intersection - return range1, update index
            intersecting_lists = range1
            index = fresh_ranges.index(range2)
            break
        elif range1[1] < range2[0] and intersecting_lists == []: # range1 and range2 have no intersect and no intersection before range1 - return range1, update index
            intersecting_lists = range1
            index = fresh_ranges.index(range2)
            break
        else: # range1 and range2 have no intersect but range1 has intersection before - just update index
            index = fresh_ranges.index(range2)
            break
    count_ids = (max(intersecting_lists) - min(intersecting_lists) + 1) 
    return [count_ids, index]

count_ids = 0
i = 0
while i < len(fresh_ranges)-1:
    result = union_intersecting_ranges_from_index(sorted_fresh_ranges, i)
    count_ids += result[0]
    i = result[1]

print(f'number of fresh ingredient IDs: {count_ids}')
