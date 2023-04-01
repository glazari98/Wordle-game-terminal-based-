# Wordle_Capstone3.py
# Author: Georgios Lazari (G21065613)
# Email: GLazari@uclan.ac.uk
# Description: The Wordle_Capstone3.py program demonstrates the Wordle game in 2 modes: autoplay and interactive-play
# mode. For autoplay type 0 in the main menu and for interactive-mode type 1. If you want to exit the program type q
# either in the main menu or while playing the interactive mode. In the interactive mode you have 6 tries to find the
# wordle otherwise you loose and the program exits.
from random import *

# the below code is for the 40% of the assignment

# dictionary where the keys will be the letters and the values wil be the number of time the letter appears in the list
# of words
letter_frequencies = {}
# list containing all the words from the wordles.txt
words = []

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# the way to read the words on each line from wordles.txt and store them in a list was copied
# from slides 20-23 Week10_(Part C)_File Processing.pdf
infile = open('wordles.txt', 'r')
lines = infile.readlines()
for i in lines:
    words.append(i.strip())


# function to look into the list of words and find the frequencies of each letter and print them in descending order
def print_frequencies(list_of_words):
    # it takes each word, and each character, if that character has already been used as a key then just increase its
    # frequence by 1, if not then just make a new entry in the dictionary with the letter as key and 1 as value.
    # solution adapted from CO1417-Lab Report (Guide for Lab 9).pdf
    for word in list_of_words:
        for char in word:
            if char in letter_frequencies:
                letter_frequencies[char] += 1
            else:
                letter_frequencies[char] = 1
    # the code for sorting the frequencies in descending order was adapted from:
    # https://stackoverflow.com/questions/9764298/given-parallel-lists-how-can-i-sort-one-while-permuting-rearranging-the-other
    letters, alphabet = zip(*sorted(zip(letter_frequencies.values(), letter_frequencies.keys()), reverse=True))

    for letter, frequency in zip(alphabet, letters):
        print(letter + ": " + str(frequency))


# the below function is for the 50% of the assignment the function takes as arguments a list of words and a list of
# individual letters and returns the words that all letters appear in
def find_words_with_letters(list_of_words, list_of_letters) -> [str]:
    common_words = []
    # check if the user put a number in the letters list, if yes then exit
    for letter in list_of_letters:
        if letter.isdigit():
            print('Your list should not contain numbers')
            exit()
    # check if 5 letters were entered in the list, and then check for each word in the list of words
    if len(list_of_letters) == 5:
        for word in list_of_words:
            # if all letters in the list of letters appear in the word then append that word into the common_words list
            if all(l in word for l in list_of_letters):
                common_words.append(word)
    # if fewer or more than 5 letters are provided in the list of letters, the common_words list is empty
    else:
        common_words = []
    return common_words


# the below function is for the 60% of the assignment
# this function takes as arguments a string secret word and a string check word and returns a list of string colours
# according to the similarity of the two words
def check(secret, check_word) -> [str]:
    colour_list = []
    # for-loops to check if the user entered a number in the two words, if yes then exit
    for l in check_word:
        if l.isdigit():
            print('Your words should not contain numbers')
            exit()
    for i in secret:
        if i.isdigit():
            print('Your words should not contain numbers')
            exit()
    # for loop to go through the letters of check_word and secret word
    for i in range(len(check_word)):
        # if a letter appears on the same position on both words, then enter the 'green' string into the colours_list
        if check_word[i] == secret[i]:
            colour_list.append('green')
        # if a letter of the check_word appears in the secret but not on the same position then enter 'yellow' into the
        # colours list
        elif check_word[i] in secret:
            colour_list.append('yellow')
        # if the letter of the check_word doesn't appear at all in the secret then enter 'gray' into the colours list
        else:
            colour_list.append('gray')
    return colour_list


