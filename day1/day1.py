import os
from math import floor


def calculate_fuel(mass):
    return floor(mass / 3) - 2


filename = os.getcwd() + '/data/task1.txt'

sum_fuel_1 = 0
with open(filename, 'r') as file:
    for line in file:
        line = int(line.rstrip())
        sum_fuel_1 += calculate_fuel(line)
print('Part1, What is the sum of the fuel requirements:', sum_fuel_1)

sum_fuel_2 = 0
with open(filename, 'r') as file:
    for line in file:
        line = int(line.rstrip())
        fuel = calculate_fuel(line)
        while fuel > 0:
            sum_fuel_2 += fuel
            fuel = calculate_fuel(fuel)
print('Part1, What is the sum of the fuel requirements:', sum_fuel_2)

