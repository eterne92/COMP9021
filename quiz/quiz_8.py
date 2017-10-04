# Randomly fills a grid of size 10 x 10 with digits between 0
# and bound - 1, with bound provided by the user.
# Given a point P of coordinates (x, y) and an integer "target"
# also all provided by the user, finds a path starting from P,
# moving either horizontally or vertically, in either direction,
# so that the numbers in the visited cells add up to "target".
# The grid is explored in a depth-first manner, first trying to move north,
# always trying to keep the current direction,
# and if that does not work turning in a clockwise manner.
#
# Written by Eric Martin for COMP9021


import sys
from random import seed, randrange

from stack_adt import *

import copy

def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def explore_depth_first(x, y, target):
    # print(sum([sum(i) for i in grid]))
    if sum([sum(i) for i in grid]) < target:
        return
    check = [[0 for _ in range(10)] for _ in range(10)]
    s = Stack()
    now_dir = 0
    s.push([x,y,0,{0,1,2,3},grid[x][y], [(x,y)], {(x,y)}])
    # while not s.is_empty():
    for _ in range(200000):
        nx, ny, nd, dirs, nsum, path, path_set = s.peek()
        # for i in range(10):
        #     for j in range(10):
        #         if i == nx and j == ny:
        #             print("#", end = ' ')
        #         elif (i,j) not in path_set:
        #             print(grid[i][j], end = ' ')
        #         else:
        #             print('*', end = ' ')
        #     print()
        # print()
        # print(nx, ny)
        # print(s.peek())
        if nsum == target:
            return path
        elif nsum > target:
            s.pop()
            if s.is_empty():
                break
            s.peek()[3] -= {nd}
        elif len(dirs) == 0:
            s.pop()
            if s.is_empty():
                break
            s.peek()[3] -= {nd}
        else:
            new_dirs = {0,1,2,3}
            for i in range(4):
                new_dir = (nd + i) % 4
                if new_dir in dirs and moving(nx, ny, new_dir) != None:
                    new_x, new_y = moving(nx, ny, new_dir)
                    # print(new_x,"**", new_y)
                    if (new_x, new_y) not in path_set:
                        new_dirs -= {(new_dir + 2) % 4}
                        testre = (possible(new_x,new_y,path_set))
                        # print(new_x, new_y, testre, nsum, nx, ny, new_dirs)
                        if testre + nsum < target:
                            new_dirs -= {new_dir}
                            # print("testre + nsum = ", testre + nsum)
                            continue
                        # print("next one:" ,[new_x, new_y, new_dir, new_dirs, nsum + grid[new_x][new_y], path + [(new_x, new_y)]])
                        s.push([new_x, new_y, new_dir, new_dirs, nsum + grid[new_x][new_y], path + [(new_x, new_y)], path_set | {(new_x, new_y)}])
                        break
            else:
                s.pop()
                if s.is_empty():
                    break
                s.peek()[3] -= {nd}
    return None

def possible(nx, ny, path):
    node_map = [[set() for _ in range(10)] for _ in range(10)]
    for i in range(10):
        for j in range(10):
            if i != 0:
                if (i-1,j) not in path:
                    node_map[i][j] |= {(i-1,j)}
            if j != 0:
                if (i,j-1) not in path:
                    node_map[i][j] |= {(i,j-1)}
            if i != 9:
                if (i+1,j) not in path:
                    node_map[i][j] |= {(i+1,j)}
            if j != 9:
                if (i,j + 1) not in path:
                    node_map[i][j] |= {(i,j+1)}
            node_map[i][j] |= {(i,j)}
    # print(node_map)
    nodes = set()
    new_nodes = copy.deepcopy(node_map[nx][ny])
    while len(nodes) != len(new_nodes):
        # print(nodes)
        nodes = copy.deepcopy(new_nodes)
        for pos in nodes:
            x, y = pos
            new_nodes |= node_map[x][y]
    sum_them = 0
    # print(nodes)
    for x, y in nodes:
        sum_them += grid[x][y]
    return sum_them

def moving(x, y, direction):
    if direction == 0:
        if x == 0:
            return
        x = x - 1
    elif direction == 1:
        if y == 9:
            return
        y = y + 1
    elif direction == 2:
        if x == 9:
            return
        x = x + 1
    elif direction == 3:
        if y == 0:
            return
        y = y - 1
    return x, y

            

try:
    for_seed, bound, x, y, target = [int(x) for x in input('Enter five integers: ').split()]
    if bound < 1 or x not in range(10) or y not in range(10) or target < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(bound) for _ in range(10)] for _ in range(10)]
# grid = [
#     [5,5,5,5,5,5,5,5,5],
#     [5,5,5,5,5,5,5,5,5],
#     [5,5,5,5,5,5,5,5,5],
#     [5,5,5,5,5,5,5,5,5],
#     [5,5,5,0,0,0,0,5,5],
#     [5,5,5,0,0,5,0,5,5],
#     [5,5,5,0,5,5,0,5,5],
#     [5,5,0,0,1,5,5,5,5],
#     [5,5,0,0,0,3,5,5,5],
#     [5,5,5,5,5,5,5,5,5]

    
# ]
# grid=[

# [0,0,0,0,0,0,0,0,0,0],

# [0,0,0,0,0,0,0,0,0,0],

# [0,0,0,0,0,0,0,0,0,0],

# [0,0,0,0,0,0,0,0,0,0],

# [0,0,0,0,0,0,0,0,0,0],

# [0,0,0,0,0,1,0,0,0,0],

# [0,0,0,0,0,0,0,0,0,0],

# [0,0,0,0,0,0,0,0,0,0],

# [0,0,0,0,0,0,0,0,0,0],

# [0,0,0,0,0,0,0,0,0,0],

# ]
print('Here is the grid that has been generated:')
display_grid()
path = explore_depth_first(x, y, target)
if not path:
    print(f'There is no way to get a sum of {target} starting from ({x}, {y})')
else:
    print('With North as initial direction, and exploring the space clockwise,')
    print(f'the path yielding a sum of {target} starting from ({x}, {y}) is:')
    print(path)

# test_path = {(i, j) for i in range(10) for j in range(10) if (i,j) != (0,0)}
# print(possible(0,0,test_path))

