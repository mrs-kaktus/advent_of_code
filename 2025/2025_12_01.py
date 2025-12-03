#  Part 1
# example
f = ['L68',
    'L30',
    'R48',
    'L5 ',
    'R60',
    'L55',
    'L1 ',
    'L99',
    'R14',
    'L82']

rot = []
dist= []
with open("2025/additional_files/document_to_safe.txt", "r") as f:
    for line in f:
        rot.append(line[0])
        dist.append(int(line[1:len(line)]))

# count dial points at 0
# starting point at 50
# left rotation - dia to lower numbers (operator -) ; right rotation - dia to higher numbers (operator +)

def rotation_to_plus_minus(rotation, distance):
    if rotation == 'L':
        return  -distance
    elif rotation == 'R':
        return distance
    else:
        return KeyError
    
def dial_ends_at_zero(rotations, distances, starting_point):
    zero_counter = 0 
    for i in range(len(rot)):
        point = starting_point + rotation_to_plus_minus(rot[i],dist[i])
        # dialing is in range 0-100, lets use modulo to keep range
        starting_point = point % 100
        if starting_point == 0:
            zero_counter += 1
    return zero_counter
    
print(f'Number of dials ending at zero: {dial_ends_at_zero(rot, dist, 50)}')

# Part 2

# any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one

starting_point = 50
clicks_at_zero = 0 
for i in range(len(rot)):
    # number of cycles (dialing is more then one cycle aka 100 clicks)
    cycles = dist[i] // 100
    # what left after cycles
    remainder = dist[i] % 100 
    # special case when starting point is zero
    if starting_point == 0:
        clicks_at_zero += cycles
    else:
        # number of clicks at zero = number of cycles + 0 (because (starting_point + remainder) is less then one cycle)
        if (rotation_to_plus_minus(rot[i],dist[i]) < 0 and starting_point - remainder > 0) or (rotation_to_plus_minus(rot[i],dist[i]) > 0 and starting_point + remainder < 100):
            clicks_at_zero += cycles
        # number of clicks at zero = number of cycles + 1 (because (starting_point + remainder) is more then one cycle) 
        elif (rotation_to_plus_minus(rot[i],dist[i]) < 0 and starting_point - remainder <= 0) or (rotation_to_plus_minus(rot[i],dist[i]) > 0 and starting_point + remainder >= 100):
            clicks_at_zero += cycles + 1
    # update starting point
    point = starting_point + rotation_to_plus_minus(rot[i],dist[i])
    starting_point = point % 100
        
print(f'Number of dials ending at zero: {clicks_at_zero}')
