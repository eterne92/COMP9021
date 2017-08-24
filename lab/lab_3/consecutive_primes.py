# Finds all sequences of consecutive prime 5-digit numbers,
# say (a, b, c, d, e, f), such that
# b = a + 2, c = b + 4, d = c + 6, e = d + 8, and f = e + 10.


# Insert your code here
from math import sqrt

is_prime = [1 for _ in range(100000)]

for i in range(2,round(sqrt(99999))+1):
    if is_prime[i] == 1:
        t = 2
        while t * i <= 99999:
            is_prime[t*i] = 0
            t += 1
print("The solutions are:")
print()
for a in range(10000,99999-30):
    if is_prime[a:a+31] == [1] + [0] + [1] + [0] * 3 + [1] + [0] * 5 + [1] + [0] * 7 + [1] + [0] * 9  + [1]:
        print(f'{a}  {a+2}  {a+6}  {a+12}  {a+20}  {a+30}')
