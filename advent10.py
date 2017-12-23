# Advent 10
import numpy as np

def reverse(num_list, cur, length):
    end_index = cur + length
    if end_index >= len(num_list):
        start_index = end_index % len(num_list)
        sublist = (num_list[cur:] + num_list[:start_index])[::-1]
        shift = len(sublist) - start_index
        num_list = sublist[shift:] + num_list[start_index:cur] + sublist[0:shift]
    else:
        num_list = num_list[:cur] + num_list[cur:end_index][::-1] + num_list[end_index:]

    return num_list


def calculate_dense_hash(num_list):
    size = 16
    dense_hash = []
    prev_i = 0
    for i in range(16, 257, 16):
        ar = np.array(num_list[prev_i:i])
        dense_hash.append(np.bitwise_xor.reduce(ar))
        prev_i = i
    return dense_hash


def main():
    input = "102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216"
    # length = [int(x) for x in input.split(',')]  #part 1
    length = [ord(x) for x in input]
    length = length + [17, 31, 73, 47, 23]
    num_list = range(256)
    cur = 0
    skip = 0
    for i in range(64):
        for value in length:
            num_list = reverse(num_list, cur, value)
            cur = ((cur + skip + value) % len(num_list))
            skip += 1
        # print num_list[0] * num_list[1] # Part 1
    dense_hash = calculate_dense_hash(num_list)
    final_hash = [y.replace('L', '') for y in [hex(x).replace('0x', '') for x in dense_hash]]
    print ''.join([y.replace(y, '0'+y) if len(y) == 1 else y for y in final_hash])


main()
