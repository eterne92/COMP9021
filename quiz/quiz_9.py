# Generates a binary tree T whose shape is random and whose nodes store
# random even positive integers, both random processes being directed by user input.
# With M being the maximum sum of the nodes along one of T's branches, minimally expands T
# to a tree T* such that:
# - every inner node in T* has two children,
# - the sum of the nodes along all of T*'s branches is equal to M, and
# - when leaves in T are expanded to 2 leaves in T*, those 2 leaves receive the same value.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange
from collections import deque
from binary_tree_adt import *



def create_tree(tree, for_growth, bound):
    if randrange(max(for_growth, 1)):
        tree.value = 2 * randrange(bound + 1)
        tree.left_node = BinaryTree()
        tree.right_node = BinaryTree()
        create_tree(tree.left_node, for_growth - 1, bound)
        create_tree(tree.right_node, for_growth - 1, bound)


def expand_tree(tree):
    # Replace pass above with your code
    max_sum = find_max(tree)
    if tree.value == None:
        return
    q = deque()
    q.append((tree,tree.value))
    while len(q) != 0:
        tree_now, sum_now = q.popleft()
        if tree_now.left_node.value != None:
            q.append((tree_now.left_node,sum_now + tree_now.left_node.value))
        elif max_sum - sum_now:
            tree_now.left_node = BinaryTree(max_sum - sum_now)
        if tree_now.right_node.value != None:
            q.append((tree_now.right_node,sum_now + tree_now.right_node.value))
        elif max_sum - sum_now:
            tree_now.right_node = BinaryTree(max_sum - sum_now)

# Possibly define other functions
def find_max(tree):
    if tree.value == None:
        return
    q = deque()
    q.append((tree,tree.value))
    max_sum = 0
    while len(q) != 0:
        tree_now, sum_now = q.popleft()
        if tree_now.left_node.value != None:
            q.append((tree_now.left_node,sum_now + tree_now.left_node.value))
        if tree_now.right_node.value != None:
            q.append((tree_now.right_node,sum_now + tree_now.right_node.value))
        if tree_now.left_node.value == None and tree_now.right_node.value == None:
            if sum_now > max_sum:
                max_sum = sum_now
        
    
    return max_sum

                
try:
    for_seed, for_growth, bound = [int(x) for x in input('Enter three positive integers: ').split()
                                   ]
    if for_seed < 0 or for_growth < 0 or bound < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
    
seed(for_seed)
tree = BinaryTree()
create_tree(tree, for_growth, bound)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
expand_tree(tree)
print('Here is the expanded tree:')
tree.print_binary_tree()

