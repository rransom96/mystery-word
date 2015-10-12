import random
import re


def space_remover(phrase):
    """ Removes the punctuation from the string"""
    return re.sub(r'[^A-Za-z\n]', "", phrase)


def easy_words(word_list):
    easy_words = list(filter((lambda words: 4 <= len(words) <= 6),
                             word_list))
    return easy_words


def medium_words(word_list):
    medium_words = list(filter((lambda words: 6 <= len(words) <= 8),
                               word_list))
    return medium_words


def hard_words(word_list):
    hard_words = list(filter((lambda words: 8 <= len(words) <= 24),
                             word_list))
    return hard_words


def random_word(word_list):
    return random.choice(word_list)


def pick_difficulty(difficulty):
    choice = ""
    while choice == "":
        if difficulty.lower()[0] == "e":
            choice = random_word(easy_words)
            print("Easy Mode, word length: {}".format(len(choice)))
        elif difficulty.lower()[0] == "n":
            choice = random_word(medium_words)
            print("Normal Mode, word length: {}".format(len(choice)))
        elif difficulty.lower()[0] == "h":
            choice = random_word(hard_words)
            print("Hard Mode, word length: {}".format(len(choice)))
        else:
            difficulty = input("Easy Mode, Normal Mode, or Hard Mode!")
            return pick_difficulty(difficulty)
    return choice


def display_word(word, letters_in_word):
    blanks = "_" * len(word)
    letters_in_word = [letters_in_word]
    already_guessed = []
    turns = 8
    # while turns >= 1:
    #     for letters in range(len(word)):
    #         if word[letters] in letters_in_word:
    #             blanks = blanks[:letters] + word[letters] + blanks[letters+1:]
    #     if "_" not in blanks:
    #         break
    #     for letters in blanks:
    #         print(letters, end=" ")
    #     print()
    #     guess = input("Guess a letter.")
    #     if len(guess) > 1:
    #         print("One guess per turn... Enter ONE letter: ")
    #     elif guess in word:
    #         letters_in_word = letters_in_word + [guess]
    #         return display_word(word, letters_in_word)
    #     elif guess not in "abcdefghijklmnopqrstuvwxyz":
    #         print("Thats not a letter... Guess a LETTER: ")
    #     else:
    #         print("{} is not in the word :(. Try again...".format(guess))
    #         turns -= 1
    # return blanks
    while turns >= 1:
        print("Number of guesses left: {}".format(turns))
        for letters in blanks:
            print(letters, end=" ")
        print()
        guess = input("Guess a letter: ")
        already_guessed = already_guessed + [guess]
        if len(guess) > 1:
            print("One guess per turn... Enter ONE letter: ")
        elif guess in word:
            letters_in_word = letters_in_word + [guess]
            for letters in range(len(word)):
                if word[letters] in letters_in_word:
                    blanks = blanks[:letters] + word[letters] + blanks[letters+1:]
            if "_" not in blanks:
                break
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Thats not a letter... Guess a LETTER: ")
        else:
            print("{} is not in the word :(. Try again...".format(guess))
            turns -= 1
    return blanks




if __name__ == '__main__':
    while True:
        with open("/usr/share/dict/words") as word_list:
            word_list = word_list.read()
            word_list = space_remover(word_list)
            word_list = word_list.lower().split()
        easy_words = easy_words(word_list)
        medium_words = medium_words(word_list)
        hard_words = hard_words(word_list)
        difficulty = input("Easy Mode, Normal Mode, or Hard Mode? ")
        word = pick_difficulty(difficulty)
        letters = []
        answer = display_word(word, letters)
        if "_" not in answer:
            print("you won")
        else:
            print("you lose")
        again = input("play again (yes/no)")
        if "yes":
            continue
        else:
            break


