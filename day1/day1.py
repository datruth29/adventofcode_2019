import os
import math

DATADIR = os.path.dirname(os.path.realpath(__file__))
DATAFILE = os.path.join(DATADIR, 'day1.txt')


def process_file(filename):
    with open(filename) as f:
        data = f.readlines()
    return data


def calculate_fuel(mass):
    return math.floor(mass / 3) - 2


def calculate_module(mass):
    result = []
    while (mass > 0):
        mass = calculate_fuel(mass)
        if mass > 0:
            result.append(mass)
    return sum(result)


data = process_file(DATAFILE)
result = sum(map(calculate_module, data))
print(result)
