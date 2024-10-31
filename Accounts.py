from pyfiglet import Figlet
from termcolor import colored
import time
def createaccount():
    f = Figlet(font="slant")
    x = f.renderText("SIGN UP!")
    y = colored(x, "blue" , attrs=['bold'])
    print(y)
    username = input("Enter your new username. > ")
    if username in accounts():
        print("This account already exisits.")
    password = input("Enter your new password. > ")
    compassword = input("Confirm your password. > ")
    while compassword != password:
        print("Your passwords are not the same.")
        compassword = input("Confirm your password. > ")
    f = open("Accounts.txt","a")
    x = open(f"{username}.txt",'x')
    f.write(f"{username}\n{password}\n")
    f.close()
    return [username,password]

def accounts():
    accounts = []
    f = open("Accounts.txt","r")
    for x in f:
        x = x.replace('\n','')
        accounts.append(x)
    return accounts

def login():
    f = Figlet(font="slant")
    x = f.renderText("LOG IN!")
    y = colored(x, "blue" , attrs=['bold'])
    print(y)
    user = input("Enter your Username. > ")
    A = accounts()
    if user not in A:
        print("Username not found.")
        quit()
    password = input("Enter your password. > ")
    while password != A[A.index(user)+1]:
        if password == '':
            quit()
        print("Incorrect Password - Try Again.")
        password = input("Or click the enter key if you have forgotten your password. > ")
    print("You have successfully logged in!")
    return user

def accountpage(username):
    f = Figlet(font="slant")
    x = f.renderText("ACCOUNT PAGE!")
    y = colored(x, "blue" , attrs=['bold'])
    print(y)
    info = []
    f = open(f"{username}.txt","r")
    for x in f:
        x = x.replace('\n','')
        info.append(x)
    print("*"*50)
    print("Your details")
    time.sleep(1.5)
    print(f"Your Postcode: {info[1]}")
    print(f"Card Method: {info[2]}")
    print("*"*50)
    print("Your Orders:")
    for x in info[3:]:
        print(f"~~> {x} ")
    time.sleep(1.5)

def savenewinfo(username,postcode,cardtype,Basket):
    f = open(f"{username}.txt","a")
    f.write(f"{username}\n{postcode}\n{cardtype}\n")
    for x in Basket:
        f.write(f"{x}\n")
    f.write("-"*50 + '\n')

def saveinfo(username,Basket):
    f = open(f"{username}.txt","a")
    for x in Basket:
        f.write(f"{x}\n")
    f.write("-"*50 + '\n')
