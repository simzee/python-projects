master_pwd = input("Enter the master password: ")


def view():
    with open("password.txt", "r") as f:
        for lines in f.readlines():
            data = lines.rstrip()
            user, password = data.split("|")
            print(f"User:{user} , Password:{password}")


def add():
    name = input("Account Name: ")
    password = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(f"{name} | {password}\n")


while True:
    mode = input("Would you like to view the passwords or add a new one? Type 1-View , 2-Add , 3-Quit:\n")

    if mode == '1':
        view()

    elif mode == '2':
        add()

    elif mode == '3':
        quit()

    else:
        print("Invalid Mode. Try again.")
        continue

