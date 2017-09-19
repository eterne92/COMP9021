# Insert your code here
while(True):
    try:
        goal_cell = int(input("Enter the desired goal cell number: "))
        if goal_cell >= 1:
            break
        else:
            raise ValueError
    except ValueError:
        print("Incorrect value, try again")
def move(direction,dice):
    ndice = dice[:]
    if direction == 0: #right
        ndice[0] = 7 - dice[2]
        ndice[2] = dice[0]
    elif direction == 1: #down
        ndice[0] = 7 - dice[1]
        ndice[1] = dice[0]
    elif direction == 2: #left
        ndice[0] = dice[2]
        ndice[2] = 7 - dice[0]
    else: #up
        ndice[0] = dice[1]
        ndice[1] = 7 - dice[0]
    return ndice
bound = 1
taken = 0
bound_reach = 0
direction = 0 #0-r,1-d,2-l,3-u
dice = [3,2,1]
for step in range(0,goal_cell-1):
    # print(f"cell:{step+2}: ",end= '')
    dice = move(direction,dice)
    # print(direction,dice)
    taken += 1
    if taken == bound:
        taken = 0
        bound_reach += 1
        direction += 1
        if direction == 4:
            direction = 0
        if bound_reach == 2:
            bound += 1
            bound_reach = 0
print(f'On cell {goal_cell}, {dice[0]} is at the top, {dice[1]} at the front, and {dice[2]} on the right.')

