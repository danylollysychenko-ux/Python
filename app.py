import csv
import random
import os

def play_again():
    """Prompts the user to play again or quit"""
    running = True
    while running:
        print("Do you want to play again (y/n) ?: ")
        choice = input("Choice: ").lower().strip()
        
        if choice == "y":
            print("Alright lets begin!")
            running = False
        elif choice == "n":
            print("Have a good day.")
            exit()
        else:
            continue

def hangman_visual(index):
    """Hangman visual for the game"""
    hangman = [
r"""  _______
 |/      |
 |
 |
 |
 |
 |
_|___""",
r"""  _______
 |/      |
 |      (_)
 |
 |
 |
 |
_|___""",
r"""  _______
 |/      |
 |      (_)
 |       |
 |       |
 |
 |
_|___""",
r"""  _______
 |/      |
 |      (_)
 |      \|
 |       |
 |
 |
_|___""",
r"""  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |
 |
_|___
""",
r"""  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      /
 |
_|___
""",
r"""  _______
 |/      |
 |      (_)
 |      \|/
 |       |
 |      / \
 |
_|___
"""]

    return hangman[index]

def words_stored_here():
    """Stores the words that are loaded from a file into a list"""
    words = []

    with open("words.csv", "r") as f:
        csv_reader = csv.reader(f)

        for word in csv_reader:
            words.append(*word)

    return words

def generate_random_word(words):
    """Generates a random word from the list"""
    random_word = random.choice(words)
    secret_word = str(random_word)

    return  secret_word

def generate_blank_spaces(secret_word):
    """Generates the blank spaces for the game"""
    blank_spaces = ["_"] * len(secret_word)

    return blank_spaces

def get_user_guess(wrong_guesses):
    """Validates the user's guess"""
    user_guess = input("Enter a letter: ").lower().strip()
    print()

    if not user_guess.isalpha():
        print(f"Please enter only a letter only.")
        return None

    if len(user_guess) > 1:
        print("Please only type one letter at a time please.\n")
        return None

    if user_guess in wrong_guesses:
        print(f"You already guessed {user_guess}")
        return None

    return user_guess

def replace_blanks(secret_word, user_guess, blank_spaces):
    """Replaces the blanks if the user correctly guesses one or multiple of the same letters"""
    for index, letter in enumerate(secret_word):
    # Used AI for this if statement because I had something else but it does make sense.
        if letter == user_guess:
            blank_spaces[index] = user_guess

    return blank_spaces

def end_game_conditions(guesses, blank_spaces, secret_word):
    """Either ends the game or keeps the game going. Depending on what the user chooses"""
    if guesses == 0:
        print(f"You lost! The word was {secret_word.upper()}.")
        play_again()

    if "".join(blank_spaces) == secret_word:
        print("You guessed the full word great job!\n")
        play_again()

def store_wrong_guesses(user_guess, wrong_guesses, secret_word):
    """Stores the wrong guesses so if the user guesses the wrong letter a second time it would not take away the guess"""
    if user_guess not in secret_word:
        print(f"{user_guess} is not part of the word.")
        wrong_guesses.append(user_guess)

    return wrong_guesses

def intro_to_game():
    """Introduction to the game"""
    running = True
    while running:
        print("Do you want to play (y/n) ?:")
        choice = input("Choice: ").lower().strip()
        
        if choice == "y":
            print("Alright lets begin!")
            running = False
        elif choice == "n":
            print("Have a good day.")
            exit()
        else:
            continue

def main():
    """Everything put together into a functioning game"""
    hangman_index = 0
    words = words_stored_here()
    secret_word = generate_random_word(words)
    blank_spaces = generate_blank_spaces(secret_word)
    guesses = 6
    wrong_guesses = []

    intro_to_game()

    print(hangman_visual(hangman_index))
    while True:

        user_guess = get_user_guess(wrong_guesses)

        if user_guess is None:
            continue
        
        if store_wrong_guesses(user_guess, wrong_guesses, secret_word):
            guesses -= 1
            print(f"You have {guesses} guesses left.\n")
            hangman_index += 1
            print(hangman_visual(hangman_index))
        
        print(f"Incorrect guesses:", ", ".join(i.upper()
            for i in wrong_guesses))  # AI was used here

        blank_spaces = replace_blanks(secret_word, user_guess, blank_spaces)

        print()
        print(f"Word: {" ".join(blank_spaces)}")

        end_game_conditions(guesses, blank_spaces, secret_word)
        print()

if __name__ == "__main__":
    main()