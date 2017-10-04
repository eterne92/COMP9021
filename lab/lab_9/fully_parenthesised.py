'''
Uses the Stack interface to evaluate an arithmetic expression written in postfix
and built from natural numbers using the binary +, -, * and / operators.             
'''


import re
from operator import add, sub, mul, truediv

from stack_adt import Stack, EmptyStackError


def evaluate(expression):
    '''
    >>> from fully_parenthesised import *
    >>> evaluate('100')
    100
    >>> evaluate('[(1 - 20) + 300]')
    281
    >>> evaluate('[1 - {20 + 300}]')
    -319
    >>> evaluate('( { 20*4 }/5 )')
    16.0
    >>> evaluate('(20*[4/5])')
    16.0
    >>> evaluate('({1 + (20 * 30)} - [400 / 500])')
    600.2
    >>> evaluate('{1 + [((20*30)-400) / 500]}')
    1.4
    >>> evaluate('[1 + {(2 * (3+{4*5})) / ([6*7]-[8/9]) }]')
    2.1189189189189186
    >>> evaluate('100 + 3')
    >>> evaluate('(100 + 3')
    >>> evaluate('(100 + -3)')
    >>> evaluate('(100 50)')
    >>> evaluate('(100 / 0)')
    '''
    if any(not (c.isdigit() or c.isspace() or c in '[](){}+-*/') for c in expression):
        return
    # Tokens can be natural numbers, +, -, *, and /
    tokens = re.compile('(\d+|\+|-|\*|/|\(|\)|\{|\}|\[|\])').findall(expression)
    try:
        value = evaluate_expression(tokens)
        return value
    except ZeroDivisionError:
        return

def evaluate_expression(tokens):
    par_dict = {')':'(','}':'{',']':'['}
    stack = Stack()
    # print(tokens)
    for token in tokens:
        # print(token)
        try:
            token = int(token)
            # print(token)
            stack.push(token)
        except ValueError:
            if token in {']',')','}'}:
                try:
                    arg_2 = stack.pop()
                    method = stack.pop()
                    arg_1 = stack.pop()
                    par = stack.pop()
                    if par != par_dict[token]:
                        return
                    if method not in {add,sub,mul,truediv}:
                        return
                    stack.push(method(arg_1,arg_2))
                except EmptyStackError:
                    return 
            elif token in par_dict.values():
                stack.push(token)
            else:
                stack.push({'+':add,'-':sub,'*':mul,'/':truediv}[token])
                # print(stack.peek())
    if stack.is_empty():
        return
    value = stack.pop()
    if not stack.is_empty():
        return
    return value


if __name__ == '__main__':
    import doctest
    doctest.testmod()
