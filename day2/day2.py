import os

DATADIR = os.path.dirname(os.path.realpath(__file__))
DATAFILE = os.path.join(DATADIR, 'day2.txt')


def process_file(filename):
    with open(filename) as f:
        data = list(map(int, f.read().split(",")))
    return data


def generate(x, y, data):
    data[1] = x
    data[2] = y
    for i in range(0, len(data), 4):
        element = data[i]
        if element == 99:
            break
        if element == 1:
            first_pos = data[i+1]
            second_pos = data[i+2]
            third_pos = data[i+3]
            data[third_pos] = data[first_pos] + data[second_pos]
        if element == 2:
            first_pos = data[i+1]
            second_pos = data[i+2]
            third_pos = data[i+3]
            data[third_pos] = data[first_pos] * data[second_pos]

    return data[0]


data = process_file(DATAFILE)
print(generate(77, 33, data[:]))
print((100 * 77) + 33)
