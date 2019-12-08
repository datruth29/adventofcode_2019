import os

DATADIR = os.path.dirname(os.path.realpath(__file__))
DATAFILE = os.path.join(DATADIR, 'day2.txt')


def process_file(filename):
    with open(filename) as f:
        data = list(map(int, f.read().split(",")))
    return data


if x == 1:
    