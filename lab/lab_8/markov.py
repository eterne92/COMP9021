from random import choice
import re
n = int(input('What n to use to let an n-gram determine the next character? '))
nwords = int(input('How many words do you want to generate?'))
with open('dictionary.txt') as f:
    l = f.read().split('\n')
    l = [i + '\n' for i in l]
    for j in range(nwords):
        word = ''
        i = 0
        c = ''
        while c != '\n':
            if i == 0:
                c = choice(l)[0]
                word += c
            elif i < n:
                c = choice([w for w in l if w.startswith(word)])[i]
                word += c
            else:
                t = choice([w for w in l if word[i-n:i+1] in w])
                c = t[t.find(word[i-n:i+1]) + n]
                word += c
            i += 1
        if word in l:
            print('Rediscovered',end = ' ')
        else:
            print('Invented', end = ' ')
        print(word[:-1])



        
            

