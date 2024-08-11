import sys
from database import DatabaseHelper


class SimpleLoginSystem:
    def __init__(self):
        self.db = DatabaseHelper()
        self.menu()
        self.db.close()

    def menu(self):
        print(f"{'_' * 15}Welcome to the Simple Login System{'_' * 15}")
        user_input = int(input("\na. Enter 1 to Register\nb. Enter 2 to Login\nc. Press any Button to Exit\n\n"))

        if user_input == 1:
            self.register()
        elif user_input == 2:
            self.login()
        else:
            sys.exit(1000)

    # To register user
    def register(self):
        name = input("\nEnter the name: ")
        email = input("Enter the email: ")
        password = input("Enter the password: ")

        response = self.db.register(name, email, password)

        if response:
            print("\nRegistration Successful\n")
        else:
            print("\nRegistration Failed\n")

        self.menu()

    # To login user
    def login(self):
        email = input("\nEnter the email: ")
        password = input("Enter the password: ")

        response = self.db.login(email, password)

        if len(response) != 0:
            print("\nLogged In Successfully\n")
            print("Hello,", response[0][1])
        else:
            print("\nInvalid email/password\n")
            sys.exit(1)

        Exit = False
        while not Exit:
            user_input = int(
                input("1. Enter 1 to view profile\n"
                      "2. Enter 2 to edit profile\n"
                      "3. Enter 3 to delete profile\n"
                      "4. Enter 4 to exit\n\n")
            )

            if user_input == 1:
                print(f"Name: {response[0][1]}\nEmail: {response[0][2]}\nPassword: {response[0][3]}\n")

            elif user_input == 2:
                user_input1 = input("\nEnter what you want to edit: ")
                user_input2 = input(f"Enter new {user_input1}: \n")
                self.db.edit_profile(user_input1, user_input2, response)

            elif user_input == 3:
                self.db.delete_profile(response[0][2], response[0][3])

            else:
                Exit = True
                # sys.exit(1)

        self.menu()


obj1 = SimpleLoginSystem()
