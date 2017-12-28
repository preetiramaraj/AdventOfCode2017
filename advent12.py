#Advent 12


def find_indirect_connections(z, conn, contains_zero):
    curr_list = []
    for y in z:
        curr_list += [x for x in conn.keys() if y in conn[x] and [True for z in contains_zero if x in z] != [True]]
   # print z, curr_list
    if len(curr_list) == 0:
        return ['-1']
    else:
        return list(set(curr_list))


def main():
    with open('advent12.in', 'r') as f:
        inp = f.readlines()

    input = [x.replace("\n", "").split("<->") for x in inp]
    conn = {}
    contains_zero = [['0'], []]
    for i, val in enumerate(input):
        curr_key = val[0].replace(" ", "")
        curr_values = [x.replace(" ", "") for x in val[1].split(", ")]
        if '0' in curr_values:
            contains_zero[1].append(curr_key)
        conn[curr_key] = curr_values

    i = 1
    new_conn = []
    while new_conn != ['-1']:
        new_conn = find_indirect_connections(contains_zero[i], conn, contains_zero)
        contains_zero.append(new_conn)
        i = i+1
    contains_zero.remove(['-1'])
    print len([x for sublist in contains_zero for x in sublist])


main()