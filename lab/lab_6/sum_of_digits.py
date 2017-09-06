# Prompts the user for two numbers, say available_digits and desired_sum, and
# outputs the number of ways of selecting digits from available_digits
# that sum up to desired_sum.


import sys

# Insert your code here


try:
    digits = int(input("Input a number that we will use as available digits: "))
    desired_sum = int(input("Input a number that represents the desired sum: "))
    if digits < 0 or desired_sum < 0:
        raise ValueError
except ValueError:
	sys.exit()

count = 0
digits = sorted([int(i) for i in list(str(digits))],reverse = True)
check = [0 for _ in range(len(digits))]
def find(n,path):
    if sum(path) > desired_sum:
        return
    elif sum(path) == desired_sum:
        global count
        # print(path,n)
        count += 1
        return
    for i in range(n,len(digits)):
        if check[i] != 1:
            path.append(digits[i])
            check[i] = 1
            find(i,path)
            check[i] = 0
            path.pop()
path = []
find(0,path)
if count > 1:
    print(f"There are {count} solutions.")
elif count == 1:
    print("There is a unique solution.")
elif count == 0:
    print("There is no solution.")
