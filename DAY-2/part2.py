#!/usr/bin/env python3

import re

def verify(entry):
    # regex: <low>-<high> <char>: <string>
    regex = re.compile(r'(\d+)\-(\d+) ([a-z]): (.*)')

    try:
        matched = regex.findall(entry)
        (ix, idx, char, password) = matched[0]
    except ValueError:
        print('Error: ', matched)
        return 0
    
    ix  = int(ix) -  1
    idx = int(idx) - 1

    not_same = not( password[ix] == password[idx] )
    return not_same and (password[ix] == char or password[idx] == char)



if __name__ == '__main__':

    # load input
    with open("input", "r") as f:
        data = [ line.rstrip() for line in f.readlines() ]
    
    total = 0
    # process data
    for line in data:
        total += int(verify(line))
    
    print(f'Total: {total}')