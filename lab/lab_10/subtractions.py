def constract(numbers):
    if len(numbers) == 2:
        return ['(' + str(numbers[0]) + ' - ' + str(numbers[1]) + ')']
    if len(numbers) == 1:
        return [str(numbers[0])]
    t = list()
    for i in range(1,len(numbers)):
        temp1 = constract(numbers[:i])
        temp2 = constract(numbers[i:])
        for e1 in temp1:
            for e2 in temp2:
                t.append('(' + e1 + ' - ' + e2 + ')')
    return t

if __name__ == "__main__":
    numbers = (1, 3, 2, 5, 11, 9, 10, 8, 4, 7, 6)
    for i in constract(numbers):
        if eval(i) == 40:
            print(i)