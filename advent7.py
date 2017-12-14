# Advent 7

with open('advent7.in', 'r') as f:
    inp = f.readlines()

inst = [(x.replace("\n", "")).split("->") for x in inp]
no_link_list = []
some_link_parent_list = []
some_link_children_list = []

for i in range(0, len(inst)):
    parent = (inst[i][0].split(" "))[0]
    if len(inst[i]) >= 2:
        children = inst[i][1].replace(" ", "").split(',')
        for j, val in enumerate(children):
            some_link_children_list.append(val)
            some_link_parent_list.append(parent)
            if val in no_link_list:
                no_link_list.remove(val)
    if parent not in some_link_children_list:
        no_link_list.append(parent)

print no_link_list