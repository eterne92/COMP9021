from random import randint
import sys

poker2dice = {
    'Ace':0,'King':1,'Queen':2,'Jack':3,'10':4,'9':5
}
dice2poker = ['Ace','King','Queen','Jack','10','9']


def check_hand(dices):
    check = [0] * 6
    for dice in dices:
        check[dice] += 1
    if max(check) == 5:
        return 'Five of a kind'
    elif max(check) == 4:
        return 'Four of a kind'
    elif max(check) == 3:
        if 2 in check:
            return 'Full house'
        else:
            return 'Three of a kind'
    elif max(check) == 2:
        if check.count(2) == 1:
            return 'One pair'
        else:
            return 'Two pair'
    else:
        if check[0] == 0 or check[-1] == 0:
            return 'Straight'
        else:
            return 'Bust'

def print_dice(dices):
    dices.sort()
    print('The roll is:', end = '')
    for dice in dices:
        print(f' {dice2poker[dice]}',end = '')
    print('\n',end = '')
    print(f'It is a {check_hand(dices)}')



def reroll(orginal_dices,round):
    dices = orginal_dices[:]
    while(True):
        input_pokers = input(f'Which dice do you want to keep for the {round} roll? ')
        pokers = input_pokers.split()
        if len(pokers) == 1 and pokers[0].upper() == 'ALL':
            return -1
        else:
            flag = 1
            for poker in pokers:
                if poker not in poker2dice:
                    flag = 0
                    break
                elif poker2dice[poker] not in dices:
                    flag = 0
                    break
                else:
                    index = dices.index(poker2dice[poker])
                    dices[index] = -1
            if flag == 0:
                print('That is not possible, try again!')
                dices = orginal_dices[:]
                continue
            else:
                break
    # print(dices)
    rolls = [1] * 5
    for i in range(5):
        if dices[i] == -1:
            rolls[i] = 0
    if not 1 in rolls:
        return -1
    else:
        return rolls

def roll_the_dice(rolls,dices):
    for i in range(5):
        if rolls[i] == 1:
            dices[i] = randint(0,5)
    return dices

def play():
    rolls = [1] * 5
    i2word = ['first','second','third']
    for i in range(3):
        if not i:
            dices = [0] * 5
            dices = roll_the_dice(rolls,dices)
            print_dice(dices)
        else:
            rolls = reroll(dices,i2word[i])
            if rolls == -1:
                print('Ok, done.')
                break
            else:
                roll_the_dice(rolls,dices)
                print_dice(dices)
    return


def simulate(n):
    rolls = [1] * 5
    dices = [0] * 5
    hands = {
        'Five of a kind' : 0,
        'Four of a kind' : 0,
        'Full house' : 0,
        'Straight' : 0,
        'Three of a kind': 0,
        'Two pair' : 0,
        'One pair' : 0,
        'Bust' : 0}
    hands_names = [
        'Five of a kind',
        'Four of a kind',
        'Full house',
        'Straight',
        'Three of a kind',
        'Two pair',
        'One pair',
        'Bust']

    for i in range(n):
        dices = roll_the_dice(rolls,dices)
        hands[check_hand(dices)] += 1
    
    for i in range(7):
        print(f"{hands_names[i]:15}: {hands[hands_names[i]]/n*100:.2f}%")
