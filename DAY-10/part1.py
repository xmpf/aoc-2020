#!/usr/bin/env python3

def parse_data(filename = 'input'):
    with open(filename, 'r') as f:
        data = list(map(int, f.readlines()))
    return data

if __name__ == "__main__":
    data = parse_data()
    data_sorted = sorted(data)
    differences = [0, 1, 0, 1]
    
    x = data_sorted[0]
    for y in data_sorted[1:]:
        diff = y - x
        x = y
        differences[diff] += 1
    
    print( differences[1] * differences[3] )