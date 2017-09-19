from random import choice
import re
n = int(input('What n to use to let an n-gram determine the next character? '))
nwords = int(input('How many words do you want to generate?'))
a = 0
b = 0
with open('dictionary.txt') as f:
    fr = f.read()
    l = fr.split('\n')
    l = [i + '\n' for i in l]
    setl = set(l)
    for j in range(nwords):
        word = ''
        i = 0
        c = ''
        while c != '\n':
            if i == 0:
                c = choice(l)[0]
                word += c
            elif i < n:
                r = re.compile('(?:^|\n)' + word + '(.|\n)')
                t = choice(re.findall(r,fr))
                c = t[-1]
                word += c
            else:
                w = word[i-n:i+1]
                r = re.compile(word[i-n:i+1] + '(.|\n)')
                t = choice(re.findall(r,fr))
                c = t[-1]
                word += c
            i += 1
        if word in setl:
            print('Rediscovered',end = ' ')
            a += 1
        else:
            print('Invented', end = ' ')
            b += 1
#        print(word[:-1])

print(a/b)


        
            

