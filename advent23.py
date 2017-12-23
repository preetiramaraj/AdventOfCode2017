# Advent 23


def fn(op, x, y, reg):
    try:
        val = int(y)
    except ValueError:
        val = reg[y]

    if x.isalpha():
        val_x = reg[x]
    else:
        val_x = int(x)

    if op == 'set':
        reg[x] = val
    elif op == 'sub':
        reg[x] -= val
    elif op == 'mul':
        reg[x] *= val
    elif op == 'jnz' and val_x != 0:
        return ['jnz', str(val)]
    return ['xxx']


def main():
    with open('advent23.in', 'r') as f:
        inp = f.readlines()

    input = [x.replace("\n", "").split(" ") for x in inp]
    i = 0
    num_muls = 0
    reg = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
    while i < len(input):
        now_inst = input[i]
        if now_inst[0] == 'mul':
            num_muls += 1
        value_list = fn(now_inst[0], now_inst[1], now_inst[2], reg)
        if value_list[0] == 'xxx':
            i += 1
        elif value_list[0] == 'jnz':
            i += int(value_list[1])
    print num_muls


main()
