# Project 2 - The physics725 Word-Game (Level 1)
(This project is based on a project from MIT Open Course Ware [course 6-0001](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/))

## Introduction

This project was done as part of a masters in physics at Uni Bonn as an introduction to Python.

### Rules of the game

We start describing the (basic) rules of the game. It is a Scrabble-like game for a single player. Letters are dealt to players, who then construct one or more words using their letters. Each **valid** word earns the user points, based on the length of the word and the letters in that word.

The specific rules are as follows:
1. *Dealing and Playing*
    1. A player is dealt a hand of `HAND_SIZE` letters of the alphabet, chosen at random with rules on the distribution of consonants, vowels and jokers. This may include multiple instances of a particular letter
    2. The player arranges the hand into as many words as they want out of the letters, but using each letter at most once.
    3. Some letters may remain unused, though the size of the hand when a word is played
       does affect its score.
2. *Scoring*
    1. The score for the hand is the sum of the score for each word formed.
    2. The score for a word is the **product** of two components:
        1. First component: the sum of the points for letters in the word.
        2. Second component: either $7 w_l - 3(n - w_l)$ or 1, whichever value is greater.
           $w_l$ is the number of letters used in the word and $n$ is the number of letters available in the current hand.
    3. Letters are scored as in Scrabble; `a` is worth 1, `b` is worth 3, `c` is worth 3, `d` is worth 2, `e` is worth 1, and so on. We already have defined the dictionary `SCRABBLE_LETTER_VALUES` with those values for you.
    4. **Example:** If $n=6$ and the hand includes 1 `w`, 2 `e`s, and 1 `d` (as well as two other letters), playing the word `weed` would be worth 176 points: $(4+1+1+2) \cdot (7\cdot 4 - 3\cdot(6-4)) = 176$. The first term is the sum of the values of each letter used; the second term is the special computation that rewards a player for playing a longer word, and penalizes them for any left over letters.
