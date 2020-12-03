#!/usr/bin/env python3

from operator import mul
from functools import reduce

if __name__ == "__main__":
    # parse input
    data = [ line.rstrip() for line in open("input", "r").readlines() ]

    # initial values
    x = 0
    y = 0
    
    # corners
    width = len(data[0])
    height = len(data)

    moves = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1)
    ]
    totals = [ 0 for _ in moves ]
    print(totals)
    # processing
    ix = -1
    for dx, dy in moves:
        ix += 1
        x = dx
        y = dy
        while x < height:
            totals[ix] += int(data[x][y] == '#')
            x += dx
            y = (y + dy) % width


    print(totals)

    print('Total trees:', reduce(mul, totals))