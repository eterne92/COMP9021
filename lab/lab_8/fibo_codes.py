def generator(n = 0, upperbound = 0):
    result = [0,1,2]
    i = 3
    while n == 0 or i < n:
        result.append(result[i-1] + result[i-2])
        i += 1
        if upperbound != 0 and result[-1] >= upperbound:
            return result
    return result

def encode(n):
    '''
    >>> encode(1)
    '11'
    >>> encode(2)
    '011'
    >>> encode(3)
    '0011'
    >>> encode(4)
    '1011'
    >>> encode(8)
    '000011'
    >>> encode(11)
    '001011'
    >>> encode(12)
    '101011'
    >>> encode(14)
    '1000011'
    '''
    if n == 0:
        return '01'
    fibolist = generator(0,n)
    i = -1
    codelist = [0] * len(fibolist)
    while i > -1 * len(fibolist) and n >= 0:
        if fibolist[i] <= n:
            n -= fibolist[i]
            codelist[i] = 1
        i -= 1
    return ''.join(str(i) for i in codelist)[1:].rstrip('0') + '1'

def decode(s):
    '''
    >>> decode('1')
    0
    >>> decode('01')
    0
    >>> decode('100011011')
    0
    >>> decode('11')
    1
    >>> decode('011')
    2
    >>> decode('0011')
    3
    >>> decode('1011')
    4
    >>> decode('000011')
    8
    >>> decode('001011')
    11
    >>> decode('1000011')
    14
    '''
    nums = s.split('11')
    nums = [i + '11' for i in nums if len(i) > 0]
    print(nums)
    if len(nums) == 0:
        return 0
    max_len = max([len(i) for i in nums])
    fibolist = generator(max_len,0)
    fibolist = fibolist[1:]
    list_of_num = []
    for word in nums:
        n = 0
        for i in range(len(word) - 1):
            n += fibolist[i] * int(word[i])
        if word == encode(n):
            list_of_num.append(n)
    if len(list_of_num) == 0:
        return 0
    elif len(list_of_num) == 1:
        return list_of_num[0]
    else:
        return list_of_num




    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
