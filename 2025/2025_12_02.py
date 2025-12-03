import textwrap
# Part 1

# str_ranges = ['11-22',
#               '95-115',
#               '998-1012',
#               '1188511880-1188511890',
#               '222220-222224',
#               '1698522-1698528',
#               '446443-446449',
#               '38593856-38593862',
#               '565653-565659',
#               '824824821-824824827',
#               '2121212118-2121212124']

with open("2025/additional_files/product_ids.txt", "r") as f:
    for line in f:
        str_ranges = line.split(',')

def is_invalid_id(str_id):
    if len(str_id)%2 == 0:
        id_parts = textwrap.wrap(str_id, len(str_id) // 2)
        if id_parts[0] == id_parts[1]:
            return True
        else:
            return False
    
def invalid_ids(int_range):
    list_of_invalid_ids = []
    for id in range(int_range[0], int_range[1] + 1):
        if is_invalid_id(str(id)):
            list_of_invalid_ids.append(id)
    return list_of_invalid_ids

int_ranges = []
# split each element in list according dash, and convert to integer
for e in str_ranges:
    int_ranges.append([int(i) for i in e.split('-')])

# check invalid id in ranges
list_of_invalid_ids = []
for int_range in int_ranges:
    list_of_invalid_ids.extend(invalid_ids(int_range))

print(f'Sum of invalid IDs: {sum(list_of_invalid_ids)}')

# Part 2

# adjustment: split string on 2 and more substrings (with equal lengths) 
def is_invalid_id_adjusted(str_id):
    # n - lenght of substring
    for n in range(1, len(str_id) // 2 + 1):
        id_parts = textwrap.wrap(str_id, n)
        if len(set(id_parts)) == 1:
            return True
    return False

# adjustment: switch using is_invalid_id to is_invalid_id_adjusted
def invalid_ids_adjusted(int_range):
    list_of_invalid_ids = []
    for id in range(int_range[0], int_range[1] + 1):
        if is_invalid_id_adjusted(str(id)):
            list_of_invalid_ids.append(id)
    return list_of_invalid_ids

# check invalid id in ranges (after adjustment)
list_of_invalid_ids_adj = []
for int_range in int_ranges:
    list_of_invalid_ids_adj.extend(invalid_ids_adjusted(int_range))

print(f'Sum of invalid IDs (after adjustment): {sum(list_of_invalid_ids)}')
