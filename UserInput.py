import requests
import time
from pyfiglet import Figlet
from termcolor import colored
import pgeocode
from Accounts import *


def ListOfGoods():
   Items = {
   'Bread': 1.20,
   'Milk': 1.15,
   'Chocolate': 0.50,
   'Water': 1.00,
   'Eggs': 1.75,
   'Flour': 0.80,
   'Beans': 0.50,
   'Cereal': 2.30,
   'Chicken Wings': 1.35,
   'Orange Juice': 0.90,
}
   return Items



def Intro():
   f = Figlet(font="slant")
   x = f.renderText("HELLO!")
   y = colored(x, "blue" , attrs=['bold'])
   print(y)
   print("Welcome to Queen Lizzys Online Supermarket!")
   print("-----------------------------------\n")
   time.sleep(1.5) 


def ItemPrinter():
   f = Figlet(font="slant")
   x = f.renderText("SHOP!")
   y = colored(x, "blue" , attrs=['bold'])
   print(y)
   Items = ListOfGoods()
   for x in Items:
       print(f"{x} for the price of £{Items[x]}")
   time.sleep(1.5)


def options():
    print("How can we help?\nLog In (L)\nView Account(V)\nSign Up (SU)\nShop (S)\nQuit(ANY OTHER KEY)")
    choice = input("Enter your choice. E.g S to shop > ").upper()
    if choice == 'L':
        return 'L'
    elif choice == 'V':
        return 'V'
    elif choice == 'SU':
        return 'SU'
    elif choice == 'S':
        return 'S'
    else:
        print("Thank you, goodbye.")
        quit()


def TotalItems():  
    n = 0
    Basket = []
    Stock = ListOfGoods() 
    while n == 0:
        Item = input("What items would you like to buy: ")
        if Item in Stock:
            Basket.append(Item)
        else:
            print("Enter a item that is available")
            continue
        choice = input("Want to continue - click any key to continue or enter N if you are done shopping: ").upper()
        time.sleep(0.2) 
        if choice == 'N':
            n = 1
    return Basket


def PriceOfBasket(Basket):
    Price = 0
    Stock = ListOfGoods() 
    for i in Basket:
        if i in Stock:
            Price += Stock[i]  
    return Price


def postcode():
   postcode_raw = input("\nSo, what's your postcode of delivery? ")
   if postcode_raw == '':
       print("Please enter a postcode")
       postcode()
   postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{postcode_raw}").json()
   try:
       area = postcode_resp['result']['admin_ward']
   except KeyError:
       print("Please enter a valid postcode")
       postcode()
   else:
       print(f"This is your area then: {area}, nice!")
       return postcode_raw
   
def DeliveryPrice(postcode):
    dist = pgeocode.GeoDistance('gb')
    r = round(dist.query_postal_code('N17 0BX', postcode),2)
    DelPrice = round((r*3.0),2)
    return DelPrice


def VorM():
   Card = input("Would you like pay using Visa or Mastercard: ")
   if Card.casefold() == 'visa':
       Cardtype = 'Visa'
   elif Card.casefold() == 'mastercard':
       Cardtype = 'Mastercard'
   else:
       print("Please enter a valid cardtype")
       VorM()
   return Cardtype



def delivery_slot():
    user_slot = input("At what time would you like your grocery?: 11:00, 11:30, 12:00, 12:30, 13:00, 13:30 or 14:00: ")
    if user_slot== "11:00" or user_slot== "11:30" or user_slot== "12:00" or user_slot== "12:30" or user_slot== "13:00" or user_slot== "13:30" or user_slot== "14:00":
        print( f"Great, your grocery shall arrive by {user_slot}." )
    else:
        print("That slot is not valid.")
        delivery_slot()
    return user_slot

