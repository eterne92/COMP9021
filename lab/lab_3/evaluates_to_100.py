L = '123456789'
path = []
def count_f(f):
    def super_f(*args):
        f(*args)
        super_f.count += 1
    super_f.count = 0
    return super_f
@count_f
def dfs(now,index):
    global path
    if index == 9 and now != 100:
        return
    elif now == 100 and index == 9:
        s = ' '.join(path)
        if s[0] == '-':
            print('-',end = '')
        print(s[2:]+' = 100')

        return
    for i in range(index+1,10):
        now += int(L[index:i])
        path.append('+ '+L[index:i])
        dfs(now,i)
        path.pop()
        now -= int(L[index:i])

        now -= int(L[index:i])
        path.append('- '+L[index:i])
        dfs(now,i)
        path.pop()
        now += int(L[index:i])



dfs(0,0)
print(dfs.count)
    
    
