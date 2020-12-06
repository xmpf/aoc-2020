#!/usr/bin/env python

from functools import reduce

def parse_input(filename = "input"):
    with open(filename, "r") as f:
        data = f.read()
    data = data.split("\n\n")
    return data

def count_answers(data):
    answers = 0
    for group in data:
        subgroups = group.split("\n")
        common = reduce(lambda x, y: set(x).intersection(y), subgroups[1:], subgroups[0])
        answers += len(common)
    return answers

if __name__ == "__main__":
    data = parse_input()
    ans = count_answers(data)
    print('Answer:', ans)