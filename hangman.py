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
    word (str): word to guess

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
    word_list (str): list with every letter of word as element

    Returns:
    list str: word_list with their respective letters
    """
    counter = 0

    for letter in normalized_word:

        if letter == character:
            word_list[counter] = word[counter]

        counter += 1

    return word_list
        


def main():

    # Get random word from data.txt
    word = get_word()

    # Remove accents
    normalized_word = normalize(word)

    print(word)

    # Prepare word
    hidden_word_list = hide(word)
    hidden_word = ''.join(hidden_word_list)

    # Check if letter is in the word
    verify_letter = lambda letter, word: letter in word

    # Game Flow
    while True:

        try:
            # Print interface
            print('Guess the word!!')
            print(hidden_word)

            # Ask the user for a letter 
            letter = input('Enter a letter: ')

            # Raise an error if the user enters a number or a symbol
            if letter.isalpha() == False:
                raise ValueError('You must enter a letter or the word')

            # Raise an error if the user don't enter a single character or a word with the same length of word
            if len(letter) > 1 and len(letter) != len(word):
                raise Exception('You must enter a single letter or the word')

            # Verify if the letter is in the word
            letter_in_word = verify_letter(letter, normalized_word)

            if letter_in_word:
                print(letter)
                hidden_word_list = replace_letter(letter, word, normalized_word, hidden_word_list)
                hidden_word = ''.join(hidden_word_list)
                


            #system('clear')
            if letter == word:
                break
        except ValueError as ve:
            print(ve)
        
        except Exception as e:
            print(e)
    

if __name__ == '__main__':
    main()