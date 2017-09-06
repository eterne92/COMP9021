from random import randint
from collections import defaultdict, deque


while True:
    try:
        n_couples = int(input("Enter a strictly positive number for the number of couples: "))
        if n_couples <= 0:
            raise ValueError
        break
    except ValueError:
        print("Wrong input, try again!")

while True:
    try:
        men = input(f"Enter {n_couples} names for the men, all on one line and separated by spaces,\n  or just press Enter for the default \"names\" M_1, ..., M_{n_couples}: ")
        if men == '':
            men = ['M_' + str(i) for i in range(1,n_couples+1)]
            break
        elif len(men.split()) == n_couples:
            men = men.split()
            break
        else:
            raise ValueError
    except ValueError:
        print("Wrong input, try again!")
            
while True:
    try:
        women = input(f"Enter {n_couples} names for the women, all on one line and separated by spaces,\n  or just press Enter for the default \"names\" M_1, ..., M_{n_couples}: ")
        if women == '':
            women = ['W_' + str(i) for i in range(1,n_couples+1)]
            break
        elif len(women.split()) == n_couples:
            women = women.split()
            break
        else:
            raise ValueError
    except ValueError:
        print("Wrong input, try again!")

#random generate favor
m_choice = defaultdict(deque)
w_choice = defaultdict(deque)
for man in range(1,n_couples + 1):
    while len(m_choice[man]) != n_couples:
        temp = randint(1,n_couples)
        if temp not in m_choice[man]:
            m_choice[man].append(temp)

for woman in range(1,n_couples + 1):
    while len(w_choice[woman]) != n_couples:
        temp = randint(1,n_couples)
        if temp not in w_choice[woman]:
            w_choice[woman].append(temp)

for man in m_choice:
    print(f"Preferences for {men[man - 1]}: ", end = '')
    for woman in m_choice[man]:
       print(f'{women[woman - 1]}', end = ' ') 
    print("\n")

for woman in w_choice:
    print(f"Preferences for {women[woman - 1]}: ", end = '')
    for man in w_choice[woman]:
       print(f'{men[man - 1]}', end = ' ') 
    print()


single_man = set(range(1,n_couples+1))
dating_person = [0 for _ in range(n_couples)]
while len(single_man) != 0:
    #date girls
    new_set = single_man.copy()
    for man in new_set:
        date_girl = m_choice[man].popleft()
        girl_index = w_choice[date_girl].index(man) 
        if dating_person[date_girl - 1] == 0:
            dating_person[date_girl - 1] = man
            single_man.remove(man)
        elif dating_person[date_girl - 1] > girl_index:
            single_man.add(dating_person[date_girl - 1])
            dating_person[date_girl - 1] = man
            single_man.remove(man)
            
print("\nThe matches are:")
for i in range(n_couples):
    print(f"{women[i]} -- {men[dating_person[i] - 1]}")