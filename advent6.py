# Advent 6

inp = "2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14"

blocks = [int(x) for x in inp.split("\t")]

str_list = [' '.join([str(x) for x in blocks])]
curr = ''
steps = 0
while curr not in str_list:
    str_list.append(curr)
    index = blocks.index(max(blocks))
    value = blocks[index]
    blocks[index] = 0
    while value > 0:
        index += 1
        blocks[(index % len(blocks))] += 1
        value -= 1
    curr = ' '.join([str(x) for x in blocks])
    steps += 1
print steps
