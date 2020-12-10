#!/usr/bin/env python3

def parse_data(filename = 'input'):
    with open(filename, 'r') as f:
        data = [ int(i) for i in f.readlines() ]
    return data

def is_invalid(preamble, num):
    for x in preamble:
        for y in preamble[1:]:
            if x == y:
                continue
            elif x + y == num:
                return False
    return True

def find_invalid(data):
    for i, num in enumerate(data[25:]):
        preamble = data[i : i + 25]
        if is_invalid(preamble, num):
            return num
    return None


if __name__ == "__main__":
    data = parse_data()
    print( find_invalid(data) )
