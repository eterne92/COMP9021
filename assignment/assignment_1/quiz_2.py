from collections import deque
import sys

def shift(state,method):
    if method == 0: #row exchange
        return(state[::-1])
    elif method == 1: #right circular shift
        return(state[3] + state[:3] + state[5:] + state[4])
    elif method == 2: #middel clockwise rotation
        return(state[0] + state[6] + state[1] + state[3] + state[4] + state[2] + state[5] + state[7])
    return state



def bfs(final_state,state):
    queue = deque()
    queue.append(state)
    index = 0
    level_end = state
    level = 0
    state_set = {state}
    while len(queue) > 0:
        state = queue.popleft()
        if state == final_state:
            return level
        for i in range(3):
            new_state = shift(state,i)
            if new_state in state_set:
                continue
            else:
                queue.append(new_state)
                state_set.add(new_state)
        if state == level_end:
            level += 1
            level_end = queue[-1]

final_state = input("Input final configuration: ")
final_state = final_state.replace(' ','')
L  = list('12345678')
for c in final_state:
    if c not in L:
        print('Incorrect configuration, giving up...')
        sys.exit()
    else:
        L.remove(c)


state = '12345678'
steps = bfs(final_state,state)
if steps == 0 or steps == 1:
    print(f'{steps} step is needed to reach the final configuration.')
else:
    print(f'{steps} steps are needed to reach the final configuration.')



