# Part 1
batteries =[ 
    '987654321111111',
    '811111111111119',
    '234234234234278',
    '818181911112111']

# batteries = []
# with open("2025/additional_files/batteries_with_joltage.txt", "r") as f:
#     for line in f:
#         batteries.append(line.rstrip())

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


def find_battery(line, start_index=0, end_index=len(line)):
    if end_index == 1:
    # if end_index == len(line)-12:
        battery = max(line[start_index:-end_index])
        start_index = line.find(battery)
        batteries_joltage.append(battery)
        return batteries_joltage, start_index
        extented_batteries_joltage.append(int(battery1 + battery2)) 
        # battery2 = max(line[start_index+1:i])
    else: 
        battery = max(line[start_index:-end_index])
        s_index = line.find(battery)
        # print(battery)
        # print(s_index)
        print(line[start_index:end_index])
        print(line[s_index:end_index-1])
        return batteries_joltage.append(battery) + find_battery(line, s_index, end_index-1)[0],find_battery(line, s_index, end_index-1)[1]
        # return battery 


for line in batteries:
    print(line)
    print(find_battery(line,0,12))


# extented_batteries_joltage = []
# for i in reversed(range(12)):
#     battery1 = max(line[:i])
#     baterry1_index = line.find(battery1)
#     battery2 = max(line[baterry1_index + 1:i])
#     extented_batteries_joltage.append(int(battery1 + battery2)) 

# def factorial(n):
#     if n == 0:  # Base case
#         return 1
#     else:       # Recursive case
#         return n * factorial(n - 1)

# print(factorial(5))