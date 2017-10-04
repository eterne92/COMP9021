
from collections import defaultdict, deque
import sys


'''
Computes all transformations from a word word_1 to a word word_2, consisting of
sequences of words of minimal length, starting with word_1, ending in word_2,
and such that two consecutive words in the sequence differ by at most one letter.
All words have to occur in a dictionary with name dictionary.txt, stored in the
working directory.
'''


dictionary_file = 'dictionary.txt'

def get_words_and_word_relationships():
    with open(dictionary_file) as f:
        s = set(f.read().split('\n'))
        graph = defaultdict(set)
        for word in s:
            for i in range(len(word)):
                for j in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    if j != word[i]:
                        new_word = word[:i] + j + word[i+1:]
                        if new_word in s:
                            graph[word].add(new_word)
    return graph
	# Replace pass above with your code

def word_ladder(word_1, word_2):
    '''
    
    '''
    word_1 = word_1.upper()
    word_2 = word_2.upper()
    graph = get_words_and_word_relationships()
    # Complete this function
    result_path = []
    q = deque()
    q.append((word_1,[word_1]))
    while len(q) != 0:
    # for _ in range(10):
        word,path = q.popleft()
        if len(result_path) > 0 and len(path) == len(result_path[0]):
            return result_path
        # print(word)
        for new_word in graph[word]:
            # print(new_word, end = '*')
            if new_word == word_2:
                if len(result_path) == 0:
                    result_path.append(path + [new_word])
                elif len(result_path[0]) == len(path) + 1:
                    result_path.append(path + [new_word])
                else:
                    return result_path
            else:
                q.append((new_word, path + [new_word]))
                
                
if __name__ == "__main__":
    print(word_ladder('three','seven'))
