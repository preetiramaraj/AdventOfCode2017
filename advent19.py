# Advent 19
import numpy as np


def isValid(dir, x, y, max_x, max_y, inst):
    if (dir == 'up' and x == 0) or (dir == 'down' and x == max_x-1) or (dir == 'left' and y == 0) or\
            (dir == 'right' and y == max_y-1):
        return False
    if (dir == 'down' and inst[x+1][y] == ' ') or (dir == 'up' and inst[x-1][y] == ' ')\
            or (dir == 'left' and inst[x][y-1] == ' ') or (dir == 'right' and inst[x][y+1] == ' '):
        return False
    return dict(down=(x+1, y), up=(x - 1, y), right=(x, y + 1), left=(x, y - 1))[dir]


def getNextValid(x, y, max_x, max_y, traversed):
    if x > 0 and traversed[x-1][y] == 1:
        dir = 'up'
    elif x < max_x - 1 and traversed[x+1][y] == 1:
        dir = 'down'
    elif y > 0 and traversed[x][y-1] == 1:
        dir = 'left'
    elif y < max_y - 1 and traversed[x][y+1] == 1:
        dir = 'right'
    else:
        return 'none'
    return dir


def main():
    with open('advent19.in', 'r') as f:
        inp = f.readlines()

    inst = [x.replace("\n", "") for x in inp]
    max_y = max([len(x) for x in inst])
    inst = [x.ljust(max_y) for x in inst]
    yi = [inst[0].index(x) for x in inst[0] if x != ' '][0]
    xi = 0

    traversed = np.zeros((len(inst), max_y))
    for j in range(0, len(inst)):
        for i in range(0, len(inst[j])):
            if inst[j][i] != ' ':
                traversed[j][i] = 1

    letters = ''
    steps = 0
    direction = 'down'
    while 0 <= xi < len(inst) and 0 <= yi < max_y:
            if inst[xi][yi].isalpha():
                letters += inst[xi][yi]
            traversed[xi][yi] = 2
            value = isValid(direction, xi, yi, len(inst), max_y, inst)
            if not value:
                direction = getNextValid(xi, yi, len(inst), max_y, traversed)
                if direction == 'none':
                    break
            else:
                xi, yi = value
                steps += 1
    print letters
    print steps


main()
