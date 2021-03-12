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
    while True:
        print("Hello", name)
        if age < 13:
            rint("{},you are {}. You are therefore an underage loli. You do not qualify for an account scrub".format(name, age))
        elif age > 130:
            print("No one\'s ever reached 130 years of age. Those Bible stories of people reaching 900+ years of age "
                  "are "
              "all false. Go die.")
        else:
            while True:
                member = input("Please enter | L for log in or | N for new account: ").upper()
                tries = 0
                success = False

                if member == 'L':
                    while tries < 3:
                        m_username = input("Enter username: ")
                        m_password = input("Enter password: ")
                        if m_username and m_password in member_list:
                            print("Successfully logged in. Welcome back.")
                            success = True
                            break
                        else:
                            print("Error. Something doesn't match up. Maybe it's your brain.")
                            tries += 1
                    if not success:
                        print("Hacker. Nobody likes you. GO mess with someone else's account and stop changing "
                              "passwords to bomb123")


                elif member == 'N':
                    m_username = input("Enter username: ")
                    m_password = input("Enter password at least 8 character's long: ")
                    if any (passreqs.isupper for passreqs in m_password) and any (passreqs.isdigit() for passreqs in m_password and len(m_password) > 8):
                        member_list.append(m_username, m_password)
                        print("Your new account has been created")
                        print(member_list)
                    else:
                        print("Your password fails to meet our requirements. Do you want all your data stolen? Yes? "
                              "Then go use our competitor Ching Chong Ching Chong, not us.")
                else:
                    print("Invalid option. Go use L or N dumbdumb.")




    # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
print('Welcome to Big Chongus password manager.')
print('If you are 13 years or older, you are able to store your passwords here.')

name = input("What is your name?: ")
while True:
    try:

        age = float(input("How old are you?: "))
        chosen_option = menu(name, age)
        break

    except:
        print("Enter an integer idiot. No random letters and symbols blind man. This will loop till you follow my "
              "instructions")




