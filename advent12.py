#Advent 12


def find_indirect_connections(z, conn, contains_zero):
    curr_list = []
    curr_list += [x for x in conn.keys() if z in conn[x] and x not in contains_zero]
    if len(curr_list) == 0:
        return ['-1']
    else:
        return list(set(curr_list))


def main():
    with open('advent12.in', 'r') as f:
        inp = f.readlines()

    input = [x.replace("\n", "").split("<->") for x in inp]
    conn = {}
    for i, val in enumerate(input):
        curr_key = val[0].replace(" ", "")
        curr_values = [x.replace(" ", "") for x in val[1].split(", ")]
        conn[curr_key] = curr_values
    all_nodes = list(conn.keys())
    num_groups = 0
    while len(all_nodes) > 0:
        i = 0
        contains_zero = [all_nodes[0]]
        all_nodes.remove(contains_zero[0])
        while i < len(contains_zero):
            new_conn = find_indirect_connections(contains_zero[i], conn, contains_zero)
            if new_conn == ['-1'] and i < len(contains_zero):
                i = i+1
                continue
            contains_zero = contains_zero + new_conn
            for x in new_conn:
                all_nodes.remove(x)
            i = i+1
        num_groups += 1
    print num_groups


main()
