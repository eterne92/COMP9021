import os
from collections import Counter
from itertools import combinations
import copy
class SudokuError(Exception):
    def __init__(self, message):
        self.message = message

class Sudoku():

    def __init__(self, filename):
        if not os.path.isfile(filename):
            raise SudokuError("Incorrect input")
        #check elements
        sudokuMatrix = []
        with open(filename) as f:
            for eachline in f:
                newline = eachline.replace('\n','')
                newline = newline.replace(' ','')
                if len(newline) != 0:
                    sudokuMatrix.append(list(newline))

        
        if len(sudokuMatrix) != 9 or any(len(line) != 9 for line in sudokuMatrix):
            raise SudokuError("Incorrect input")
        
        for line in sudokuMatrix:
            if any(i not in set('0123456789') for i in line):
                raise SudokuError("Incorrect input")
        for i in range(9):
            for j in range(9):
                if sudokuMatrix[i][j] == '0':
                    sudokuMatrix[i][j] = {1,2,3,4,5,6,7,8,9}
                else:
                    sudokuMatrix[i][j] = {int(sudokuMatrix[i][j])}
        self.matrix = sudokuMatrix
        self.filename = filename
        self.bare = copy.deepcopy(self.matrix)
        self.force()
        self.track = copy.deepcopy(self.matrix)

    def get_row(self):
        return [[self.matrix[i][j] for i in range(len(self.matrix))] \
                                        for j in range(len(self.matrix))]
    
    def get_box(self):
        matrix = []
        for i in range(0,7,3):
            for j in range(0,7,3):
                matrix.append([self.matrix[i + t // 3][j + t % 3] for t in range(9)])
        return matrix


    def _check_line(self,matrix):
        for line in matrix:
            temp = set()
            for i in line:
                if len(i) == 1:
                    if list(i)[0] in temp:
                        return False
                    temp.add(list(i)[0])
        return True

    def preassess(self):
        if not (self._check_line(self.matrix) and self._check_line(self.get_box()) \
                                        and self._check_line(self.get_row())):
            print("There is clearly no solution.")
        else:
            print("There might be a solution.")
        
    def _convert_into_set(self, lines):
        for i in range(9):
            ints = []
            for sets in lines[i]:
                if len(sets) == 1:
                    ints.append(sets)
            for superset in lines[i]:
                if len(superset) > 1:
                    for subset in ints:
                        superset -= subset
    
    def force(self):
        self._convert_into_set(self.matrix)
        self._convert_into_set(self.get_box())
        self._convert_into_set(self.get_row())
        # mprint(self.matrix)
        last = []
        while last != self.matrix:
            last = copy.deepcopy(self.matrix)
            L = [list(self.matrix[i][j])[0] for i in range(9) for j in range(9) if len(self.matrix[i][j]) == 1 ]
            L = Counter(L).most_common()
            for most,_ in L:
                m = self.get_box()
                for i in range(9):
                    if {most} not in m[i]:
                        t = [(most in s) for s in m[i]].count(True)
                        if t == 1:
                            for s in m[i]:
                                if most in s:
                                    s.clear()
                                    s.add(most)
                self._convert_into_set(self.matrix)
                self._convert_into_set(self.get_box())
                self._convert_into_set(self.get_row())
        

    def find_preemptive(self, m):
        for i in range(9):
            superset = set()
            count = 0
            for sets in m[i]:
                if len(sets) > 1:
                    superset |= sets
                    count += 1
            allset = []
            for j in range(2,len(superset)):
                allset += [set(i) for i in combinations(superset,j)]
            for sets in allset:
                if [sets.issuperset(subset) for subset in m[i]].count(True) == len(sets):
                    # print(sets)
                    testset = set()
                    for j in range(9):
                        if sets.issuperset(m[i][j]):
                            testset |= m[i][j]
                    if testset != sets:
                        continue
                    for j in range(9):
                        if not sets.issuperset(m[i][j]):
                            m[i][j] -= sets
        self._convert_into_set(self.matrix)
        self._convert_into_set(self.get_box())
        self._convert_into_set(self.get_row())

    def work(self):
        last = []
        while last != self.matrix:
            last = copy.deepcopy(self.matrix)
            self.find_preemptive(self.matrix)
            self.find_preemptive(self.get_row())
            self.find_preemptive(self.get_box())


    def print_to_tex(self,state):
        filename = self.filename[:-4] + '_' + state + '.tex'
        with open(filename, 'w') as f:
            print(
            '\\documentclass[10pt]{article}\n'
            '\\usepackage[left=0pt,right=0pt]{geometry}\n'
            '\\usepackage{tikz}\n'
            '\\usetikzlibrary{positioning}\n'
            '\\usepackage{cancel}\n'
            '\\pagestyle{empty}\n'
            '\n'
            '\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},\n'
            '                               label=above right:{\\tiny #2},\n'
            '                               label=below left:{\\tiny #3},\n'
            '                               label=below right:{\\tiny #4}]{#5};}}\n'
            '\n'
            '\\begin{document}\n'
            '\n'
            '\\tikzset{every node/.style={minimum size=.5cm}}\n'
            '\n'
            '\\begin{center}\n'
            '\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\\hline\\hline'
            , file = f)
            #body
            if state == 'bare':
                m = self.bare
                show_set = False
            elif state == 'forced':
                m = self.track
                show_set = False
            elif state == 'marked':
                m = self.track
                show_set = True
            elif state == 'worked':
                m = self.matrix
                show_set = True
            output_string = ''
            for i in range(9):
                output_string += f'% Line {i + 1}\n'
                for j in range(9):
                    if show_set and len(self.track[i][j]) != 1:
                        sub_string = '\\N{1 2}{3 4}{5 6}{7 8 9}'
                        for num in {1,2,3,4,5,6,7,8,9}:
                            if num not in self.track[i][j]:
                                #erase all the numbers that is not in track[i][j]
                                sub_string = sub_string.replace(str(num), '')
                            elif num not in m[i][j] or m[i][j] == {num}:
                                #if it's worked, m and track are not the same
                                sub_string = sub_string.replace(str(num), '\\cancel{%s}'%(str(num)))
                    else:
                        sub_string = '\\N{}{}{}{}'
                    if len(m[i][j]) == 1:
                        sub_string += '{%s}'%(str(min(m[i][j])))
                    else:
                        sub_string += '{}'
                    sub_string = sub_string.replace('  ', ' ')
                    sub_string = sub_string.replace('{ ', '{')
                    sub_string = sub_string.replace(' }', '}')
                    output_string += sub_string
                    if j != 8:
                        #not the end of a long line
                        output_string += ' &'
                        if j % 3 == 2:
                            output_string += '\n'
                        else:
                            output_string += ' '
                    else:
                        output_string += ' \\\ \\hline'
                if i % 3 == 2:
                    output_string += '\\hline'
                if i != 8:
                    output_string += '\n\n'
            print(output_string, file = f)
            print('\\end{tabular}\n'
                '\\end{center}\n\n'
                '\\end{document}',file = f)
            

    def bare_tex_output(self):
        self.print_to_tex("bare")
    
    def forced_tex_output(self):
        self.print_to_tex("forced")

    def marked_tex_output(self):
        self.print_to_tex("marked")

    def worked_tex_output(self):
        self.work()
        self.print_to_tex("worked")
