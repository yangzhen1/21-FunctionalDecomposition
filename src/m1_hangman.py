"""
Hangman.

Authors: Zhen Yang and YiCheng Yang.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.
import random

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.
def main():
    print("Game Starts!")
    all_process()
    while True:
        respond = input('Play another game? (y/n):')
        if respond == 'y':
            all_process()
        if respond == 'n':
            print('Thanks for playing hangman! Have a nice day!')
            break

def all_process():
    guess_count=int(input('How many unsuccessful choices do you want to allow yourself:'))
    word = stage_2()
    wordlist = word_as_a_list(word)
    guess = '-'* len(word)
    guesslist = word_as_a_list(guess)
    #print('The word we choose is:',word)
    process_of_guess(wordlist,guess_count,guesslist)

def process_of_guess(word,n,guess):
    while True:
        if guess == word:
            newword = turn_to_string(guess)
            print('Fantastic! You got the word: ', newword, '!')
            break
        letter_entered = input('What letter do you want to try: ')
        if check_in_word(letter_entered,word):
            if guess != word:
                index = word_index(letter_entered,word)
                for j in range(len(index)):
                    guess[index[j]]=letter_entered
                newword = turn_to_string(guess)
                print('Good Guess! You still have', n, 'unsuccessful guess before you LOSE the game.')
                print('Here is what you currently know about the secret word: ',newword)
        if check_in_word(letter_entered,word) == False:
            n = n - 1
            print('Sorry! There are no',letter_entered,'letters in the secret word. You have ', n, 'unsuccessful guess left before you Lose the Game.')
            if n == 0:
                secretword = turn_to_string(word)
                print('What a pity! You failed and the secret word was',secretword)
                break

def stage_2():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
        r = random.randrange(0,len(words))
        item = words[r]
        return item

def word_index(letter,sequence):
    index=[]
    for k in range(len(sequence)):
        if letter == sequence[k]:
            index = index+[k]
    return index

def word_as_a_list(word):
    wordlist=[]
    for k in range(len(word)):
        wordlist = wordlist + [word[k]]
    return wordlist

def turn_to_string(word):
    aword=''
    for k in range(len(word)):
        aword += str(word[k])
    return aword

def check_in_word(letter,sequence):
    for k in range(len(sequence)):
        if letter == sequence[k]:
            return True
    return False




####### Do NOT attempt this assignment before class! #######

main()
