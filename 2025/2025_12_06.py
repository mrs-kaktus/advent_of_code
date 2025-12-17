import numpy as np
import itertools as it

# Part 1

# example = [
#     [123, 328, 51, 64],
#     [45, 64, 387, 23],
#     [6, 98, 215, 314],
#     ['*',   '+',   '*',   '+']  
# ]

numbers = []
operators = []
with open("2025/additional_files/cephalopod_math_homework.txt", "r") as f:
    for line in f:
        if '+' in line:
            operators = line.split()
        else:
            numbers.append([int(e) for e in line.strip().split()])

transposed_numbers = list(map(list, zip(*numbers)))

def solve_problem(operator,numbers):
    if operator == '+':
        return sum(numbers)
    elif operator == '*':
        return int(np.prod(numbers))

grand_total = 0
for operator, numbers in it.zip_longest(operators,transposed_numbers):
    grand_total += solve_problem(operator,numbers)

print(f'grand total of solved problems: {grand_total}')

# Part 2

# example = [
#     '123 328  51 64 ',
#     ' 45 64  387 23 ',
#     '  6 98  215 314',
#     '*   +   *   +  '
# ]

numbers_str = []
operators = []
with open("2025/additional_files/cephalopod_math_homework.txt", "r") as f:
    for line in f:
        if '+' in line:
            operators = list(reversed(line.split()))
        else:
            numbers_str.append((' ' + line).rstrip()[::-1]) # removing whitespace at the end of string; the reverse string and add white space at beginning (to recognise end of problem) 

def read_number_in_column(numbers_str):
    numbers = []
    temp_list_of_numbers = []
    for n1, n2, n3, n4 in zip(numbers_str[0], numbers_str[1], numbers_str[2], numbers_str[3]):
        if (n1 + n2 + n3 + n4).strip().isdigit():
            temp_list_of_numbers.append(int(n1 + n2 + n3 + n4))
        else:
            numbers.append(temp_list_of_numbers)
            temp_list_of_numbers = []
    return numbers

numbers_from_column = read_number_in_column(numbers_str)

grand_total = 0
for operator, numbers in it.zip_longest(operators, numbers_from_column):
    grand_total += solve_problem(operator,numbers)

print(f'grand total of solved problems: {grand_total}')
