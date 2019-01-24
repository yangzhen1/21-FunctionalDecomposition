"""
Hangman.

Authors: Zhen Yang and YiCheng Yang.
"""  # DONE: 1.ff PUT YOUR NAME IN THE ABOVE LINE.
def main():
    words = stage_1()
    item = random_stage_1(words)

    x = stage_2()
    stage_3(x , item)



# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.
import random

def stage_1():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
        return words
def random_stage_1(words):
    r = random. randrange(0, len(words))
    item = words[r]
    print(item)
    return item

def stage_2():
    x = str(input('please leave the message after a beep:'))
    return x

def stage_3(x,item):
    list = []
    for k in range(len(item)):
        list.append('-')
    for k in range(len(item)):
        if item[k] == x:
            list[k] = x
    string = ''
    for k in range(len(item)):
        string += list[k]
    print(string)
    return(string)


####### Do NOT attempt this assignment before class! #######
main()



