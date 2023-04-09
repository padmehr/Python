import random
from words import words
import string

# hangman


def get_word(words):
    word = random.choice(words)
    return word.upper()


def hangman():
    used_letters = set()
    word = get_word(words)
    word_letters = set(word)
    lives = 3
    alphabet = set(string.ascii_uppercase)
    # user input
    while len(word_letters) > 0 and lives > 0:
        print("Number of lives: " + str(lives))
        print(word)
        print("You have used these letters: " + " ".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("current word: " + " ".join(word_list))
        guess = input("enter a character: ").upper()
        print("\n")

        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                lives = lives - 1
        elif guess in used_letters:
            print("You already guess this letter")

        else:
            print("Invalid letter")

    if lives == 0:
        print("You lose!")
    else:
        print("You won!")


hangman()