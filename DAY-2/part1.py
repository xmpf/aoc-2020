#!/usr/bin/env python3

import re

def verify(entry):
    # regex: <low>-<high> <char>: <string>
    regex = re.compile(r'(\d+)\-(\d+) ([a-z]): (.*)')

    try:
        matched = regex.findall(entry)
        (low, high, char, password) = matched[0]
    except ValueError:
        print('Error: ', matched)
        return 0
    
    return int(low) <= (password.count(char)) <= int(high)



if __name__ == '__main__':

    # load input
    with open("input", "r") as f:
        data = [ line.rstrip() for line in f.readlines() ]
    
    total = 0
    # process data
    for line in data:
        total += int(verify(line))
    
    print(f'Total: {total}')