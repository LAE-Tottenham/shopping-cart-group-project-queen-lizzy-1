import math

exchange_rates = {
    'USD': 1.13,
    'EUR': 1.15,
    'CAD': 1.80,
    'INR': 109.81,
    'GHC': 20.86,
    'GBP': 1.00,
    
}
currencies = ['USD','EUR','CAD','INR','GHC']

def check_currency_exists(currency):
    if currency in currencies:
        pass
    else:
        print("Invalid Input")
        quit()

def currency_convert(original_c, new_c, amount):
    if float(amount) < 10.0:
        print("That is too little to convert.")
        quit()
    elif float(amount) > 1000.0:
        print("That is too much to convert.")
        quit()
    else:
        return round(exchange_rates[new_c]*float(amount),2)