from UserInput import *
from currency_exchange_tool import *
def receipt(Bat,DelPri,Tot,Delslot,Card,PC,Type):
    Items = ListOfGoods()
 
    company_name = "Queen Lizzy's Online Shop"

    f = Figlet(font="slant")
    x = f.renderText("Queen Lizzy's Online Shop")
    y = colored(x, "blue" , attrs=['bold'])
    print(y)
    print("-------------------------------------------------------\n")
    time.sleep(1.5) 


    print("*"*55) 
    print("\t Product \t Product Price")
    for i,x in enumerate(Bat):
        print(f"\t{x} \t         {currency(Items[x],Type)}")
    print("*"*55) 

    print("\t\t\t Delivery Price" )
    print(f"\t\t\t {DelPri}")

    print("="*55) 
    print(f"\t\t\t Total" )
    print(f"\t\t\t {Tot}" )

    print("*"*55)  
    print("\t\t\t Delivery Slot:")
    print(f"\t\t\t {Delslot}")
    print("\t\t\t Payment Method:")
    print(f"\t\t\t {Card}")
    print("\t\t\t Address:")
    print(f"\t\t\t {PC}")

    Message = "Thank you for shopping with us. Have a good day!"
    print("\n\t{}\n".format(Message))

    print("-------------------------------------------------------\n")

