# Advent 18
from collections import defaultdict


def fn(op, x, y, reg, last_played):
    try:
        val = int(y)
    except ValueError:
        val = reg[y]

    if op == 'snd':
        last_played = (reg[x])
        return [last_played]
    elif op == 'set':
        reg[x] = val
    elif op == 'add':
        reg[x] += val
    elif op == 'mul':
        reg[x] *= val
    elif op == 'mod':
        reg[x] %= val
    elif op == 'rcv' and reg[x] != 0:
        return ['rcv', last_played]
    elif op == 'jgz' and reg[x] > 0:
        return ['jgz', str(val)]
    return ['xxx']


def main():
    with open('advent18.in', 'r') as f:
        inp = f.readlines()

    input = [x.replace("\n", "").split(" ") for x in inp]
    i = 0
    last_played = -999999999999999
    reg = defaultdict(lambda: 0)
    while i < len(input):
        value_list = []
        now_inst = input[i]
        if len(now_inst) > 2:
            value_list = fn(now_inst[0], now_inst[1], now_inst[2], reg, last_played)
        else:
            value_list = fn(now_inst[0], now_inst[1], '-999' , reg, last_played)
        if value_list[0] == 'xxx':
            i += 1
        elif value_list[0] == 'rcv':
            last_played = value_list[1]
            break
        elif value_list[0] == 'jgz':
            i += int(value_list[1])
        else:
            last_played = value_list[0]
            i += 1
    print last_played

main()