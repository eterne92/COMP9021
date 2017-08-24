# Finds all triples of positive integers (i, j, k) such that
# i, j and k are two digit numbers, i < j < k,
# every digit occurs at most once in i, j and k,
# and the product of i, j and k is a 6-digit number
# consisting precisely of the digits that occur in i, j and k.


# Insert your code here
L = [x for x in range(10,98) if x // 10 != x % 10 ]
for i in L:
    for j in L:
        for k in L:
            if k>j>i:
                d =  set(str(i) + str(j) + str(k))
                if len(d) == 6:
                    if set(str(i*j*k)) == d:
                        print(f'{i} x {j} x {k} = {i*j*k} is a solution.')
