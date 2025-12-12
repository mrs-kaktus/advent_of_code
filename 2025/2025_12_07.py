# Part 1

tachyon_manifold = [
    '.......S.......',
    '...............',
    '.......^.......',
    '...............',
    '......^.^......',
    '...............',
    '.....^.^.^.....',
    '...............',
    '....^.^...^....',
    '...............',
    '...^.^...^.^...',
    '...............',
    '..^...^.....^..',
    '...............',
    '.^.^.^.^.^...^.',
    '...............'
]

tachyon_manifold = []
with open("2025/additional_files/tachyon_manifold.txt", "r") as f:
    for line in f:
        tachyon_manifold.append(line.rstrip())


def find_splitter(str):
    return [i for i, letter in enumerate(str) if letter == '^']

def split_beam(beams_pos, splitters_pos):
    new_beams = []
    split_counter = 0
    for beam in beams_pos:
        for splitter in splitters_pos:
            if beam == splitter:
                new_beams.extend([splitter - 1, splitter + 1])
                split_counter += 1
                break
            else:
                continue
        else: # if beam is not splitted, it continues 
            new_beams.extend([beam])
    new_beams_pos = list(set(new_beams)) # remove duplicities
    return [new_beams_pos, split_counter]


beams_pos = [tachyon_manifold[0].index('S')]
split_counter = 0
for line in tachyon_manifold[1:]:
    splitters_pos = find_splitter(line)
    if splitters_pos != []:
        result = split_beam(beams_pos,splitters_pos)
        beams_pos = result[0]
        split_counter += result[1]
    else:
        continue

print(split_counter)
# 1259 too low