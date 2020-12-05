#!/usr/bin/env python3

MAX_ROW = 128
MAX_COL = 8

def parse_input(filename = "input"):
    with open(filename, "r") as f:
        data = [line.rstrip() for line in f.readlines()]
    return data

def solve(data):

    tbl = str.maketrans( {'F':'0', 'B':'1', 'L':'0', 'R':'1'} )

    seats = [[0 for _ in range(MAX_COL)] for _ in range(MAX_ROW)]

    for line in data:
        row = line[:7:]
        col = line[7:]
        col = int(col.translate(tbl), 2)
        row = int(row.translate(tbl), 2)
        seats[row][col] = 1
    
    possible_seats = [
        [1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1],
    ]

    seats_id = []
    for ix, layout in enumerate(possible_seats, 1):
        try:
            seats_id.append( seats.index(layout) * 8 + ix )
        except ValueError:
            continue
    
    return seats_id

if __name__ == "__main__":
    data = parse_input()
    max_id = solve(data)
    print('Answer:', max_id)