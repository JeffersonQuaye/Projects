print("Currency Converter")

def convert_input():
    while True:
        try:
            amount = float(input('Enter the amount: '))
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_currency(label):
    currencies = ("USD", "EUR", "GBP")
    while True:
        currency = input(f'{label} currency (USD, EUR, GBP): ').upper()
        if currency not in currencies:
            print("Invalid currency. Please enter a valid currency (USD, EUR, GBP).")
        else:
            return currency


def conversion(amount, source, target):
    # if source == target:
        #     print("Source and target currencies cannot be the same.")
        #     continue
        # elif source == "USD" and target == "EUR":
        #     converted_amount = amount * 0.85
        # elif source == "USD" and target == "GBP":
        #     converted_amount = amount * 0.75
        # elif source == "EUR" and target == "USD":
        #     converted_amount = amount * 1.18
        # elif source == "EUR" and target == "GBP":
        #     converted_amount = amount * 0.88
        # elif source == "GBP" and target == "USD":
        #     converted_amount = amount * 1.33
        # elif source == "GBP" and target == "EUR":
        #     converted_amount = amount * 1.14
            
    exchange_rates = {
        'USD': {'EUR': 0.85, 'GBP': 0.75},
        'EUR': {'USD': 1.18, 'GBP': 0.88},
        'GBP': {'USD': 1.33, 'EUR': 1.14}
    }
        
    if source == target:
        print("Source and target currencies cannot be the same.")
    
    return amount * exchange_rates[source][target]

def main():
    amount = convert_input()
    source = get_currency("Source")
    target = get_currency("Target")
    converted_amount = conversion(amount, source, target)
    print(f"{amount} {source} = {converted_amount:.2f} {target}")

main()