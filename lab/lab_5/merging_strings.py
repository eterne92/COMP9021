# Say that two strings s_1 and s_2 can be merged into a third
# string s_3 if s_3 is obtained from s_1 by inserting
# arbitrarily in s_1 the characters in s_2, respecting their
# order. For instance, the two strings ab and cd can be merged
# into abcd, or cabd, or cdab, or acbd, or acdb..., but not into
# adbc nor into cbda.
#
# Prompts the user for 3 strings and displays the output as follows:
# - If no string can be obtained from the other two by merging,
# then the program outputs that there is no solution.
# - Otherwise, the program outputs which of the strings can be obtained
# from the other two by merging.


# Insert your code here
s1 = input("Please input the first string: ")
s2 = input("Please input the second string: ")
s3 = input("Please input the third string: ")

L = sorted([s1,s2,s3],key = lambda x:len(x))
# print(L)
flag = False
def dfs(n1,n2,s):
    if n1 == len(L[0]) and n2 == len(L[1]):
        # print(s)
        if s == L[2]:
            global flag
            flag = True
            return
    elif s != L[2][:n1+n2]:
        # print(s)
        return
    if n1 < len(L[0]):
        s += L[0][n1]
        dfs(n1+1,n2,s)
        s = s[:-1]
    if n2 < len(L[1]):
        s += L[1][n2]
        dfs(n1,n2+1,s)
        s = s[:-1]
s = ''
dfs(0,0,s)
if flag:
    if L[2] == s1:
        print("The first string can be obtained by merging the other two.")
    elif L[2] == s2:
        print("The second string can be obtained by merging the other two.")
    elif L[2] == s3:
        print("The third string can be obtained by merging the other two.")
else:
    print("No solution")


