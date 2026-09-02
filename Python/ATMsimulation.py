class ATM:
    def __init__(self):
        self.balance = 0
    
    def check_balance(self):
        print(f'Your currnet balance is ${self.balance}')
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Successfully deposited ${amount}.')
        else:
            print('Deposit amount must be positive.')
            
    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds.')
        elif amount <= 0:
            print('Withdrawal amount must be positive.')
        else:
            self.balance -= amount
            print(f'Successfully withdrew ${amount}.')
            

def main():
   atm = ATM()
   while True:
       print('\nWelcome to the ATM!')
       print('1. Check Balance')
       print('2. Deposit')
       print('3. Withdraw')
       print('4. Exit')
       
       choice = input('Please select an option: ')
       
       if choice == '1':
           atm.check_balance()
       elif choice == '2':
           while True:
                try:
                    amount = float(input('Enter deposit amount: '))
                    atm.deposit(amount)
                    break
                except ValueError:
                    print('Invalid input. Please enter a valid number')
       elif choice == '3':
           while True:
                try:
                    amount = float(input('Enter withdrawal amount: '))
                    atm.withdraw(amount)
                    break
                except ValueError:
                    print('Invalid input. Please enter a valid number')
       elif choice == '4':
           print('Thank you for using the ATM.')
           break
       else:
           print('Invalid option. Please try again.')

if __name__ == '__main__':
    main()