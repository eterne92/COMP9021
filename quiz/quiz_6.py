# Creates a class to represent a permutation of 2, 2, ..., n for some n >= 0.
#
# An object is created by passing as argument to the class name:
# - either no argument, in which case the empty permutation is created, or
# - "length = n" for some n >= 0, in which case the identity over 1, ..., n is created, or
# - the numbers 1, 2, ..., n for some n >= 0, in some order, possibly together with "lengh = n".
#
# __len__(), __repr__() and __str__() are implemented, the latter providing the standard form
# decomposition of the permutation into cycles (see wikepedia page on permutations for details).
#
# Objects have:
# - nb_of_cycles as an attribute
# - inverse() as a method
#
# The * operator is implemented for permutation composition, for both infix and in-place uses.
#
# Written by *** and Eric Martin for COMP9021

class PermutationError(Exception):
    def __init__(self, message):
        self.message = message

class Permutation:
    def __init__(self, *args, length = None):
        # Replace pass above with your code
        if args == ():
            if length == None:
                self.num = tuple()
            elif length < 0:
                raise PermutationError("Cannot generate permutation from these arguments")
            else:
                self.num = tuple(range(1,length + 1))
        else:
            if not all(isinstance(x, int) for x in args):
                raise PermutationError("Cannot generate permutation from these arguments")
            if length != None and len(args) != length:
                raise PermutationError("Cannot generate permutation from these arguments")
            if length == None or length == len(args):
                if set(args) != set(range(1,len(args) + 1)):
                    raise PermutationError("Cannot generate permutation from these arguments")
                else:
                    self.num = tuple(args)
        self._count_cycle()
        self.nb_of_cycles = len(self.cycles)
            

    def __len__(self):
        # Replace pass above with your code
        return len(self.num)

    def __repr__(self):
        # Replace pass above with your code
        return 'Permutation' + str(self.num)

    def __str__(self):
        # Replace pass above with your code
        output_string = ''
        if self.num == ():
            output_string = '()'
        else:
            for cycle in self.cycles:
                output_string += f"({' '.join(str(i) for i in cycle)})"
        return output_string

    def __mul__(self, permutation):
        # Replace pass above with your code
        if len(self) != len(permutation):
            raise PermutationError("Cannot compose permutations of different lengths")
        else:
            print(self.num,permutation.num)
            new_p = [0 for _ in range(len(self))]
            for i in range(1, len(self) + 1):
                new_p[i - 1] = permutation.num[self.num[i - 1] - 1]
            return Permutation(*(new_p))
    def __imul__(self, permutation):
        # Replace pass above with your code
        self = self * permutation
        return self

    def inverse(self):
        # Replace pass above with your code
        return Permutation(length = len(self)) * self
        
    # Insert your code for helper functions, if needed
    def _count_cycle(self):
        if self.num == ():
            self.cycles = []
        cycles = []
        checked = set()
        for i in range(len(self.num)):
            if self.num[i] not in checked:
                cycle = [self.num[i]]
                cycle_set = {self.num[i]}
                next_index = self.num[i] - 1
                checked.add(self.num[i])
                while self.num[next_index] not in cycle_set:
                    cycle_set.add(self.num[next_index])
                    cycle.append(self.num[next_index])
                    checked.add(self.num[next_index])
                    next_index = self.num[next_index] - 1
                index = cycle.index(max(cycle))
                cycle = cycle[index:] + cycle[:index]
                cycles.append(cycle)

        self.cycles = sorted(cycles)

