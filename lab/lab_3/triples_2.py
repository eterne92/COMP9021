# Finds all triples of consecutive positive three-digit integers
# each of which is the sum of two squares.


# Insert you code here
from math import sqrt
L = [0 for _ in range(1000)]
solu = {}
for i in range(0,round(sqrt(999))+1):
    for j in range(i,round(sqrt(999))+1):
        t = i*i + j*j
        if 100 <= t and t <= 999:
            L[t] = 1
            solu[t] = (i,j)
def print_solu(t):
    return f'{solu[t][0]}^2+{solu[t][1]}^2'
for i in range(100,998):
    if L[i] == L[i+1] == L[i+2] == 1:
        print(f'({i}, {i+1}, {i+2}) (equal to ({print_solu(i)}, {print_solu(i+1)}, {print_solu(i+2)})) is a solution.')
