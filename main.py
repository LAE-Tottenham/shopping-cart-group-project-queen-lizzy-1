from UserInput import *
from Accounts import *
from currency_exchange_tool import *
from outputreceipt import receipt

n = None
Intro()
while True == True:
    r = options()
    if r == 'SU':
        m = createaccount()
        n = login()
        ItemPrinter()
        Basket = TotalItems()
        PriceOfB = PriceOfBasket(Basket)
        PoC = postcode()
        deltime = delivery_slot()
        DelPrice = DeliveryPrice(PoC)
        Cardtype = VorM()
        rate = getexch()
        Total = currency(PriceOfB + DelPrice,rate)
        receipt(Basket,currency(DelPrice,rate),Total,deltime,Cardtype,PoC,rate)
        savenewinfo(m[0],PoC,Cardtype,Basket)
    elif r == 'L':
        n = login()
    elif r == 'V':
        if n == None:
            print("You are not logged in. Login to view your account.")
            time.sleep(1.5)
        else:
            accountpage(n)
    elif r == 'S':
        if n == None:
            print("You haven't logged in. Sign up or Login to shop.")
            time.sleep(1.5)
        else:
            info = []
            f = open(f"{n}.txt","r")
            for x in f:
                x = x.replace('\n','')
                info.append(x)
            ItemPrinter()
            Basket = TotalItems()
            PriceOfB = PriceOfBasket(Basket)
            PoC = info[1]
            deltime = delivery_slot()
            DelPrice = DeliveryPrice(PoC)
            Cardtype = info[2]
            rate = getexch()
            Total = currency(PriceOfB + DelPrice,rate)
            receipt(Basket,currency(DelPrice,rate),Total,deltime,Cardtype,PoC,rate)
            saveinfo(n,Basket)