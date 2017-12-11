# Advent 5

with open('advent5.in', 'r') as f:
    inp = f.readlines()

inst = [int(x.replace("\n", "")) for x in inp]

curr_pos = 0
step = 0
while curr_pos < len(inst):
    prev_pos = curr_pos
    curr_pos += inst[prev_pos]
    inst[prev_pos] += 1
    step += 1

print step
