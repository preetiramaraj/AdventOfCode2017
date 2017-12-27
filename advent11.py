#Advent 11


def nextCoordinate(dir, x, y, z):
    if dir == "n":
        y += 1
        z -= 1
    elif dir == "s":
        y -= 1
        z += 1
    elif dir == "ne":
        x += 1
        z -= 1
    elif dir == "sw":
        x -= 1
        z += 1
    elif dir == 'nw':
        x -= 1
        y += 1
    elif dir == "se":
        x += 1
        y -= 1

    return x, y, z


def main():
    with open('advent11.in', 'r') as f:
        inp = f.readlines()
    input = inp[0].split(',')
    x = 0
    y = 0
    z = 0
    for i, val in enumerate(input):
        x, y, z = nextCoordinate(val, x, y, z)
    distance = (abs(x) + abs(y) + abs(z))/2
    print "Manhattan distance = ", distance

main()
