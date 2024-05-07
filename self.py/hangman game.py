import random

# GLOBAL VARIABLES
MAX_TRIES = 6
COLORS = ['\033[37m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m','\033[93m', '\033[95m', '\033[96m']
COLOR = random.choice(COLORS)
HANGMAN_PHOTOS = {0:"    x-------x",1: """    x-------x
    |
    |
    |
    |
    |
""",2: """    x-------x
    |       |
    |       0
    |
    |
    |""", 3:"""    x-------x
    |       |
    |       0
    |       |
    |
    |""",4: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""",5: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""",6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}

# FUNCTIONS
def print_hangman(num_of_tries):
    """Prints the current state of the hangman.
    :param num_of_tries: how many wrong guesses has the player had
    :type num_of_tries: int
    :return: None
    """
    print(HANGMAN_PHOTOS[num_of_tries])

def print_opening_screen():
    """Prints the opening screen of the game.
    :return: None
    """
    HANGMAN_ASCII_ART = """Welcome to the game Hangman
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/"""
    print(f"{HANGMAN_ASCII_ART}\n{MAX_TRIES}\nTo clear screen, type CLEAR")

def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks if the player guess is a valid guess
    :param letter_guessed: the user's guess
    :param old_letters_guessed: the user's past guess
    :type letter_guessed: string
    :type old_letters_guessed: list of strings
    :return: 0- invalid guess, 1- valid guess, 2- guessed before
    :rtype: int
    """
    if len(letter_guessed) > 1 or not letter_guessed.isalpha():
        return 0 # invalid guess.
    if letter_guessed.lower() in old_letters_guessed:
        return 2 # valid guess but has already been guessed.
    return 1 # valid guess and not guessed before.

def check_win(secret_word, old_letters_guessed):
    """Checks if the player has guessed all the letters of the secret word.
    :param letter_guessed: the user's guess
    :param old_letters_guessed: the user's past guess
    :type letter_guessed: string
    :type old_letters_guessed: list of strings
    :return: True if the player won, else otherwise.
    :rtype: bool
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

def show_hidden_word(secret_word, old_letters_guessed):
    """Print the progress tof guessing the hidden word.
    :param letter_guessed: the user's guess
    :param old_letters_guessed: the user's past guess
    :type letter_guessed: string
    :type old_letters_guessed: list of strings
    :return: None.
    """
    progress = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            progress += COLOR + letter + " " + '\033[0m'
        else:
            progress += "_ "
    print(progress)

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Tries to add the guess to the old guesses.
    :param letter_guessed: the user's guess
    :param old_letters_guessed: the user's past guess
    :type letter_guessed: string
    :type old_letters_guessed: list of strings
    :return: 0- invalid guess, 1- valid guess and guess added to list, 2- guessed before
    :rtype: int
    """
    result = check_valid_input(letter_guessed,old_letters_guessed)
    if result == 1: # if guess is valid, add to previous guesses
        old_letters_guessed.append(letter_guessed)
    elif result == 0: # if guess isn't valid, print X
        print("X")
    return result

def choose_word(file_path, index):
    """Chooses the secret word according to the players choices.
    :param file_path: the file path of the words
    :param index: the position of the secret word in the file
    :type file_path: string
    :type index: int
    :return: the secret word.
    :rtype: string
    """
    while True: # don't continue until correct file path is provided
        try:
            with open(file_path,"r") as file:
                file_data = file.read()
                break
        except:
            file_path = input("It look like you entered a wrong file path..... Please enter a correct one: ")

    words = file_data.split(" ")
    i=0
    while index>1:
        if i+1==len(words):
            i=0
        else:
            i+=1
        index-=1
    return words[i]

def check_guess(guess, secret_word):
    """Checks if the user's guess is correct.
    :param guess: the users guess.
    :param secret_word: the secret word
    :type guess: string
    :type secret_word: string
    :return: True is guess is correct, false otherside
    :rtype: bool
    """
    return guess.lower() in secret_word or guess.upper() in secret_word

def print_previous_guesses(old_letters_guessed):
    """Print user's past guesses.
    :param old_letters_guessed: the user's past guess.
    :type old_letters_guessed: list of strings
    :return: None
    """
    print(f"{' -> '.join(old_letters_guessed)}")

def incorrect_guess(num_of_tries):
    """Prints hangman status.
    :param num_of_tries: the amount of mistakes the user's made.
    :type num_of_tries: int
    :return: None
    """
    print(":(")
    print_hangman(num_of_tries)

def main():
    """This is the main function of the game.
    :return: None
    """
    print_opening_screen()
    file_path = input("Enter file path: ")
    index = int(input("Enter index: "))
    secret_word = choose_word(file_path, index)
    num_of_tries = 0
    old_letters_guessed = []
    print("Lets start!")
    print_hangman(num_of_tries)
    show_hidden_word(secret_word,old_letters_guessed)
    while True:
        if check_win(secret_word,old_letters_guessed):
            print("WIN")
            break
        if num_of_tries == MAX_TRIES:
            print("LOSE")
            break
        guess = input("Guess a letter: ")
        result = try_update_letter_guessed(guess,old_letters_guessed) # Check if guess valid and add to previous guesses
        if result == 1: # if guess if valid
            if check_guess(guess,secret_word): # Check if guess is correct
                show_hidden_word(secret_word,old_letters_guessed) # Show the new progress of the hidden word
            else: # If guess isn't correct
                num_of_tries += 1
                incorrect_guess(num_of_tries) # print current state of hangman
        elif result == 2: # if guess has been guessed before
            print_previous_guesses(old_letters_guessed) # print previous guesses


if __name__ == "__main__":
    main()
