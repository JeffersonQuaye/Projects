import random


def initial_balance():
    while True:
        try:
            initial_balance = int(input("Enter your initial balance: $"))
            if initial_balance <= 0:
                print("Initial balance must be a positive number.")
            else:
                return initial_balance
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_bet_amount(balance):
    while True:
        try:
            bet_amount = int(input("Enter your bet amount: $"))
            if bet_amount > balance or bet_amount <= 0:
                print(f'Invalid amuont. You can bet between $1 and ${balance}')
            else:
                return bet_amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def spin_reels():
    syymbols = ['🍒', '🍋', '🍉', '⭐', '🔔']
    return[random.choice(syymbols) for _ in range(3)]


def display_reels(reels):
    print(f'{reels[0]} | {reels[1]} | {reels[2]}')



def calculate_winnings(reels, bet):
    if reels[0] == reels[1] == reels[2]:
        return bet * 10
    if reels[0] == reels[1] or reels[0] == reels[2] or reels[1] == reels[2]:
        return bet * 2
    return 0


def main():
    balance = initial_balance()
    
    print('Welcome to the Slot Machine Game!')
    print(f'You started with a balance of ${balance}. \n')
    
    while balance > 0:
        print(f'Current balance is ${balance}.')
        
        bet = get_bet_amount(balance)
        reels = spin_reels()
        
        display_reels(reels)
        payout = calculate_winnings(reels, bet)
        
        if payout > 0:
            print(f'You won ${payout}')
        else:
            print('You lost')
        
        balance += payout - bet
        if balance <= 0:
            print('You are out of money! Game over')
            break
        
        play = input('Do you wish to continue playing? (y/n): ').lower()
        if play != 'y':
            print(f'You walk away with ${balance}.')

if __name__ == '__main__':
    main()