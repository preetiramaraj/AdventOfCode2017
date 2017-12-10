# Advent 4

with open('advent4.in', 'r') as f:
    inp = f.readlines()

sum = 0
for i, l in enumerate(inp):
    dict = {}
    lnew = l.replace("\n", "")
    lnew_arr = lnew.split(" ")
    valid = True
    for x in lnew_arr:
        if x in dict:
            valid = False
            break
        else:
            dict[x] = 1
    if valid:
        sum += 1

print sum


