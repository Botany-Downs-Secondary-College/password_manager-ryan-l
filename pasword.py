#to-do list
#by ryan langstone
import time
pasword = []
accounts = []
def number_input(phrase, option):
    digit = ""
    while digit == "":
        try: 
            digit = int(input(phrase))
            
        except:
            if option == "":
                print ("has to be a number")
            else:
                print ("has to be of one of the options provided")
    return  digit
def validate_pasword(pasword):
    acsept = True
    if len(pasword) <= 8:
        print("pasword to short")
        acsept = False
    if not any(char.isdigit() for char in pasword):
        print("pasword doesn't contain a number")
        acsept = False
    if not any(char.isalpha() for char in pasword):
        print("pasword doesn't contain a charicter")
        acsept = False
    if not any(not char.isalpha() and not char.isdigit() for char in pasword):
        print("pasword doesn't contain a special charicter")
        acsept = False
    return acsept

def login_menu():
    otions = [1,2,3]
    print("chose a mode by entering a number:")
    print("1: add a acount")
    print("2: log in")
    print("3: exit")
    return  number_input("", otions)

def add_acount():
    age = number_input("enter your age", "")
    if age >= 13:
        in_loop = True
        while in_loop == True:
            username = input("ener a username")
            if username not in accounts:
                in_loop = False
            else:
                print("username already in use")
        in_loop = False
        while in_loop == False:     
            pasword = input("ener a pasword")
            in_loop = validate_pasword(pasword)
        dictonary = {"username":username, "pasword":pasword}
        accounts.append(dictonary)
        return True
    else:
        print("you are to young")
        return False

def log_in():
    used = False
    while used == False:
        username = input("ener your username")
        for i in accounts:
            if i["username"] == username:
                user = i
                used = True
                break
        if used == False:
            print("that username does not exist")
    used = False     
    while used == False:
        pasword = input("ener your pasword")
        if user["pasword"] == pasword:
            used = True
        else:
            print("that is the incorect pasword")

value = 0
while value != 3:
    acount_valdiity = True
    value = login_menu()
    if value == 1:
        acount_valdiity = add_acount()
    elif value == 2:
        log_in()
    else:
        print("hope you use this tool again some time")
        time.sleep(1)
        print("see ya")