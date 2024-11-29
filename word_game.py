# This file implements the word_game.
# Helper modules are in word_module.py

# YOUR NAME HERE PLEASE: Mash-Huda Rahman Shipra

import word_module as wm

# Playing a game is done in the following steps:

# YOU HAVE TO DO THIS according to the following
# specification.

"""
Allow the user to play a series of hands

* Asks the user to input a total number of hands

* Accumulates the score for each hand into a total score for the
  entire series

* BONUS TASK:
  For each hand, before playing, ask the user if they want to substitute
  one letter for another. If the user inputs 'yes', prompt them for their
  desired letter. This can only be done once during the game. Once the
  substitue option is used, the user should not be asked if they want to
  substitute letters in the future.

* BONUS TASK:
  For each hand, ask the user if they would like to replay the hand.
  If the user inputs 'yes', they will replay the hand and keep
  the better of the two scores for that hand.  This can only be done once
  during the game. Once the replay option is used, the user should not
  be asked if they want to replay future hands. Replaying the hand does
  not count as one of the total number of hands the user initially
  wanted to play.

* Note: if you replay a hand, you do not get the option to substitute
        a letter - you must play whatever hand you just had.

* prints the total score for the series of hands and finished the program

"""

# print welcome message and get going
print("Welcome to the physics718 word game!")
print("====================================")
print()

# load word list:
word_list = wm.load_words()

hand_size = 10               # size of a hand

hand_num = int(input("How many hands do you want to play? "))     #input from user on how many hands to play

total_score = 0              #defined to get total score after finishing the whole game (different from total_score in wm)
flag = 1                     #flag to make sure user is not asked to substitute hand in later hands after they do so once
#something = 1

#for loop to run play_hand the number of times user inputs in hand_num
for i in range(hand_num):
    hand = wm.deal_hand(n=hand_size, vowels=wm.VOWELS, consonants=wm.CONSONANTS)    #deal hands
    wm.display_hand(hand)                                                           #display the hand

    #condition to check for user requested substitute hand
    if flag:
    #if something == 1:
        def ask_input(hand):
            sub_input = input("Do you want to substitute a letter? y/n: ")

            #condition to substitute letters if the user asks
            if sub_input == 'y':
                letter = str(input("Which letter would you like to substitute? "))

                if letter in hand:
                    return wm.substitute_hand(hand, letter)
                else:
                    print("Letter is not in the hand.")
            # something = 0
            elif sub_input != 'n':
                return ask_input(hand)
            return hand

        hand = ask_input(hand)
        flag = not flag

    play_game = wm.play_hand(hand, word_list)                #playing the game
    total_score = total_score + play_game                    #calculates the total score after each hand

print(f'Total score over {hand_num} hands: {total_score}')   #prints out total score after the whole game
print(f'Game over!')                                         #message indicating the game is over to the player
