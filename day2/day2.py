import os


def calculate_val1(input_data, noun, verb):
    # deep copy because python list is mutable
    data = input_data[::]

    # before running the program, replace position 1 with the value 12 and replace position 2 with the value 2
    data[1] = noun
    data[2] = verb
    length = len(data)

    for i in range(0, len(data), 4):
        opcode, x, y, position = data[i:i + 4]

        if x > length or y > length or position > length:
            continue
        if opcode == 1:
            data[position] = data[x] + data[y]
        elif opcode == 2:
            data[position] = data[x] * data[y]
        elif opcode == 99:
            break
    return data[0]


def calculate_val2(data):
    for noun in range(100):
        for verb in range(100):
            if calculate_val1(data, noun, verb) == 19690720:
                return 100 * noun + verb


filename = os.getcwd() + '/data/task.txt'
with open(filename, 'r') as file:
    raw_data = file.read()
    data = list(map(int, raw_data.split(',')))

    print('What value is left at position 0:', calculate_val1(data, 12, 2))
    print('What is 100 * noun + verb:', calculate_val2(data))
