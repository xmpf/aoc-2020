#!/usr/bin/env python

from collections import defaultdict

def parse_input(filename = "input"):
    with open(filename, "r") as f:
        memory = [ line.rstrip() for line in f.readlines() ]
    return memory

if __name__ == "__main__":
    PC  = 0
    ACC = 0
    MEM = []
    RUNNING = True

    SEEN = defaultdict(int)

    MEM = parse_input()
    while RUNNING:
        instruction = MEM[PC]
        opcode, number = instruction.split(' ')

        SEEN[PC] += 1
        if SEEN[PC] == 2:
            break

        if opcode == "jmp":
            PC += int(number)
            continue
        elif opcode == "acc":
            ACC += int(number)
        elif opcode == "nop":
            pass
        else:
            RUNNING = False
            break
        PC += 1

    print("ACC = ", ACC)