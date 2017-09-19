import sys
input_charts = input("Enter between 3 and 10 lowercase letters: ")
input_charts = input_charts.replace(" ","")
if not (input_charts.islower() and input_charts.isalpha()):
    print("Incorrect input, giving up...")
    sys.exit()
if len(input_charts) > 10 or len(input_charts) < 3:
    print("Incorrect input, giving up...")
    sys.exit()
all_words = {}
char_to_value = {
    'a':2, 'b':5, 'c':4, 'd':4, 'e':1, 'f':6, 
    'g':5, 'h':5, 'i':1, 'j':7, 'k':6, 'l':3,
    'm':5, 'n':2, 'o':3, 'p':5, 'q':7, 'r':2, 
    's':1, 't':2, 'u':4, 'v':6, 'w':6, 'x':7,
    'y':5, 'z':7
}
with open("wordsEn.txt") as f:
    for word in f.readlines():
        word = word[:-1]
        # print(word)
        char_quantity = [0] * 26
        value = 0
        for c in word:
            try:
                value += char_to_value[c]
                char_quantity[ord(c)-ord('a')] += 1
            except KeyError:
                pass
        all_words[word] = (value,char_quantity)




#do something with inputs
input_quantity = [0] * 26
for c in input_charts:
    input_quantity[ord(c) - ord('a')] += 1
max_value = 0
wordlist = []
for word,value in all_words.items():
    for i in range(26):
        flag = 1
        if value[1][i] > input_quantity[i]:
            flag = 0 
            break
    if flag == 0:
        continue
    else:
        if value[0] > max_value:
            max_value = value[0]
            wordlist = [word]
        elif value[0] == max_value:
            wordlist += [word]

wordlist.sort()
if len(wordlist) == 0:
    print("No word is built from some of those letters.")
else:
    print(f"The highest score is {max_value}.")
    if len(wordlist) == 1:
        print(f"The highest scoring word is {wordlist[0]}")
    else:
        print("The highest scoring words are, in alphabetical order:")
        for word in wordlist:
            print(f'    {word}')


        

