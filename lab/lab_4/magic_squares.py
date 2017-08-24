# Given a positive integer n, a magic square of order n is a matrix of size n x n
# that stores all numbers from 1 up to n^2 and such that the sum of the n rows,
# the sum of the n columns, and the sum of the two diagonals is constant,
# hence equal to n(n^2+1)/2.


def is_magic_square(square):
# Possibly define other functions
    sum_all = sum([sum(i) for i in square])
    single_sum = sum_all // len(square)
    for row in square:
        if sum(row) != single_sum:
            return False
    for i in range(len(square)):
        if sum([square[t][i] for t in range(len(square))])!= single_sum:
            return False
    sum_left = 0
    for i in range(len(square)):
        sum_left += square[i][i]
    if sum_left != single_sum:
        return False
    for i in range(len(square)-1,-1,-1):
        sum_left -= square[i][i]
    if sum_left == 0:
        return True
    else:
        return False
    
def print_square(square):
    width = len(str(max([max(i) for i in square])))
    for row in square:
        for c in row:
            print(f'{c:{width}}',end = '')
            if c != row[-1]:
                print(' ',end = '')
        print()
    # Replace pass above with your code

