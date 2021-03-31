#to-do list
#by ryan langstone
#finished on 2/3/2021 for school
import time #so that i can do delays
import secure
import ast
#declaring all global variables
accounts = []
user = ""
#defining functions
def update_file(sring):
    my_file = open("account_info.txt", "w")
    x = secure.encript(str(sring))
    my_file.write(x)
    my_file.close()


def number_input(phrase, option):
    #pass a input statment in and the option you want it to be and it will return the valid input
    digit = None
    while digit == None:
        try: 
            digit = int(input(phrase))
            
        except:
            if option == []:
                print ("has to be a hole number")
        if digit not in option and option !=[]:
                digit = None
                print ("has to be of one of the options provided")
    return  digit

    
def validate_pasword(pasword):
    #makes sure the pasword is valid, and tells you what is wrong
    acsept = True
    if len(pasword) < 8:
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
    #gives the posible options at the start of the code, and gets you to chose one
    otions = [1,2,3]
    print("chose a mode by entering a number:")
    print("1: add an account")
    if len(accounts) >0:
        print("2: log in")
    print("3: exit")
    return  number_input("", otions)


def add_acount():
    # adds an acount to the acount variable 
    global user
    back = False
    age = number_input("enter your age", [])
    if age >= 13:
        in_loop = True
        while in_loop == True:
            username = input("enter a username or type 0 to exit")
            if username == "0":
                back = True
                in_loop = False
            else:
                if username not in accounts:
                    in_loop = False
                else:
                    print("username already in use")
        if back == False:
            in_loop = False
            while in_loop == False:     
                pasword = str(input("ener a pasword or type 0 to exit"))
                if pasword == "0":
                    back = True
                    in_loop = True
                    
                    break
                else:
                    in_loop = validate_pasword(pasword)
            print(back)
            if back == False:
                dictonary = {"username":username, "pasword":pasword, "data":[]}
                accounts.append(dictonary)
                update_file(accounts)
                user = len(accounts)-1
                return True
        if back == True:
            return False
    else:
        print("you are to young")
        return False


def log_in():
    #logs in if username and pasword match, else asks you to try again
    global user
    used = False
    back = False
    while used == False:
        username = str(input("enter your username or 0 to exit"))
        print("username")
        if username == "0":
            back = True
            used = True
        else:
            user_number = -1
            for i in accounts:
                user_number = user_number +1
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
                user = user_number
                print(user)
                break
            else:
                print("that is the incorect pasword")


def menu():
    #prints all options once you have loged in and gets you to chose one
    options = [1,2,3,4]
    print("press 1 to add a task")
    print("press 2 to view tasks")
    print("press 3 to log out")
    print("press 4 to exit program")
    return  number_input("", options)


def add_pasword():
    #adds a "pasword" to the list that the user has
    back = False
    while back == False:
        aplication = input("\nEnter the aplication the pasword account is for, your username and then pasword \nall separated by commas\nor 0 to exit\n").split(",")
        if len(aplication) == 1 and aplication[0] == "0":
            back = True
        elif len(aplication) == 3:
            dictonary = {"use":aplication[0],"username":aplication[1],"pasword":aplication[2]}
            accounts[user]["data"].append(dictonary) 
            update_file(accounts)   
        else:
            print("you need to imput 3 things separated by comas\ne.g. w3schools,my_username,pass2020\nor type 0 to exit")


def print_paswords():
    #prints all the paswords that the usr has
    
    for i in accounts[user]["data"]:
        print("aplication: "+i["use"]+", username: "+i["username"]+", pasword: "+i["pasword"])
    in_loop = True
    while in_loop == True:
        word = input("search for aplication, or type 0 to go back")
        print(word)
        if word == "0":
            break
        else:
            for i in accounts[user]["data"]:
                if i["use"] == word:
                    print("aplication: "+i["use"]+", username: "+i["username"]+", pasword: "+i["pasword"])
#print(secure.encript())

def loged_in():
    #main code for when you have loged in, directs to the aproptiate function
    global value
    global user
    print("loged in as "+accounts[user]["username"])
    number = 0
    while number != 4:
        number = menu()
        if number == 1:
            add_pasword()
        elif number == 2:
            print_paswords()
        elif number == 3:
            user = None
            print("you are now loged out")
            number == 4
            break
        else:
            print("hope you use this tool again some time")
            time.sleep(1)
            print("see ya")
            value = 3


#extra global variables that are used for the while loop bellow 
try:
    my_file = open("account_info.txt", "r")
    info = my_file.read()
    if len(my_file.read()) < 1:
        accounts = secure.unencript(info)
        accounts = ast.literal_eval(accounts)
except:
    pass
value = 0
user = None
#main code, directing you to the apropriate function based on what you chose
while value != 3:
    acount_valdiity = True
    value = login_menu()
    if value == 1:
        acount_valdiity = add_acount()
        if acount_valdiity == True:
            loged_in()
    elif value == 2:
        if len(accounts) >0:
            log_in()
            if user != None:
                loged_in()
    else:
        print("hope you use this tool again some time")
        time.sleep(1)
        print("see ya")