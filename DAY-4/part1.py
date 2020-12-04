#!/usr/bin/env python3

def verify(entry):
    entry = entry.replace('\n', ' ')
    entry = entry.split(" ")
    if len(entry) < 7:
        return 0
    complete_set = {"byr", "eyr", "hgt", "pid", "hcl", "iyr", "ecl", "cid"}
    entry = set(map(lambda x: x.split(":")[0], entry))    
    return complete_set.difference(entry) <= {"cid"}

if __name__ == "__main__":
    
    with open("input", "r") as f:
        data = f.read()
    
    data = data.split("\n\n")

    total = 0
    for passport in data:
        total += int(verify(passport))

    print("Total:", total)