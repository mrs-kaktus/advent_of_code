import numpy as np

# Part 1

# example = [
#     'aaa: you hhh',
#     'you: bbb ccc',
#     'bbb: ddd eee',
#     'ccc: ddd eee fff',
#     'ddd: ggg',
#     'eee: out',
#     'fff: out',
#     'ggg: out',
#     'hhh: ccc fff iii',
#     'iii: out'
# ]
# machine_names = []
# communication = []
# for line in example:
#     machine_names.append(line.split(':')[0])
#     communication.append(line.replace(':','').split())
# machine_names.append('out')

machine_names = []
communication = []
with open("2025/additional_files/machines_n_outputs.txt", "r") as f:
    for line in f:
        machine_names.append(line.split(':')[0])
        communication.append(line.replace(':','').split())
machine_names.append('out')

matrix = []
for output_machines in communication:
    m = [0]*len(machine_names)
    for output_machine in output_machines[1:]:
        index = machine_names.index(output_machine)
        m[index] = 1
    matrix.append(m)
matrix.append([0]*len(machine_names))

input = [0]*len(machine_names)
input[machine_names.index('you')] = 1
input = np.transpose(input)

counter = 0
while any(i != 0 for i in input):
    input = np.matmul(input,matrix)
    counter += input[-1] 
print(f'number of paths: {counter}')


# Part 2

# example = [
#     'svr: aaa bbb',
#     'aaa: fft',
#     'fft: ccc',
#     'bbb: tty',
#     'tty: ccc',
#     'ccc: ddd eee',
#     'ddd: hub',
#     'hub: fff',
#     'eee: dac',
#     'dac: fff',
#     'fff: ggg hhh',
#     'ggg: out',
#     'hhh: out'
# ]

# machine_names = []
# communication = []
# for line in example:
#     machine_names.append(line.split(':')[0])
#     communication.append(line.replace(':','').split())
# machine_names.append('out')

# matrix = []
# for output_machines in communication:
#     m = [0]*len(machine_names)
#     for output_machine in output_machines[1:]:
#         index = machine_names.index(output_machine)
#         m[index] = 1
#     matrix.append(m)
# matrix.append([0]*len(machine_names))


# from svr to out
input = [0]*len(machine_names)
input[machine_names.index('svr')] = 1
input = np.transpose(input)

counter = 0
ind = machine_names.index('out')
while any(i != 0 for i in input):
    input = np.matmul(input,matrix)
    counter += input[ind]
print('from svr to out')
print(counter)


#  from srv to fft
input = [0]*len(machine_names)
input[machine_names.index('svr')] = 1
input = np.transpose(input)

counter = 0
ind = machine_names.index('fft')
while any(i != 0 for i in input):
    input = np.matmul(input,matrix)
    counter += input[ind]
print('from svr to fft')
print(counter)
from_svr_to_fft = counter

# from fft to dac
input = [0]*len(machine_names)
input[machine_names.index('fft')] = 1
input = np.transpose(input)

counter = 0
ind = machine_names.index('dac')
while any(i != 0 for i in input):
    input = np.matmul(input,matrix)
    counter += input[ind]
print('from fft to dac')
print(counter)
from_fft_to_dac = counter

# from dac to out
input = [0]*len(machine_names)
input[machine_names.index('dac')] = 1
input = np.transpose(input)

counter = 0
ind = machine_names.index('out')
while any(i != 0 for i in input):
    input = np.matmul(input,matrix)
    counter += input[ind]
print('from dac to out')
print(counter)
from_dac_to_out = counter

result = from_svr_to_fft * from_fft_to_dac * from_dac_to_out
print(result)