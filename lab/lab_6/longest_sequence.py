# Prompts the user for a string w of lowercase letters and outputs the
# longest sequence of consecutive letters that occur in w,
# but with possibly other letters in between, starting as close
# as possible to the beginning of w.


import sys


# Insert your code here
w = input("Please input a string of lowercase letters: ")
path = []
maxpath = []
def dfs(n,path):
    global maxpath
    if len(path) > len(maxpath):
            maxpath = path[:]
    if n == len(w):
        return
    for i in range(n,len(w)):
        if path == [] or ord(w[i]) - ord(path[-1]) == 1:
            path.append(w[i])
            dfs(i+1,path)
            path.pop()
            
dfs(0,[])
print("The solution is: " + ''.join(maxpath))
