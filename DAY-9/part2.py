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

def solve(data, invalid_num):
    for i, _ in enumerate(data):
        total = 0
        for j, y in enumerate(data[i:], i + 1):
            total += y
            if total > invalid_num:
                break
            elif total == invalid_num:
                sliced = data[i:j]
                return (min(sliced), max(sliced))
    return (None, None)

if __name__ == "__main__":
    data = parse_data("input")
    invalid_num = find_invalid(data)
    mini, maxi = solve(data, invalid_num)
    print( f'{mini} + {maxi} = {mini + maxi}' )