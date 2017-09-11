# Randomly fills a grid of size height and width whose values are input by the user,
# with nonnegative integers randomly generated up to an upper bound N also input the user,
# and computes, for each n <= N, the number of paths consisting of all integers from 1 up to n
# that cannot be extended to n+1.
# Outputs the number of such paths, when at least one exists.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

# def dfs(result,i,j):
#     flag = 0
#     if i - 1 >= 0 and grid[i - 1][j] == grid[i][j] + 1:
#         dfs(result,i - 1,j)
#         flag = 1
#     if i + 1 <len(grid) and grid[i + 1][j] == grid[i][j] + 1:
#         dfs(result,i + 1,j)
#         flag = 1
#     if j - 1 >= 0 and grid[i][j - 1] == grid[i][j] + 1:
#         dfs(result,i ,j - 1)
#         flag = 1
#     if j + 1 <len(grid[i]) and grid[i][j + 1] == grid[i][j] + 1:
#         dfs(result,i ,j + 1)
#         flag = 1
#     if flag == 0:
#         result[grid[i][j]] += 1
    

def get_paths():
    # Insert your code for other functions
    result = defaultdict(int)
    check = [[0 for _ in range(width)] for _ in range(height)]
    max_num = max([max(i) for i in grid])
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                check[i][j] = 1
    for t in range(2,max_num):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i - 1 >= 0 and grid[i-1][j] == t - 1:
                    check[i][j] += check[i-1][j]
                    check[i-1][j] = -1
    
    return result
try:
    for_seed, max_length, height, width = [int(i) for i in
                                                  input('Enter four nonnegative integers: ').split()
                                       ]
    if for_seed < 0 or max_length < 0 or height < 0 or width < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randint(0, max_length) for _ in range(width)] for _ in range(height)]
print('Here is the grid that has been generated:')
display_grid()
paths = get_paths()
if paths:
    for length in sorted(paths):
        print(f'The number of paths from 1 to {length} is: {paths[length]}')