# the below function is for the 70%+ of the assignment
# this function takes as arguments a list of words, a list of letters that are said to be the grays which means we don't
# want them to appear in the word we are searching. A dictionary of letters(yellows) as keys and as values, sets of the positions
# where we don't want the letters to appear in the word we are searching. Lastly, a dictionary of letters(greens) as keys and as
# values, sets of the positions where we want the letters to appear.
def find_word(words, grays, yellows, greens):
    choosen = []
    # for loop to check every word in the list of words
    for word in words:
        # for the letters in the grays list, if all letters don't appear in the word then proceed
        if all(l not in word for l in grays):
            # boolean variable indicating if the keys and values of the yellow dictionary match the word
            yellows_match = True
            # for loop to check the keys and values of the yellows dictionary
            for letter, positions in yellows.items():
                # if statement to check if letter appears in all the positions that we don't want it to appear in the
                # word(in all the indexes of the values' set)
                if all(word[position] == letter for position in positions):
                    # if it does make the boolean variable False and exit the loop
                    yellows_match = False
                    break
                # if statement to check if the letter appears in the word in any of the position we don't want it to
                # appear(in any of the indexes of the values' set
                elif any(word[position] == letter for position in positions):
                    # if it does make the boolean variable False and exit the loop
                    yellows_match = False
                    break
                # if statement to check if the letter doesn't appear in the word
                elif letter not in word:
                    # if it does not make the boolean variable False and exit the loop
                    yellows_match = False
                    break
            # boolean variabe indicating if the keys and values of the green dictionary match the word
            greens_match = True
            # for loop to check if the letters and positions of those letters in the greens dictionary appear in the
            # word we are searching.
            for letter, positions in greens.items():
                for position in positions:
                    if word[position] != letter:
                        # if not make the boolean variable False, and exit the loop
                        greens_match = False
                        break
            # if both of the boolean variables are True then it means our criteria that we are searching are met and the
            # word is entered into the choosen list
            if yellows_match and greens_match:
                choosen.append(word)
    # if statement to return the first entry of the choosen list if there are more than 1 entries
    if len(choosen) > 0:
        return choosen[0]
    # if nothing is entered then return None
    else:
        return None

# the below code is for 80%+ of the assignment
title = '*** Welcome to the Wordle game! ***\nSelect mode: [0] for Autoplay or [1] to Play against the computer. Hit ' \
        '[Q] to Quit: '

