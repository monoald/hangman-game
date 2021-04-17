from random import randint
from random import seed
from os import system


def get_word():
    """Get a random word from our data.

    Returns:
    string: Word to guess
    """
    with open('./words/data.txt', 'r', encoding='utf-8') as f:
        words = dict(enumerate(f))
        
    # Choose a random number
        seed()
        number = randint(0, len(words))

    # Get word
        word = words.get(number)
        word = word.replace('\n', '')

    return word 


def normalize(word):
    """Quite accent marks from word.

    Args:
    word (str): Word to operate

    Returns:
    str: Word without accent marks
    """
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )

    for to_replace, replacement in replacements:
        word = word.replace(to_replace, replacement)
    return word


def hide(word):
    """Hide word with '-' instead letters.

    Args:
    word (str): Word to guess

    Returns:
    list str: Hidden word with '-'
    """
    word_length = len(word)

    hidden_word_list = ['-' for letter in range(word_length)]

    return hidden_word_list


def replace_letter(character, word, normalized_word, word_list):
    """Replace the correct letter in its respective place.

    Args:
    char (str): Single character
    word (str): Word to guess
    word_list (str): List with every letter of word as element

    Returns:
    list str: word_list with their respective letters
    """
    counter = 0

    for letter in normalized_word:

        if letter == character:
            word_list[counter] = word[counter]

        counter += 1

    return word_list


def hangman_draw(lines):
    """Draw the hangman.

    Args:
    lines (int): number of elements to draw

    Returns:
    str: Hangman parts according to number of lines
    """

    title = """
    █░█ ▄▀█ █▄░█ █▀▀ █▀▄▀█ ▄▀█ █▄░█
    █▀█ █▀█ █░▀█ █▄█ █░▀░█ █▀█ █░▀█
    """

    rope = """
    ================
                  ||
"""

    head = """                ------
               / 0  0 \\
              (   --   )
               \\______/
    """

    arms = """           ===||===
              //  ||  \\\\
             //   ||   \\\\
           -..-   ||   -..-
    """

    legs = """             //\\\\
                //  \\\\
               (_)  (_)
    """

    hangman = [title, rope, head, arms, legs]

    show = ''

    for i in range(lines):
        show += hangman[i]

    return show


def lose():
    """Preapre the message when the user lose the game.

    Returns:
    str: Lose message
    """
    you_lose = """
    █░█ ▄▀█ █▄░█ █▀▀ █▀▄▀█ ▄▀█ █▄░█
    █▀█ █▀█ █░▀█ █▄█ █░▀░█ █▀█ █░▀█
               ------
              / X  X \\
             (   o    )
              \\______/

      █▄█ █▀█ █░█   █░░ █▀█ █▀ █▀▀
      ░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄
    """
    return you_lose


def win():
    """Prepare the message when user the user wins.

    Returns:
    str: Win message
    """

    you_win = """
    █░█ ▄▀█ █▄░█ █▀▀ █▀▄▀█ ▄▀█ █▄░█
    █▀█ █▀█ █░▀█ █▄█ █░▀░█ █▀█ █░▀█
                ------
              / 0  0 \\
             (  '--'  )
              \\______/
              
      █▄█ █▀█ █░█   █░█░█ █ █▄░█
      ░█░ █▄█ █▄█   ▀▄▀▄▀ █ █░▀█
    """
    return you_win


def main():

    # Get random word from data.txt
    word = get_word()

    # Remove accents
    normalized_word = normalize(word)

    # Prepare word
    hidden_word_list = hide(word)
    hidden_word = ''.join(hidden_word_list)

    # Initialize body_parts
    body_parts = 1

    # List to save the letters entered by user
    entered_letters = []

    # Check if letter is in the word
    verify_letter = lambda letter, word: letter in word

    letter_in_word = 'r'

    # Clear terminal
    system('clear')

    # Game Flow
    while True:

        print(hangman_draw(body_parts))

        print(word)
        print(letter_in_word)
        print(body_parts)

        # Runed out of lives
        if body_parts == 5:
            # Clear terminal
            system('clear')

            print(lose())
            break
            
        try:
            # Print interface
            print('Guess the word!!')
            print(hidden_word)

            # Ask the user for a letter 
            letter = input('Enter a letter: ')

            # Raise an error if the user enters a number or a symbol
            if letter.isalpha() == False:
                raise TypeError('You must enter a letter or try to guess the word')

            # Raise an error if the user don't enter a single character or a word with the same length of word
            if len(letter) > 1 and len(letter) != len(word):
                raise Exception('You must enter a single letter or try to guess the word')
            
            # Raise an error when the user enter a letter that already was entered
            if letter in entered_letters:
                raise Warning(f'You already entered the letter "{letter}"')
            else:
                # Save entered letter
                entered_letters.append(letter)

            # Check if the user try to guess the word
            # If user guessed the word the game ends
            if letter == normalized_word:
                # Clear terminal
                system('clear')
                
                print(win())
                break

            # Verify if the letter is in the word
            letter_in_word = verify_letter(letter, normalized_word)

            if letter_in_word:
                # Replace letter in their respective place
                hidden_word_list = replace_letter(letter, word, normalized_word, hidden_word_list)
                hidden_word = ''.join(hidden_word_list)
            else:
                # Add body man in hangman
                body_parts += 1

            # If each letter was guessed correctly the user wins
            if hidden_word == word:
                # Clear terminal
                system('clear')

                print(win())
                break

            # Clear terminal
            system('clear')
                
        except TypeError as te:
            # Clear terminal
            system('clear')

            print(te)
        
        except Exception as e:
            # Clear terminal
            system('clear')

            print(e)

        except Warning as w:
            # Clear terminal
            system('clear')

            print(w)
    

if __name__ == '__main__':
    main()