# module for the physics 718 word game.
# Large parts of this file were obtained from
# a somilar problem of the MIT 6.0001 OCW course.

# Original file by: Kevin Luu <luuk> and Jenna Wiens <jwiens>

# YOUR NAME HER PLEASE: Mash-Huda Rahman Shipra

import math
import random

# module constants
HAND_SIZE = 10  # 'default' hand-size
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
    'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3,
    'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
    'y': 4, 'z': 10, '*': 0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words_alpha.txt"


def load_words(filename=WORDLIST_FILENAME):
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(filename, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")

    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n, letter_values=SCRABBLE_LETTER_VALUES):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of
    letters, or the empty string "". You may not assume that the
    string will only contain lowercase letters, so you will have to
    handle uppercase and mixed case strings appropriately.

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    letter_values: dict of values for lower case letters
    returns: int >= 0

    """

    wordcal = word.lower()  # lowers all the letters to match the dictionary
    wordlen = len(word)  # length of the word

    # loop for summing the letter scores
    sum1 = 0
    for i in wordcal:
        sum1 += letter_values[i]

    # checks and assigns the second part of the score
    if (7 * wordlen - 3 * (n - wordlen)) > 1:
        sum2 = (7 * wordlen - 3 * (n - wordlen))
    else:
        sum2 = 1

    # for an empty string, the for loop is not executed,
    # sum1 is taken to be zero, returning the score = 0

    return sum1 * sum2


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')  # print all on the same line
    print()  # print an empty line


#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n=HAND_SIZE, vowels=VOWELS, consonants=CONSONANTS):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    vowels: string of vowels
    consonants: string of consonants
    returns: dictionary (string -> int)
    """

    hand = {}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels - 1):  # removed one slot for vowels to be filled in by wild card
        x = random.choice(vowels)
        hand[x] = hand.get(x, 0) + 1

    hand['*'] = 1  # add wild card to hand

    for i in range(num_vowels, n):
        x = random.choice(consonants)
        hand[x] = hand.get(x, 0) + 1

    return hand


#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured).

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """

    new_hand = hand.copy()  # making a copy so the dictionary "hand" does not change

    # for loop to feed letters from word in dictionary as keys
    for i in word.lower():  # word.lower() used to avoid error if a capital letter is used
        if i not in new_hand:  # condition for avoiding error if a word outside of hand is played
            new_hand[i] = new_hand.get(i,
                                       0) + 1  # added a test case (test 4) in test_update_hand() in test_word_module.py
        new_hand[i] -= 1  # updates hand
        if new_hand[i] == 0:
            new_hand.pop(i)  # removes the letter from dictionary if all the letters have been played up
            # matches the result with expected_hand1 in text_word_module.py
    return new_hand


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    new_hand = hand.copy()  # making a copy so the dictionary "hand" does not change
    is_valid = []  # creating empty boolean list

    # for loop to check if letter in word exists in hand
    for i in word.lower():  # lowering the letter to match dictionary keys
        is_valid.append(i in new_hand)  # boolean list for letter in hand

        # creating a custom update hand to avoid error due to letter repetition
        if i in new_hand:
            new_hand[i] -= 1
            if new_hand[i] == 0:
                new_hand.pop(i)

    # condition for wild card
    check_wild_word = []  # boolean list to check existence of word in word_list
    if '*' in word:  # check for wild card in word
        for i in VOWELS:  # for loop to replace wild card with vowels
            new_word = word[:word.index('*')] + i + word[word.index('*') + 1:]
            check_wild_word.append(new_word in word_list)
        is_valid.append(any(check_wild_word))  # if any element is true, the word is valid

    # if no wild card is used
    else:
        is_valid.append(word.lower() in word_list)  # appending to boolean list check value for word in word list

    return all(is_valid)  # valid word is if all the elements in boolean list is true


#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """

    return len(hand)  # returns length of the hand dealt


def play_hand(hand, word_list, ask_replay, short_circuit = False):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """

    n = 1 if short_circuit else calculate_handlen(hand)  # caltulating size of the hand dealt
    end_requested = False
    # playing until letters left in hand or input "!!"
    total_score = 0  # will iteratively add to it after every word played
    while n > 0:
        print(f'Current hand:')
        display_hand(hand)  # shows the current hand in a separate line

        word = input("Enter word, or \"!!\" to finish this hand: ")  # input word from user

        word_score = 0  # score for every word played

        # if player inputs "!!", break the loop
        if word == '!!':
            print(f'You finished this hand. Total score {total_score}')
            end_requested = True
            break


        # Otherwise (the input is not two exclamation points):
        else:
            valid_word = is_valid_word(word, hand, word_list)

            # If the word is valid:
            if valid_word == True:
                word_score = get_word_score(word, n,
                                            letter_values=SCRABBLE_LETTER_VALUES)  # count score for played word
                print(f'\"{word}\" earned you {word_score} points')
                total_score += word_score  # count total score
                hand = update_hand(hand, word)  # update the user's hand by removing the letters of their inputted word
                # Reject with a message if the word is not valid
            else:
                print(f'Invalid word. Please enter a valid word.')

            n = len(hand)  # update the number of letters left in hand

    # shows the user the total score after each play of word
    if not end_requested:
        print(f'You finished this hand.', end=' ')
        if ask_replay:
            print(f'Current score: {total_score}.')
            wants_replay = input('Do you want to replay this hand? (y/n): ')
            if wants_replay == 'y':
                score = play_hand(deal_hand(), word_list, False, True)
                if(score > total_score):
                    score_type = 'replay'
                else:
                    score_type = 'original'
                print(f'The {score_type} score was higher and will be used as the total score for this round')
                total_score = max(score, total_score)
                print(f'Total score for this hand: {total_score}')
            elif not short_circuit:
                print(f'Current score: {total_score}')
    # Returns the total score as result of function after hand is finished
    return total_score


#
# procedure you will use to substitute a letter in a hand
# (BONUS TASK)
#

def substitute_hand(hand, letter):
    """
    Allow the user to replace all copies of one letter in the hand
    (chosen by user) with a new letter chosen from the VOWELS and
    CONSONANTS at random. The new letter should be different from
    user's choice, and should not be any of the letters already in the
    hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)

    """

    new_hand = hand.copy()

    # generates random choice of new letter from a new dictionary of avail letters after the letters in hand is removed from it
    def new_avail_letters(new_hand):
        avail_letters = list(VOWELS)
        if not avail_letters.__contains__(letter):
            avail_letters = list(CONSONANTS)

        for i in new_hand.keys():
            if avail_letters.__contains__(i):
                avail_letters.remove(i)

        return random.choice(avail_letters)

    new_letter = new_avail_letters(new_hand)  # replacing the previous letter with new letter
    print(f'New letter {new_letter}')
    new_hand[letter] -= 1  # prints out the new letter (optional)
    new_hand[new_letter] = 1  # replacing the key in hand

    return new_hand