game_mode = input(title)
# while True loop is an infinite loop, the only parameter to exit the loop is to type 'q' inside the function
while True:
    # if the user types 1 then they will play interactive-play mode
    if game_mode == '1':
        # set the number of tries to 1
        number_of_tries = 1
        print('Challenge accepted! Can you guess the Secret Word? [type q to Quit]\n')
        # choose a random word from the list of words, this is the word that we will be trying to find
        random_word = choice(words)
        print(random_word)
        # ask the user to enter a word, set it to lower-case
        word = input('Enter a 5-letter word: ').lower()
        # if the user types 'q', exit the program
        if word == 'q':
            print('Thank you for playing Wordle. Byee!!')
            exit()
        # while loop to check if the user enter a word more or less than 5 letters, a word that is not in the list,
        # entered nothing or 'q' to exit
        # this is for the first entry of the user
        while True:
            if len(word) == 0:
                print('You entered nothing')
            elif word == 'q':
                print('Thank you for playing Wordle. Byee!!')
                exit()
            elif len(word) != 5:
                print(word + " is not 5 letters long!")
            elif word not in words:
                print(word + " is not in the list of accepted words!")
            else:
                break
            # while in this loop everytime a statement is true, ask for the user to enter a 5-letter word again
            word = str(input('Enter a 5-letter word: '))

        # if the user finds the word from first try
        if word == random_word and number_of_tries == 1:
            # stating number of tries and list of colours from check function created above
            print(str(number_of_tries) + ' -> ' + str(check(random_word, word)))
            print('Lucky or Genius! You found the wordle in just 1 try!!!\n')
            # main menu appears again, asking for the user to choose a mode
            game_mode = input(title)
        else:
            # while loop for when the user types words that donlt much the required one
            while word != random_word:
                # print number of tries and the list of colours that check the similarity of letter of the words from
                # the check function created above
                print(str(number_of_tries) + ' -> ' + str(check(random_word, word)))
                # the user has 6 tries to find the word, otherwise he looses and the program exits
                if number_of_tries == 6:
                    print("Wordle: " + random_word + ". Unfortunately you were unable to find the wordle in 6 tries "
                                                     "so YOU LOST!!\n")
                    exit()
                # each time the user doesn't find the word, number of tries increases by one, and the user is asked to
                # enter another word
                number_of_tries += 1
                word = str(input('Enter a 5-letter word: '))

                if word == 'q':
                    print('Thank you for playing Wordle. Byee!!')
                    exit()
                # while loop to check if the user enter a word more or less than 5 letters, a word that is not in the list,
                # entered nothing or 'q' to exit
                # this is for the tries when the user repeatedly doesn't find the word after 1st try
                while True:
                    if len(word) == 0:
                        print('You entered nothing')
                    elif word == 'q':
                        print('Thank you for playing Wordle. Byee!!')
                        exit()
                    elif len(word) != 5:
                        print(word + " is not 5 letters long")
                    elif word not in words:
                        print(word + " is not in the list of accepted words!")
                    else:
                        break
                    word = str(input('Enter a 5-letter word: '))
            else:
                # winning message stating the number of tries and list of colours from check function created above
                print(str(number_of_tries) + ' -> ' + str(check(random_word, word)))
                print('Congratulations! you found the wordle in ' + str(number_of_tries) + ' tries!\n')
                # main menu appears again
                game_mode = input(title)
    # if the user types 0 then the program will proceed with auto-play
    elif game_mode == '0':
        # set tries to 1
        tries = 1
        # secret word is the required word(random ward from the wordles.txt)
        secret_word = choice(words)
        # test word is the word the program first tests(random ward from the wordles.txt)
        test_word = choice(words)
        print('trying: ' + test_word)
        # use the check function to get a list of colours comparing the two words
        test = check(secret_word, test_word)
        print('-> ' + str(test))
        # make a list for gray letters, and two dictionaries for yellow and green letters
        # these will be used for the find_word function
        grays = []
        greens = {}
        yellows = {}
        # while the test word doesn't match the secret one
        while secret_word != test_word:
            test = check(secret_word, test_word)
            # use the list of colours(variable 'test' above) to make the grays, yellows and greens
            # in the test_word check the letter that corresponds to the position of 'gray' in the test list and append
            # it in the grays list
            for i in range(len(test)):
                if test[i] == 'gray':
                    grays.append(test_word[i])
                # if it's 'green' then check if the letter in the test_word that corresponds to that index has already
                # been a key in the greens dictionary.
                elif test[i] == 'green':
                    # if not then make a new entry with the letter as key and as value, a set containing an integer,
                    # corresponding to the position of that letter
                    if test_word[i] not in greens:
                        greens[test_word[i]] = {i}
                    else:
                        # if that letter has already been a key then just enter into the values' set the index it was found
                        greens_set = greens[test_word[i]]
                        greens_set.add(i)
                        greens[test_word[i]] = greens_set
                # yellows dictionary formed same way as greens' dictionary
                elif test[i] == 'yellow':
                    if test_word[i] not in yellows:
                        yellows[test_word[i]] = {i}
                    else:
                        yellows_set = yellows[test_word[i]]
                        yellows_set.add(i)
                        yellows[test_word[i]] = yellows_set
            # when the entries are done, the grays , yellows and greens are used in the find word function to find a new
            # word that matches those criteria. The new word is searched from the words list that contains all words from
            # wordles.txt
            test_word = str(find_word(words, grays, yellows, greens))
            print('trying: ' + test_word)
            print('-> ' + str(check(secret_word, test_word)))
            # everytime it's not the same increase tries by 1
            tries += 1
        else:
            # if the test word is the same as secret word
            print(secret_word + ' == ' + test_word)
            print('found in ' + str(tries) + ' tries\n')
            game_mode = input(title)
    # if the user types q on the main menu
    elif game_mode == 'q':
        print('Thank you for playing Wordle. Byee!!')
        exit()
    # if the user enters something else than 0,1 or q
    else:
        print("Invalid input\n")
        game_mode = input(title)
