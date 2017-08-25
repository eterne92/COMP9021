# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for given step_number >= 1
# and step_size >= 2, the number of stairs of step_number many steps,
# with all steps of size step_size.
#
# A stair of 1 step of size 2 is of the form
# 1 1
#   1 1
#
# A stair of 2 steps of size 2 is of the form
# 1 1
#   1 1
#     1 1
#
# A stair of 1 step of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#
# A stair of 2 steps of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#         1
#         1 1 1
#
# The output lists the number of stairs from smallest step sizes to largest step sizes,
# and for a given step size, from stairs with the smallest number of steps to stairs
# with the largest number of stairs.
#
# Written by *** and Eric Martin for COMP9021
import time

from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))


def pre_grid():
    for i in range(len(grid)-1,-1,-1):
        for j in range(len(grid)-1,-1,-1):
            if grid[i][j] != 0:
                right[i][j] = right[i][j+1] + 1
                down[i][j] = down[i+1][j] + 1
def find_ans(size):
    ans = [0] * (len(grid) + 1)
    check = [[0] * len(grid) for _ in range(dim)]
    for i in range(len(grid)-size+1):
        for j in range(len(grid)-size+1):
            if check[i][j] == 0 and right[i][j] >= size:
                now_i = i 
                now_j = j + size - 1
                while True:
                    try:
                        if down[now_i][now_j] >=size:
                            now_i = now_i + size - 1
                            check[now_i][now_j] = -1
                            if right[now_i][now_j] >= size:
                                now_j = now_j + size - 1
                                # print('*',now_i,now_j)
                                check[i][j] += 1
                            else:
                                break
                        else:
                            break
                    except IndexError:
                        break
                if check[i][j] > 0:
                    # print(i,j)
                    ans[check[i][j]] += 1
    L = []
    for i in range(1,dim+1):
        if ans[i] > 0:
            L.append((i,ans[i]))
    return L

    
    
def stairs_in_grid():
    pre_grid()
    re = {}
    for i in range(2,int(dim/2)+2):
        L = find_ans(i)
        if len(L) > 0:
            re[i] = L
    return re
    # Replace return {} above with your code

# Possibly define other functions

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
# arg_for_seed, density, dim = 0,3,9
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
right = [[0] * (len(grid)+1) for _ in range(dim+1)]
down = [[0] * (len(grid)+1) for _ in range(dim+1)]
print('Here is the grid that has been generated:')
display_grid()
# A dictionary whose keys are step sizes, and whose values are pairs of the form
# (number_of_steps, number_of_stairs_with_that_number_of_steps_of_that_step_size),
# ordered from smallest to largest number_of_steps.
stairs = stairs_in_grid()
for step_size in sorted(stairs):
    print(f'\nFor steps of size {step_size}, we have:')
    for nb_of_steps, nb_of_stairs in stairs[step_size]:
        stair_or_stairs = 'stair' if nb_of_stairs == 1 else 'stairs'
        step_or_steps = 'step' if nb_of_steps == 1 else 'steps'
        print(f'     {nb_of_stairs} {stair_or_stairs} with {nb_of_steps} {step_or_steps}')
