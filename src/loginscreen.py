#intro
"""
    main login screen and user selection
"""

print("User profiles")


def check():
    # You need to read it only once, not every loop
    users = open("users.txt").read().split("\n")
    for i in range(len(users)):
        users[i] = users[i].split("|")

    # Now what you want is to loop infinitely
    # until you get correct username/password
    # instead of recursive calling this
    # function over and over again
    while True:
        username = str(input("Username: "))
        password = str(input("Password: "))

        for user in users:
            uname = user[4]
            pword = user[5]

            if uname == username and pword == password:
                print("Hello " + user[1] + ".")
                print("You are logged in as: " + user[2] + ".")
                main_menu()

        # If none of the records matched the input
        print("Wrong username/password.")
        print("Try again!\n\n")


check()
