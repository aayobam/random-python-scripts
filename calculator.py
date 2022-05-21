# program that performs basic arithmentic operation


def end():
    try:
        response = input("Do you want to continue? type Y for yes or N for No: ").lower()

        if response == "yes" or response == "y":
            start()

        elif response == "no" or response == "n":
            print(f"\n{'*' * 20} Thanks for using this app, goodbye.. {'*' * 20}")
            exit()
        else:
            print("Invalid response, please try again.\n")
            end()
    except ValueError:
        end()


# performs addition
def addition():
    try:
        first_num = float(input("Enter first number: "))
        second_num = float(input("Enter second number: "))
        print(f"Result = {first_num + second_num}")
        end()
    except ValueError:
        print("A whole number is required\n")
        addition()

# performs subtraction
def subtraction():
    try:
        first_num = float(input("Enter first number: "))
        second_num = float(input("Enter second number: "))
        print(f"Result = {first_num - second_num}")
        end()
    except ValueError:
        print("A whole number is required\n")
        subtraction()

# performs division
def division():
    try:
        first_num = float(input("Enter first number: "))
        second_num = float(input("Enter second number: "))
        print(f"Result = {first_num / second_num}")
        end()
    except ValueError:
        print("A whole number is required\n")
        division()

# performs multiplication
def multiplication():
    try:
        first_num = float(input("Enter first number: "))
        second_num = float(input("Enter second number: "))
        print(f"Result = {first_num * second_num}")
        end()
    except ValueError:
        print("A whole number is required\n")
        multiplication()


# performs modulus
def modulus():
    try:
        first_num = float(input("Enter first number: "))
        second_num = float(input("Enter second number: "))
        print(f"Result = {first_num % second_num}")
        end()
    except ValueError:
        print("A whole number is required\n")
        modulus()


def option_selector():
    print("1 - ADDTION\n2 - SUBTRACTION\n3 - DIVISION\n4 - MULTIPLICATION\n5 - MODULO\n6 - EXIT\n")


def start():
    try:
        print(f"{'*' * 20} WELCOME TO SIMPLE CONSOLE CALCULATOR APP {'*' * 20}\n")
        option_selector()
        response = int(input("What operation will you like to perform?: ").upper())
        if response == 1:
            print("\nYou have chosen ADDITION\n")
            addition()

        elif response == 2:
            print("\nYou have chosen SUBTRACTION\n")
            subtraction()

        elif response == 3:
            print("\nYou have chosen DIVISION\n")
            division()

        elif response == 4:
            print("\nYou have chosen MULTIPLICATION\n")
            multiplication()

        elif response == 5:
            print("\nYou have chosen MODULUS\n")
            modulus()

        elif response == 6:
            print(f"\n{'*' * 20} Thanks for using this app, goodbye.. {'*' * 20}")
            exit()
    except ValueError:
        print("Invalid input please try again\n")
        start()
start()