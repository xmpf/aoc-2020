#!/usr/bin/env python3

if __name__ == "__main__":
    # parse input
    data = [ line.rstrip() for line in open("input", "r").readlines() ]

    # initial values
    x = 1
    y = 3
    total = 0
    
    # corners
    width = len(data[0])
    height = len(data)

    # processing
    while x < height:
        total += int(data[x][y] == '#')
        x += 1
        y = (y + 3) % width

    print('Total trees:', total)