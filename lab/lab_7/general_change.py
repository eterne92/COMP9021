import sys
from collections import defaultdict
cash_pool = []
print("Input pairs of the form 'value : number'\n\
to indicate that you have ’number’ many banknotes of face value ’value’.\n\
Input these pairs one per line, with a blank line to indicate end of input.")
while True:
    t = input()
    if t == '':
        break;
    t = t.split(':')
    cash_pool+= [int(t[0])] * int(t[1])
try:
    desired_amount = int(input("Input the desired amount: "))
    if desired_amount < 1:
        raise ValueError
except ValueError:
    print("Be serious, Dude")
    sys.exit()

solution = defaultdict(int)
dp = [[0 for _ in range(desired_amount + 1)] for _ in range(len(cash_pool) + 1)]


for i in range(1,len(dp)):
    for j in range(1,len(dp[i])):
        space_left =  j - cash_pool[i - 1]
        print(i,j,space_left)
        if j == cash_pool[i - 1]:
            dp[i][j] = 1
        else:
            if dp[i - 1][space_left] != 0:
                dp[i][j] = dp[i - 1][space_left] + 1



for i in range(len(dp)):
    for j in range(len(dp[i])):
        print(f"{dp[i][j]:3}", end = ' ' if j != len(dp[i]) - 1 else '\n')


