import random

number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print('Too high! Try again.')
    elif guess == number:
        print(f'Congratulations! You guessed the number {number} in {attempts} attempts.')
        break
    