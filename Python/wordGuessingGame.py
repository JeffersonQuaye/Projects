import random
import re

def read_words():
    try:
        with open('words.txt', 'r') as file:
            word = file.read().splitlines()
            return word
    except FileNotFoundError:
        print('words.txt does not exist.')
        return []


def display_word(secret_word, guessed_letters):
    word_to_display = ''
    
    
    for letter in secret_word:
        if letter in guessed_letters:
            word_to_display += letter
        else:
            word_to_display += '_'
        print(word_to_display)


def user_input(guessed_letters):
    while True:
        guess = input('Guess a letter: ').lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif re.search('[a-z]', guess):
            print('Please enter only letter from a to z.')
        elif guess in guessed_letters:
            print('You have already guessed that letter.')
        else:
            return guess


def is_word_guessed(secret_word, guessed_letters):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True
    


def main():
    words = read_words()
    if not words:
        print('No words available')
        return
    secret_word = random.choice(words)
    print(secret_word)
    
    attempts = 6
    
    guessed_letters = []
    while attempts > 0:
        display_word(secret_word, guessed_letters)
        
        guess = user_input(guessed_letters)
        guessed_letters.append(guess)
        
        if guess in secret_word:
            print('Good guess')
            if is_word_guessed(secret_word, guessed_letters):
                print('Congratulations! You guessed the word:')
                break
        else:
            print('Wrong guess')
            attempts -= 1
            if attempts == 0:
                print(f'Game over! The word was: {secret_word}')
                break


if __name__ == '__main__':
    main()