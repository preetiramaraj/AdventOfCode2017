# Advent 7
from collections import Counter

with open('advent7.in', 'r') as f:
    inp = f.readlines()

inst = [(x.replace("\n", "")).split("->") for x in inp]
no_link_list = []
some_link_parent_list = []
some_link_children_list = []
flattened_children_list = []
weights = {}

for i in range(0, len(inst)):
    parent = (inst[i][0].split(" "))[0]
    weight = (inst[i][0].split(" "))[1][1:-1]
    weights[parent] = int(weight)
    if len(inst[i]) >= 2:
        children = inst[i][1].replace(" ", "").split(',')
        some_link_children_list.append(tuple(children))
        some_link_parent_list.append(parent)
        for j, val in enumerate(children):
            flattened_children_list.append(val)
            # some_link_parent_list.append(parent)
            if val in no_link_list:
                no_link_list.remove(val)
    if parent not in flattened_children_list:
        no_link_list.append(parent)

print no_link_list

leaf_list = set(flattened_children_list) - set(some_link_parent_list)
index_list = []
for y, tuplex in enumerate(some_link_children_list):
    if set(tuplex).issubset(set(leaf_list)):
        index_list.append(some_link_children_list.index(tuplex))

index_list1 = set(index_list)

balanced = {}
now_parent_list = list(([some_link_parent_list[int(x)] for x in index_list1]))
now_children_list = list(([some_link_children_list[int(x)] for x in index_list1]))

for tuple in now_children_list:
    for val in tuple:
        balanced[val] = weights[val]

while len(now_children_list) != 0:
    for i, val in enumerate(now_parent_list):
        child_weights = [balanced[x] for x in now_children_list[i]]
        if len(set(child_weights)) == 1:
            balanced[val] = weights[val] + sum(child_weights)
        else:
            c = Counter(child_weights)
            weight_to_be_changed = weights[now_children_list[i][child_weights.index((c.most_common()[-1][0]))]]
            print weight_to_be_changed, " aaaa"
            reqd_wt = weight_to_be_changed + c.most_common()[-2][0] - c.most_common()[-1][0]
            print reqd_wt
            break
    now_children_list = []
    for x in now_parent_list:
        for tuplex in some_link_children_list:
            if x in tuplex and tuplex not in now_children_list and set(tuplex).issubset(set(balanced.keys())): # append only if all children have been balanced
                now_children_list.append(tuplex)
    now_parent_list = [some_link_parent_list[some_link_children_list.index(x)] for x in now_children_list]