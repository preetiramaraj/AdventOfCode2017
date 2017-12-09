
# Advent 3
# 2-9 (9-1),10-25(25-9),26-49(49-25)25,36
# each square size is 1^2,3^2,5^2,7^2,9^2
# take 10-25: 5^2, max manhattan dist = 4 (5-1)
# 10 is 3 steps away, 11 is 2 steps away, 12 is 3 steps away,13 is 4 steps away
# 10+1,10+1+4,10+1+4+4,10+1+4+4+4 are all 2 steps away
# 10, 10+2,10+2+2,10+2+2+2..10+2*7 are 3 steps away
# 10+3,13 + 4, 17+4, 21+ 4 are all four steps away
# 13 is farthest with 4 steps,each square closer to the center is one step closer


# 1+8 (3^2), 1+8+8*2 = 1+8(3)(5^2), 1+8+8*2+8*3 = 1+8(1+2+3), 1+8(1+2+3+4)
xmax = 0
n = 0
square_side = 1
x = 347991
while xmax < x:
    xmax = ((n * (n + 1) / 2) * 8) + 1
    n += 1
    square_side += 2

nmin = n - 2
xmin = (((nmin * (nmin + 1) / 2) * 8) + 1) + 1
print "xmin:", xmin
print "xmax: ", xmax
square_side -= 2  # Max number of numbers on that side. 2+3-2, 10+5-2
print "square_side: ", square_side
top_right = (xmin + square_side - 2)
top_left = top_right + square_side - 1
bottom_left = top_left + square_side - 1
bottom_right = bottom_left + square_side - 1
print "top-right: ", top_right, " top-left: ", top_left, " bottom-left: ", bottom_left, " bottom-right: ", bottom_right

result = -1
# now find which row/column it exists on
if x == top_right or x == top_left or x == bottom_right or x == bottom_left:
    result = (square_side - 1)
elif x < top_right:
    xmax = top_right
elif top_right < x < top_left:
    xmax = top_left
    xmin = top_right
elif top_left < x < bottom_left:
    xmax = bottom_left
    xmin = top_left
elif bottom_left < x < bottom_right:
    xmax = bottom_right
    xmin = bottom_left

# Updated xmax and xmin
if result == -1:
    print "Updated: ", xmin, "-", xmax
    center_min = (xmax - (square_side / 2))
    print "Center value whose distance from 1 is ", (square_side / 2), "is ",center_min
    print "Max possible manhattan distance: ", (square_side-1)
    print "x-distance = ", abs(x-center_min) + (square_side/2)
else:
    print "x-distance = ", result