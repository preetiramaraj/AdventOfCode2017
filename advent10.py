#Advent 10


def reverse(num_list, cur, length):
    end_index = cur+length
    if end_index >= len(num_list):
        start_index = end_index % len(num_list)
        sublist = (num_list[cur:] + num_list[:start_index])[::-1]
        shift = len(sublist) - start_index
        num_list = sublist[shift:] + num_list[start_index:cur] + sublist[0:shift]
    else:
        num_list = num_list[:cur] + num_list[cur:end_index][::-1] + num_list[end_index:]

    return num_list


def main():
    input = "102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216"
    length = [int(x) for x in input.split(',')]
    num_list = range(256)
    cur = 0
    skip = 0
    for value in length:
        num_list = reverse(num_list, cur, value)
        cur = ((cur + skip + value) % len(num_list))
        skip += 1
    print num_list[0] * num_list[1]

main()
