# Randomly generates N distinct integers with N provided by the user,
# inserts all these elements into a priority queue, and outputs a list
# L consisting of all those N integers, determined in such a way that:
# - inserting the members of L from those of smallest index of those of
#   largest index results in the same priority queue;
# - L is preferred in the sense that the last element inserted is as large as
#   possible, and then the penultimate element inserted is as large as possible, etc.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, sample

from priority_queue_adt import *


# Possibly define some functions
    
def preferred_sequence():
    # Replace pass above with your code (altogether, aim for around 24 lines of code)
    plist = pq._data[ : len(pq) + 1]
    # print(plist)
    for index in range(len(plist) - 1, 0, -1):
        fathers = []
        ni = index
        while index > 0:
            fathers.append(index)
            index = index // 2
        # print(fathers)
        fathers = fathers[::-1]
        for i in range(len(fathers)):
            new_list = plist[:]
            for t in range(i,len(fathers) - 1):
                pnode = fathers[t]
                child = fathers[t + 1]
                # print(pnode, child)
                new_list[pnode], new_list[child] = new_list[child], new_list[pnode]
            # print(new_list, ni)
            # print(stf(1,new_list[:ni]))
            if stf(1,new_list[:ni]):
                break
        plist = new_list
        # print(plist)
    return plist[1:]

def stf(index, heap):
    if index > len(heap):
        return True
    left = index * 2
    right = index * 2 + 1
    if left < len(heap) and heap[left] > heap[index]:
        return False
    if right < len(heap) and heap[right] > heap[index]:
        return False
    return stf(left, heap) and stf(right, heap)

# try:
#     for_seed, length = [int(x) for x in input('Enter 2 nonnegative integers, the second one '
#                                                                              'no greater than 100: '
#                                              ).split()
#                        ]
#     if for_seed < 0 or length > 100:
#         raise ValueError
# except ValueError:
#     print('Incorrect input (not all integers), giving up.')
#     sys.exit()    
for for_seed, length in [(i, j) for i in range(20) for j in range(100)]:
    seed(for_seed)
    L = sample(list(range(length * 10)), length)
    pq = PriorityQueue()
    for e in L:
        pq.insert(e)
    # print('The heap that has been generated is: ')
    # print(pq._data[ : len(pq) + 1])
    # print('The preferred ordering of data to generate this heap by successsive insertion is:')
    # print(preferred_sequence())
    plist = preferred_sequence()
    newpq = PriorityQueue()
    for e in plist:
        newpq.insert(e)

    if pq._data[:len(pq) + 1] != newpq._data[:len(newpq) + 1]:
        print("nooooooooooooooo")
        break
    else:
        print("coooooooooooooool")


