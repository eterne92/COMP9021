# Prompts the user for a strictly positive number N
# and outputs an equilateral triangle of height N.
# The top of the triangle (line 1) is labeled with the letter A.
# For all nonzero p < N, line p+1 of the triangle is labeled
# with letters that go up in alphabetical order modulo 26
# from the beginning of the line to the middle of the line,
# starting wth the letter that comes next in alphabetical order
# modulo 26 to the letter in the middle of line p,
# and then down in alphabetical order modulo 26
# from the middle of the line to the end of the line.


# Insert your code here
try:
    level = int(input("Enter strictly positive number: "))
    if level <= 0:
        raise ValueError
except ValueError:
    exit()

now = 0

for i in range(1,level+1):
    print_string = ''
    space_nb = level - i
    print(space_nb * ' ',end = '')
    for t in range(i):
        print_string += chr(now+65)
        now += 1
        if(now == 26):
            now = 0
    print_string = print_string + print_string[-2::-1]
    print(print_string)
