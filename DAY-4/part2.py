#!/usr/bin/env python3

import re

def verify_values(entry):
    byr, iyr, eyr, hgt, hcl, ecl, pid = [False for _ in range(7)]

    byr = 1920 <= int(entry['byr']) <= 2002
    iyr = 2010 <= int(entry['iyr']) <= 2020
    eyr = 2020 <= int(entry['eyr']) <= 2030
    hgt = entry['hgt']

    if hgt[-2:] == "cm":
        hgt = 150 <= int(hgt[:-2]) <= 193
    elif hgt[-2:] == "in":
        hgt = 59 <= int(hgt[:-2]) <= 76
    else:
        return 0
    
    hcl = re.search(r'#[0-9a-f]{6}', entry['hcl'])
    ecl = entry['ecl'] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    pid = re.search(r'[0-9]{9}', entry['pid'])
    return all([byr, iyr, eyr, hgt, hcl, ecl, pid])

def verify(entry):
    entry = entry.replace('\n', ' ')
    entry = entry.split(" ")
    if len(entry) < 7:
        return 0
    complete_set = {"byr", "eyr", "hgt", "pid", "hcl", "iyr", "ecl", "cid"}
    try:
        entry = dict(map(lambda x: x.split(":"), entry))
    except ValueError:  # missing value
        return 0
    return (complete_set.difference(entry) <= {"cid"}) and verify_values(entry)

if __name__ == "__main__":
    
    with open("input", "r") as f:
        data = f.read()
    
    data = data.split("\n\n")

    total = 0
    for passport in data:
        total += int(verify(passport))

    print("Total:", total)