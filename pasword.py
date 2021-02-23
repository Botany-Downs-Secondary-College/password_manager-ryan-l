#to-do list
#by ryan langstone
import time
pasword = []
accounts = []
user = ""
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
    global user
    back = False
    age = number_input("enter your age", "")
    if age >= 13:
        in_loop = True
        while in_loop == True:
            username = input("ener a username or type 0 to exit")
            if username == 0:
                back = True
            else:
                if username not in accounts:
                    in_loop = False
                else:
                    print("username already in use")
        if back == False:
            in_loop = False
            while in_loop == False:     
                pasword = str(input("ener a pasword or type 0 to exit"))
                print(pasword)
                if pasword == "0":
                    back == True
                    in_loop == True
                    
                    break
                else:
                    in_loop = validate_pasword(pasword)
            if back == False:
                dictonary = {"username":username, "pasword":pasword}
                accounts.append(dictonary)
                user = accounts[len(accounts)-1]
                print(user)
                return True
        if back == True:
            return False
    else:
        print("you are to young")
        return False

def log_in():
    global user
    used = False
    back = False
    while used == False:
        username = str(input("ener your username or 0 to exit"))
        print("username")
        if username == "0":
            back = True
            used = True
        else:
            for i in accounts:
                if i["username"] == username:
                    login_user = i
                    used = True
                    break
            if used == False:
                print("that username does not exist")
    if back == False:     
        for i in range(3):
            pasword = str(input("ener your pasword or 0 to exit"))
            if pasword == "0":
                break
            if login_user["pasword"] == pasword:
                user = login_user
                print(user)
                break
            else:
                print("that is the incorect pasword")

def loged_in():
    print("loged in as "+user["username"])
    

value = 0
user = None
while value != 3:
    acount_valdiity = True
    value = login_menu()
    if value == 1:
        acount_valdiity = add_acount()
        if acount_valdiity == True:
            loged_in()
    elif value == 2:
        log_in()
        if user != None:
            loged_in()
    else:
        print("hope you use this tool again some time")
        time.sleep(1)
        print("see ya")