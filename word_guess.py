import random

LEXICON_FILE = "TestLexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8            # Initial number of guesses player starts with


def get_word():
    """
    This function returns a random word from a file called Lexicon.txt that the player will be asked
    to guess to win the game."""
    with open(LEXICON_FILE, 'r') as file:
        lines = file.readlines()
        count = len(lines)
        index = random.randrange(count)
        word = lines[index].strip()
        return word


def play_game(secret_word):
    """
    This function asks the player to guess the secret word and
    it then compares the letter keyed in by the player with secret word.
    If all the letter matches, it will declare the user as winner and if the letter
    doesn't match, it will ask the user to guess till they find the right word or till the
    guess limit - if no more guesses left, it will announce that they have lost the game.
    """
    print(secret_word)  # THIS IS ONLY FOR ILLUSTRATION PURPOSE AND SHOULD BE DELETED WHEN YOU WANT SOMEONE TO GUESS
    print("The word now looks like this: " + "_" * len(secret_word))
    print("You have " + str(INITIAL_GUESSES) + " guesses left")
    count = INITIAL_GUESSES
    success_char = []
    while count > 0:
        user_guess = input("Type a single letter here, then press enter: ")
        user_guess = user_guess.upper()
        listed = ''.join([c if c in success_char else "_" for c in secret_word])
        # the above line replaces the "-" with the guessed letter, if the guess words are found in the secret words
        if len(user_guess) > 1 or user_guess == "":
            print("Guess should only be a single character.")
            print("The word now looks like this: " + str(listed))
            print("You have " + str(count) + " guesses left")
        elif user_guess not in secret_word:
            count -= 1
            print("There are no " + str(user_guess) + "'s in the word")
            if count == 0:
                print("Sorry, you lost. The secret word was: " + str(secret_word))
            else:
                print("You have " + str(count) + " guesses left")
                print("The word now looks like this: " + str(listed))
        else:
            print("The guess is correct")
            if user_guess not in success_char:
                success_char.append(user_guess)
            listed = ''.join([c if c in success_char else '_' for c in secret_word])
            # the above line replaces the "-" with the guessed letter, if the guess words are found in the secret words
            if set(success_char[:]) == set(secret_word[:]):
                print("Congratulations, the word is: " + str(secret_word))
                break
            print("You have " + str(count) + " guesses left")
            print("The word now looks like this: " + str(listed))

"""
This program get's a random secret word from the Lexicon File and 
and prompts the players to key in the right letter till all the letter are found or
till the guess count and declare as winner if the all the keyed in letters matches the 
secret word or declare as loser if there is no more guesses left
"""


def main():
    secret_word = get_word()
    play_game(secret_word)


if __name__ == "__main__":
    main()