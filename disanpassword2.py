# password_manager.py
# create and display passwords for users
# D.Tennakoon, Feb 21


# initialize variable and lists
name = ""
age = ""
# An empty list to store usernames and passwords for web/apps
password_list = []
# A list with existing member's details and store new member's details
member_list = ["Ravi", "Jong Ul"]


# Press the green button in the gutter to run the script.
def menu(name, age):
    # Use a breakpoint in the code line below to debug your script.
    print("Hello", name)
    if age < 13:
        print("{},you are {}. You are therefore an underage loli. You do not qualify for an account scrub".format(name, age))
    elif age > 130:
        print("No one\'s ever reached 130 years of age. Those Bible stories of people reaching 900+ years of age are "
              "all false. Go die.")
    else:
        mode = input(""""Choose a mode by entering the number:
        1: Add passwords 2: View Passwords: 3: Exit :""").strip()
        return mode
    # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
print('Welcome to Big Chongus password manager.')
print('If you are 13 years or older, you are able to store your passwords here.')

name = input("What is your name?: ")
age = float(input("How old are you?: "))


while True:
    chosen_option = menu(name, age)

# noinspection PyUnreachableCode
    if chosen_option == '1':
        print("Loading successful")
        add.details()

    elif chosen_option == '2':
        print("Loading successful")
        view.list()

    elif chosen_option == '3':
        print("See you again soon")
        break

    else:
        print("Get out of here!!!")
        break

