# Prompts the user for a number N and prints out the first N + 1 lines of Pascal triangle.



# Insert you code here            

try:
    level = int(input('Enter a nonnegative integer: '))
    if level < 1:
        raise ValueError
except ValueError:
    exit()

pascal = []
L = [1]
max_num = 0 
pascal.append(L)
for i in range(1,level+1):
    L = [1] * (i + 1)
    for t in range(1,i):
        L[t] = pascal[i-1][t-1]+pascal[i-1][t]
    pascal.append(L)
    max_num = max(L)
width = len(str(max_num))

for i in range(level+1):
    print(' ' * width * (level - i),end = '')
    for t in pascal[i]:
        print(f'{t:{width}}',end = '')
        print(' ' * width,end = '')
    print()
