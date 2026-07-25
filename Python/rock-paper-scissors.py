from random import choice

emoji = {
        'r':'🪨',
        's':'✂️',
        'p':'📃'
    }
choices = tuple(emoji.keys())

def get_user_choice():
    while True:
        user_option = input('Rock, paper or scissors (r/p/s)?: ').lower()
        if user_option in choices:
            return user_option
        else:
            print('Invalid Choice!')

def display_choices(user_option, computer_options):
    print(f'You chose {emoji[user_option]}')
    print(f'Computer chose {emoji[computer_options]}')

def determine_winner(user_option, computer_options):
    if user_option == computer_options:
        print('Tie')
    elif (user_option == 'r' and computer_options == 's') or (user_option == 'p' and computer_options == 'r') or (user_option == 's' and computer_options == 'p'):
        print('You win!')
    else:
        print('Computer wins!')
    
def play_game():
    while True:
        user_option = get_user_choice()
        
        computer_options = choice(choices)
        
        display_choices(user_option, computer_options)
        
        determine_winner(user_option, computer_options)

        play = input('Do you want to continue? (y/n): ').lower()
        if play == 'y':
            continue
        else:
            print('Thanks for playing!')
            break
        
play_game()0