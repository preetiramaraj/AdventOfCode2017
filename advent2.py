# Advent 2

with open('advent2.in', 'r') as f:
    inp = f.readlines()
sum = 0
for i, l in enumerate(inp):
    lnew = l.replace("\n", "")
    lnew_arr = lnew.split("\t")
    lnew_arr_int = [int(x) for x in lnew_arr]
    # sum += max(lnew_arr_int) - min(lnew_arr_int)
    for j, k in enumerate(lnew_arr_int):
        for n, m in enumerate(lnew_arr_int):
            if j != n and k % m == 0:
                sum += (k / m)
                break
print sum
