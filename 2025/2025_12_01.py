import math

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
    
def dail_ends_at_zero(rotations, distances, starting_point):
    modulo_point = starting_point
    zero_counter = 0 
    for i in range(len(rot)):
        point = modulo_point + rotation_to_plus_minus(rot[i],dist[i])
        # dialing is in range 0-100, lets use modulo to keep range
        modulo_point = point % 100
        if modulo_point == 0:
            zero_counter += 1
    return zero_counter
    
print (f'Number of dials ending at zero: {dail_ends_at_zero(rot, dist, 50)}')


# Part 2

# any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one

modulo_point = 50
clicks_at_zero = 0 
for i in range(len(rot)):
    point = modulo_point + rotation_to_plus_minus(rot[i],dist[i])
    if point == 0:
        clicks_at_zero += 1
    elif point % 100 == 0:
        clicks_at_zero = math.trunc(dist[i]/100) + 1 
    elif point < 0 or point > 100:
        clicks_at_zero += round(modulo_point + dist[i] / 100) 
    modulo_point = point % 100

    
        
print(clicks_at_zero)
# 6775 too low
# 10396 too high