# Written by *** and Eric Martin for COMP9021


'''
Generates a liast L of random nonnegative integers, the largest possible value
and the length of L being input by the user, and generates:
- a list "fractions" of strings of the form 'a/b' such that:
    . a <= b;
    . a*n and b*n both occur in L for some n
    . a/b is in reduced form
  enumerated from smallest fraction to largest fraction
  (0 and 1 are exceptions, being represented as such rather than as 0/1 and 1/1);
- if "fractions" contains then 1/2, then the fact that 1/2 belongs to "fractions";
- otherwise, the member "closest_1" of "fractions" that is closest to 1/2,
  if that member is unique;
- otherwise, the two members "closest_1" and "closest_2" of "fractions" that are closest to 1/2,
  in their natural order.
'''

from fractions import *
import sys
from random import seed, randint
from math import gcd
import functools

try:
    arg_for_seed, length, max_value = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
if not any(e for e in L):
    print('\nI failed to generate one strictly positive number, giving up.')
    sys.exit()
print('\nThe generated list is:')
print('  ', L)

fractions = []
spot_on, closest_1, closest_2 = [None] * 3

'''
solution without fractions lib
'''
# def printfrac(frac):
#     if frac[1] == 1:
#         return(f'{frac[0]}')
#     else:
#         return (f'{frac[0]}/{frac[1]}')
# def standard(frac):
#     if frac[0] == 0:
#         return [0,1]
#     frac_gcd = gcd(frac[0],frac[1])
#     frac[0] //= frac_gcd
#     frac[1] //= frac_gcd
#     return frac

# def cmpfrac(frac1,frac2):
#     return frac1[0] * frac2[1] - frac1[1]*frac2[0]

# def minus_fraction(frac1,frac2):
#     return standard([frac1[0] * frac2[1] - frac1[1]*frac2[0], frac1[1] * frac2[1]])

# #make list of fracs
# fracs= []
# for i in L:
#     for j in L:
#         if i<=j:
#             frac = standard([i,j])
#             if frac not in fracs:
#                 fracs.append(frac)
# fracs.sort(key = functools.cmp_to_key(cmpfrac))
# fractions = [printfrac(f) for f in fracs]
# if [1,2] in fracs:
#     spot_on = True
# elif len(fracs) == 1:
#     closest_1 = printfrac(fracs[0])
# else:
#     fracs.append([1,2])
#     fracs.sort(key = functools.cmp_to_key(cmpfrac))
#     for i in range(0,len(fracs)):
#         if fracs[i] == [1,2]:
#             index = i
#             break
#     # print(fracs)
#     left = fracs[index-1]
#     right = fracs[index+1]
#     dist_l = [abs(t) for t in minus_fraction(left,[1,2])]
#     dist_r = [abs(t) for t in minus_fraction([1,2],right)]
#     # print(dist_l,dist_r)
#     flag = minus_fraction(dist_l,dist_r)[0]
#     # print(flag)
#     if flag == 0:
#         closest_1 = printfrac(left)
#         closest_2 = printfrac(right)
#     elif flag < 0:
#         closest_1 = printfrac(left)
#     else:
#         closest_1 = printfrac(right)
'''
solution with fractions lib
'''
for i in L:
    for j in L:
        if j >= i:
            if j != 0:
                frac = Fraction(i,j)
                if frac not in fractions:
                    fractions.append(frac)

fractions.sort()
if Fraction(1,2) in fractions:
    spot_on = True
else:
    min_diff = Fraction(1,1)
    near = []
    for frac in fractions:
        if frac > Fraction(1,2):
            diff = frac - Fraction(1,2)
        else:
            diff = Fraction(1,2) - frac
        # print(frac,diff,min_diff)
        if  diff < min_diff:
            min_diff = diff
            near = [frac]
        elif diff == min_diff:
            near.append(frac)
            # print("in")
    if len(near) == 1:
        closest_1 = near[0]
    else:
        closest_1 = near[0]
        closest_2 = near[1]
fractions = [str(x) for x in fractions]
print('\nThe fractions no greater than 1 that can be built from L, from smallest to largest, are:')
print('  ', '  '.join(e for e in fractions))
if spot_on:
    print('One of these fractions is 1/2')
elif closest_2 is None:
    print('The fraction closest to 1/2 is', closest_1)
else:
    print(closest_1, 'and', closest_2, 'are both closest to 1/2')

