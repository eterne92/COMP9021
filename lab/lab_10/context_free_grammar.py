import re
from binary_tree_adt import *

    

    
def tokenizer(string):
    r = re.compile("(\d+|\(|\)|\+|\-|\*|\/)")
    t = re.findall(r,string)
    return t
        

def parse_tree(string):
    '''
    
    '''
    t = tokenizer(string)
    tree = expression(t)
    return tree
    
def expression(strlist):
    # print(strlist)
    if not strlist:
        return
    for i in range(len(strlist)):
        if strlist[i] == '+' or strlist[i] == '-':
            if expression(strlist[:i]) and term(strlist[i+1:]):
                temp = BinaryTree(strlist[i])
                temp.left_node = expression(strlist[:i])
                temp.right_node = term(strlist[i+1:])
                return temp
    return term(strlist)

def term(strlist):
    # print(strlist)
    if not strlist:
        return
    for i in range(len(strlist)):
        if strlist[i] == '*' or strlist[i] == '/':
            if term(strlist[:i]) and factor(strlist[i+1:]):
                temp = BinaryTree(strlist[i])
                temp.left_node = term(strlist[:i]) 
                temp.right_node = factor(strlist[i+1:])
                return temp
    return factor(strlist)

def factor(strlist):
    # print(strlist)
    if not strlist:
        return
    if strlist[0] == '(' and strlist[-1] == ')':
        return expression(strlist[1:-1])
    return number(strlist)

def number(strlist):
    # print(strlist)
    if len(strlist) > 1:
        return 
    if strlist[0].isdigit():
        return BinaryTree(strlist[0])
    else:
        return 

if __name__ == "__main__":
    string = '1 - 20 + 300'
    parse_tree(string).print_binary_tree()
    string = '(1 + 20) * (30 - 400)'
    parse_tree(string).print_binary_tree()
    string = "(2 + 3) * (10 - 2) - 12 * (1000 + 15)"
    parse_tree(string).print_binary_tree()
