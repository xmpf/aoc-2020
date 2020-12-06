#!/usr/bin/env python

def parse_input(filename = "input"):
    with open(filename, "r") as f:
        data = f.read()
    data = data.split("\n\n")
    return data

def count_answers(data):
    answers = 0
    for group in data:
        answers += len(set(filter(lambda x: ord('a') <= ord(x) <= ord('z'), group)))
    return answers

if __name__ == "__main__":
    data = parse_input()
    ans = count_answers(data)
    print('Answer:', ans)