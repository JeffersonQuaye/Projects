class ATM:
    def __init__(self):
        self.balance = 0

    
    def check_balance(self):
        return self.balance

    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit must be positive')
        self.balance += amount

            
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Insufficient Funds')
        if amount <= 0:
            raise ValueError('Withdrawal amount must be positive') 
        self.balance -= amount


class ATM_UI:
    def __init__(self):
        self.atm = ATM()
        
        
    def get_number(self, prompt):
        while True:
            try:
                number = float(input(prompt))
                return number
            except ValueError:
                print('Please enter a valid number')
    
    
    def menu(self):
        print('\nWelcome to the ATM!')
        print('1. Check Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')
        
    
    def make_depoosit(self):
        while True:
                try:
                    amount = self.get_number('Enter deposit amount: ')
                    self.atm.deposit(amount)
                    print(f'Successfully deposited ${amount}.')
                    break
                except ValueError as e:
                    print(e)
    
    
    def make_withdrawal(self):
        while True:
                try:
                    amount = self.get_number('Enter withdrawal amount: ')
                    self.atm.withdraw(amount)
                    print(f'Successfully withdrew ${amount}.')
                    break
                except ValueError as e:
                    print(e)
            
    
    def run(self):
        while True:
            self.menu()
            
            choice = input('Please select an option: ')
            
            if choice == '1':
                print(f'Your current balamce is: ${self.atm.check_balance()}')
            elif choice == '2':
                self.make_depoosit()
            elif choice == '3':
                self.make_withdrawal()
            elif choice == '4':
                print('Thank you for using the ATM.')
                break
            else:
                print('Invalid option. Please try again.')
        

def main():
   atm = ATM_UI()
   atm.run()


if __name__ == '__main__':
    main()