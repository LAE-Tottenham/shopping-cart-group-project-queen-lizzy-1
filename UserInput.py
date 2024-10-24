import requests
def Items():
    Items = {
    'Bread': 1.20,
    'Milk': 1.15,
    'Chocoloate': 0.50,
    'Water': 1,
    'Eggs': 1.75,
    'Flour': 0.80,
    'Beans': 0.50,
    'Cereal': 2.3,
    'Chicken Wings': 1.35,
    'Orange Juice': 0.95,
}
    print("Welcome to the store we currently sell: Bread, Milk, Chocolate, Water, Eggs, Flour, Beans, Cereal, Chicken Wings, Orange Juice")
    for x in Items:
        print(f"{x} for £{Items[x]}.")
    n = 0
    Price = 0
    Basket = []
    while n == 0:
        Item = input("What items would you like to buy: ")
        if Item in Items:
            Basket.append(Item)
        choice = input("Want to continue - click any key to continue enter N if you are done shopping.").upper() 
        if choice == 'N':
            n = 1
    print(Basket)
    for x in Basket:
        if x in Items:
            Grocery = Price + Items[x]
    print(Grocery)
    for key, value in Items.items():
        if Basket.__contains__(key): 
            Grocery = Price + value 

Items() 
def postcode(): 
    postcode_raw = input("\nSo, what's your postcode? ")
    if postcode_raw == '':
        print("Please enter a postcode")
        postcode() 
    postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{postcode_raw}").json()
    area = postcode_resp['result']['admin_ward']
    longitude = postcode_resp['result']['longitude']
    latitude = postcode_resp['result']['latitude']
    print(f"Nice! so you live in {area}.\n")
    return area, longitude, latitude
postcode()
def CardType(): 
    Card = input("Would you like use Visa or Mastercard: ")
    if Card.casefold() == 'visa':
        cardtype = 'Visa'
    elif Card.casefold() == 'mastercard': 
        cardtype = 'Mastercard' 
    else:
        cardtype = 'Visa'
CardType()
