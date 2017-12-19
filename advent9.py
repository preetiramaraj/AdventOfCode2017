# Advent 9


def remove_cancelled(inp):
    while '!' in inp:
        index = inp.index('!')
        inp = inp[:index] + inp[index + 2:]
    return inp


def remove_garbage(inp):
    while '<' in inp:
        index = inp.index('<')
        index_g = inp.index('>')
        inp = inp[:index] + inp[index_g + 1:]
    return inp


def calculate_score(inp):
    cur_score = 0
    cur_char = 0
    total_score = 0
    while cur_char != len(inp):
        if inp[cur_char] == '{':
            cur_score += 1
            total_score += cur_score
        if inp[cur_char] == '}':
            cur_score -= 1
        cur_char += 1
    return total_score


def main():
    with open('advent9.in', 'r') as f:
        inp = f.readlines()

    new_inp = remove_cancelled(inp[0])
    no_garbage_inp = remove_garbage(new_inp)
    print calculate_score(no_garbage_inp)


main()
