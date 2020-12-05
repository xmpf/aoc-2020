#!/usr/bin/env python3

def parse_input(filename = "input"):
    with open(filename, "r") as f:
        data = [line.rstrip() for line in f.readlines()]
    return data

def solve(data):

    tbl = str.maketrans( {'F':'0', 'B':'1', 'L':'0', 'R':'1'} )

    max_id = 0
    for line in data:
        row = line[:7:]
        col = line[7:]
        col = int(col.translate(tbl), 2)
        row = int(row.translate(tbl), 2)
        
        curr_id = row * 8 + col
        max_id = curr_id if max_id < curr_id else max_id
    
    return max_id

if __name__ == "__main__":
    data = parse_input()
    max_id = solve(data)
    print('Maximum seat ID:', max_id)