# I assume that inputs that I was not asked to check for correctness will be entered correctly,
# such as the file path that I assume will be placed in the same folder and then there will be no uses of \n or \t.
# I assume a number will be typed for the index.

def print_start_game(MAX_TRIES):
    """ The function accepts the number of attempts as input 
    and prints the opening screen
    :param MAX_TRIES: maximum number of user attempts
    :type MAX_TRIES: int
    """
    HANGMAN_ASCII_ART = "  _    _\n | |  | |\n | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __\n |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ \n | |  | | (_| | | | | (_| | | | | | | (_| | | | |\n |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n                      __/ |\n                     |___/\n"
    print(HANGMAN_ASCII_ART,MAX_TRIES,"\n")

def check_valid_input(letter_guessed, old_letters_guessed):
    """ A Boolean function that receives a character and a list of letters
    that the user has previously guessed. The function checks two things: 
    1. the correctness of the input 
    2. whether it is legal to guess the letter
    :param letter_guessed: maximum number of user attempts
    :param old_letters_guessed: maximum number of user attempts
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True or False depending on whether the 2 conditions are met
    :rtype: bool
    """
    if(len(letter_guessed) == 1 and letter_guessed.isalpha() and (letter_guessed.lower() not in old_letters_guessed)):
	    return True
    else:
        return False

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """ The function uses the check_valid_input function to know if the character is valid.
    If the character is invalid or guessed before, the function prints the character X, below it the list of letters
    that have already been guessed and returns false. 
    If the character is valid and has not been guessed before - the function adds the character to the guess list and returns true.
    :param letter_guessed: maximum number of user attempts
    :param old_letters_guessed: maximum number of user attempts
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: If the character is invalid - False, if valid - True
    :rtype: bool
    """
    if(check_valid_input(letter_guessed, old_letters_guessed)):
        old_letters_guessed.append(letter_guessed.lower())
        old_letters_guessed.sort()
        return True
    else:
        print("X")
        old_letters_guessed.sort()
        print(' -> '.join(list(old_letters_guessed)))
        return False

def show_hidden_word(secret_word, old_letters_guessed):
    """ Prints the secret word with the '_' sign instead of the not yet guessed letters
    :param secret_word: the word that the user need to guess
    :param old_letters_guessed: maximum number of user attempts
    :type secret_word: str
    :type old_letters_guessed: list
    """
    ans = ["_"] * len(secret_word) #Initialize a list of '_' depending on the length of the secret word
    for i in range(len(old_letters_guessed)):
        for j in range(len(secret_word)):
            if(old_letters_guessed[i] == secret_word[j]):
                ans[j] = secret_word[j] #If a guessed letter appears in the secret word the '_' will be replaced by this letter           
    print(" ".join(ans)) #Print the list with spaces

def check_win(secret_word, old_letters_guessed):
    """ A Boolean function that  check if the user win 
    :param secret_word: the word that the user need to guess
    :param old_letters_guessed: maximum number of user attempts
    :type secret_word: str
    :type old_letters_guessed: list
    :return: True - if all the letters of the secret word were guessed by the user.
    Otherwise, the function returns False.
    :rtype: bool
    """
    for i in range(len(secret_word)):
        if(secret_word[i] not in old_letters_guessed):
            return False
    return True        

def print_hangman(num_of_tries):
    """ Prints the condition of the hangman according to the number of attempts
    :param num_of_tries: number of user attempts
    :type num_of_tries: int
    """
    HANGMAN_PHOTOS = {0: "\n    x-------x\n",1: ":(\n    x-------x\n    |\n    |\n    |\n    |\n    |\n",2: ":(\n    x-------x\n    |       |\n    |       0\n    |\n    |\n    |\n",3: ":(\n    x-------x\n    |       |\n    |       0\n    |       |\n    |\n    |\n",4: ":(\n    x-------x\n    |       |\n    |       0\n    |      /|\ \n    |\n    |\n",5: ":(\n    x-------x\n    |       |\n    |       0\n    |      /|\ \n    |      /\n    |\n",6: ":(\n    x-------x\n    |       |\n    |       0\n    |      /|\ \n    |      / \ \n    |\n"}
    print(HANGMAN_PHOTOS[num_of_tries])

def choose_word(file_path, index):
    """ Gets path to a file and index, 
    calculates how many different words are in the file
    returns the word located in the same index in the file (index starts from 1 and not from 0)
    :param file_path: file path that entered by the user
    :param index: the place of the word in the file
    :type file_path: str
    :type index: int
    :return: the selected word from file
    :rtype: str
    """
    file_object = open(file_path, 'r')
    file_data = file_object.read()
    words_spllited = file_data.split(" ")
    file_object.close()
    
    dif_words = len(list(set(words_spllited))) #how many different words
    
    the_word = ""
    if((index - 1) < len(words_spllited)):
        the_word = words_spllited[index - 1]
    while (index - 1) >= len(words_spllited): #Reaching the index in a circular way
        index = index - len(words_spllited)
        if((index - 1) < len(words_spllited)):
            the_word = words_spllited[index - 1]
    return the_word.lower()
    
def main():
    MAX_TRIES = 6 #I have defined it as global variable because the main use it and additional functions use it too
    num_of_tries = 0 # Initialize the number of attempts
    old_letters = [] # Initialize the list of words guessed by the user
    print_start_game(MAX_TRIES)
    file_path = input("Enter file path: ")
    index = int(input("Enter index: "))
    secret_word = choose_word(file_path, index)
    secret_word = secret_word.lower() # lower the letters of the secret word
    print("\nLet’s start!")
    print_hangman(num_of_tries) #initial possition - 0 tries
    show_hidden_word(secret_word, old_letters) #initial word - only '_' signs
    while (num_of_tries < MAX_TRIES): #As long as the user has not reached the maximum number of attempts - GAME ON
        letter_guessed = input("Guess a letter: ")
        if(try_update_letter_guessed(letter_guessed, old_letters)): #if the letter is valid
            if(letter_guessed.lower() not in secret_word): #It's considered as "try" only if the letter valid, hasn't been guessed yet and doesn't appear in the secret word
                num_of_tries += 1
                print_hangman(num_of_tries)
            show_hidden_word(secret_word, old_letters)
        if(check_win(secret_word, old_letters)):
            print("\nBRAVO\nYOU WON !!!")
            break
        elif(num_of_tries == MAX_TRIES):
            print("YOU LOSE")

if __name__ == "__main__":
    main()

# NOAM SHNEOR 312350531


