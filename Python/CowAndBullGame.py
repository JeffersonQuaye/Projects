import random

def secret_number():
    digit = list(range(10))
    random.shuffle(digit)
    return ''.join([str(digit) for digit in digit[:4]])

    
def calc_cows_and_bull(secret, guess):
    cows = sum([1 for i in range(4) if guess[i] in secret])
    bulls = sum([1 for i in range(4) if guess[i] == secret[i] and guess[i] != secret[i]])
    
    return cows, bulls

def main():
    secret = secret_number()
    while True:
        guess = input('Guess: ')
        if len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4:
            cows, bulls = calc_cows_and_bull(secret, guess)
            print(f'Cows: {cows}, Bulls: {bulls}')
            if bulls == 4:
                print('Congratulations! You guessed the secret number.')
                break
        else:
            print('Invalid guess. Please enter a 4-digit number with unique digits.')
    
if __name__ == '__main__':
    main()