import random

print('WELCOME TO THE DICE ROLL SIMULATOR!')
while True:
    roll = input('Roll the dice? (y/n): ')
    if roll.lower() == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'{dice1}, {dice2}')
    elif roll.lower() == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Invalid input. Please enter "y" or "n".')