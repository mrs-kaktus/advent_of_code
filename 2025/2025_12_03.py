# Part 1
batteries =[ 
    '987654321111111',
    '811111111111119',
    '234234234234278',
    '818181911112111']

batteries = []
with open("2025/additional_files/batteries_with_joltage.txt", "r") as f:
    for line in f:
        batteries.append(line.rstrip())

# turn on 2 batteries in each line with maximal joltage
batteries_joltage= []
for line in batteries:
    battery1 = max(line[:-1])
    baterry1_index = line.find(battery1)
    battery2 = max(line[baterry1_index + 1:])
    batteries_joltage.append(int(battery1 + battery2)) 

print(f'total similarity score: {sum(batteries_joltage)}')

# Part 2
# turn on 12 batteries in each line with maximal joltage
