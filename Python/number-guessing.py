import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Guess a number between 1 and 100: ")
    attempts += 1
    
    if not guess.isdigit():
        print("Please enter a valid number.")
    elif int(guess) < number:
        print("Too low! Try again.")
    elif int(guess) > number:
        print('Too high! Try again.')
    elif int(guess) == number:
        print(f'Congratulations! You guessed the number {number} in {attempts} attempts.')
        break
    