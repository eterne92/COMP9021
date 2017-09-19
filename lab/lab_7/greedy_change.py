import sys
from collections import defaultdict
try:
    desired_amount = int(input("Input the desired amount: "))
    if desired_amount < 1:
        raise ValueError
except ValueError:
    print("Be serious, Dude")
    sys.exit()

#greedy solution sucks
cash_pool = [1,2,5,10,20,50,100]
largest_fit = cash_pool.pop()
target_left = desired_amount
solution = defaultdict(int)
total = 0
while target_left > 0:
    while target_left < largest_fit:
        largest_fit = cash_pool.pop()
    target_left -= largest_fit
    solution[largest_fit] += 1
    total += 1
print(f"{total} banknotes are needed\nThe detail is:")
for number, times in sorted(solution.items(),reverse = True):
    print(f"{'$' + str(number):>4}: {times}")
