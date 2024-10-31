import math
import requests
exchange_rates = requests.get(f"https://v6.exchangerate-api.com/v6/563e25d8fd79beb0902357d5/latest/GBP").json()
currencies = exchange_rates['conversion_rates']

def getexch():
    Type = input("What currency would you like to convert the price to in the format (GBP): ")
    while Type not in currencies:
        print("Invalid Input")
        Type == input("Enter a Valid Currency.")
    return Type
def currency(amount,exh):
    return round(currencies[exh]*float(amount),2)
    if float(amount) < 10.0:
        print("That is too little to convert.")
        quit()
    elif float(amount) > 1000.0:
        print("That is too much to convert.")
        quit()
    else:
        return round(currencies[exh]*float(amount),2)
    
#print(currency_convert(77.99))