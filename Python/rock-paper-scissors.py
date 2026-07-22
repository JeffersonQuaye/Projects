from random import choice

while True:
    emoji = {
        'r':'🪨',
        's':'✂️',
        'p':'📃'
    }
    choices = ('r', 'p', 's')

    user_option = input('Rock, paper or scissors (r/p/s)?: ').lower()
    if user_option not in choices:
        print('Invalid Choice!')
        continue

    computer_options = choice(choices)

    print(f'You chose {emoji[user_option]}')
    print(f'Computer chose {emoji[computer_options]}')

    if user_option == computer_options:
        print('Tie')
    elif (user_option == 'r' and computer_options == 's') or (user_option == 'p' and computer_options == 'r') or (user_option == 's' and computer_options == 'p'):
        print('You win!')
    else:
        print('Computer wins!')

    play = input('Do you want to continue? (y/n): ').lower()
    if play == 'y':
        continue
    else:
        print('Thanks for playing!')
        break