import re

def tokenizer(string):
    r = re.compile("(\d+|\(|\)|\+|\-|\*|\/)")
    t = re.findall(r,string)
    return t
        

def evaluate(string):
    '''
    >>> from context_free_grammar import *
    >>> evaluate('100')
    100
    >>> evaluate('(100)')
    100
    >>> evaluate('1 - 20 + 300')
    281
    >>> evaluate('(((((1))-((20))+((300)))))')
    281
    >>> evaluate('20 * 4 / 5')
    16.0
    >>> evaluate('(((((20))*((4))/((5)))))')
    16.0
    >>> evaluate('1 + 20 * 30 - 400 / 500')
    600.2
    >>> evaluate('1 + (20*30-400) / 500')
    1.4
    >>> evaluate('1+(20 / 30 * 400)- 500')
    -232.33333333333337
    >>> evaluate('1 + 2 * (3+4*5) / (6*7-8/9)')
    2.1189189189189186
    >>> evaluate('100)')
    >>> evaluate('100 + ')
    >>> evaluate('100 + -3')
    >>> evaluate('100 œ 50')
    >>> evaluate('100 / 0')
    '''
    t = tokenizer(string)
    if expression(t):
        print(expression(t))
    
def expression(strlist):
    if not strlist:
        return False
    for i in range(len(strlist)):
        if strlist[i] == '+':
            if expression(strlist[:i]) and term(strlist[i+1:]):
                return expression(strlist[:i]) + term(strlist[i+1:])
        elif strlist[i] == '-':
            if expression(strlist[:i]) and term(strlist[i+1:]):
                return expression(strlist[:i]) - term(strlist[i+1:])
    return term(strlist)

def term(strlist):
    if not strlist:
        return False
    for i in range(len(strlist)):
        if strlist[i] == '*':
            if term(strlist[:i]) and factor(strlist[i+1:]):
                return term(strlist[:i]) * factor(strlist[i+1:])
        if strlist[i] == '/':
            if term(strlist[:i]) and factor(strlist[i+1:]):
                return term(strlist[:i]) / factor(strlist[i+1:])
    return factor(strlist)

def factor(strlist):
    if not strlist:
        return False
    if strlist[0] == '(' and strlist[-1] == ')':
        return expression(strlist[1:-1])
    return number(strlist)

def number(strlist):
    if len(strlist) > 1:
        return False
    if strlist[0].isdigit():
        return int(strlist[0])
    else:
        return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
