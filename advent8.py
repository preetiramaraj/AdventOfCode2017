# us dict to store esch register and chnge values, while you go through each instruction keep track of max number encountered until then.
from collections import defaultdict


def fn(op, x, y, reg):
    return {
        '>=': (reg[x] >= y),
        '<=': (reg[x] <= y),
        '!=': (reg[x] != y),
        '==': (reg[x] == y),
        '>': (reg[x] > y),
        '<': (reg[x] < y)
    }[op]


def main():
    with open('advent8.in', 'r') as f:
        inp = f.readlines()

    inst = [(x.replace("\n", "")).split("if") for x in inp]
    print inst
    print (inst[0][0]).strip().split(" ")
    print (inst[0][1]).strip().split(" ")
    reg = defaultdict(lambda: 0)
    for i, row in enumerate(inst):
        action = inst[i][0].strip().split(" ")
        condition = inst[i][1].strip().split(" ")
        if fn(condition[1], condition[0], int(condition[2]), reg):
            if action[1] == 'inc':
                reg[action[0]] += int(action[2])
            else:
                reg[action[0]] -= int(action[2])
    max_val = max([value for key, value in reg.items()])
    print max_val

main()
