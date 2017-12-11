# Advent 5

with open('advent5.in', 'r') as f:
    inp = f.readlines()

inst = [int(x.replace("\n", "")) for x in inp]

curr_pos = 0
step = 0
while 0 <= curr_pos < len(inst):
    prev_pos = curr_pos
    curr_pos += inst[prev_pos]
    # Part 2
    if inst[prev_pos] >= 3:
        inst[prev_pos] -= 1
    else:
        inst[prev_pos] += 1 #Part 1
    step += 1
print "step"
print step

