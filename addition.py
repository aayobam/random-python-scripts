# program that adds 2 integers
def main():
    try:
        response = input("Do you want to continue? type Y for yes or N for No: ").lower()

        if response == "yes" or response == "y":
            addition_of_integer()

        elif response == "no" or response == "n":
            print(f"\n{'*' * 20} Thanks for using this app, goodbye.. {'*' * 20}")
            exit()
        else:
            print("Invalid response, please try again.\n")
            main()

    except ValueError:
        print("An alphabet is required, please try again.")
        main()
    

def addition_of_integer():
    print(f"\n{'*' * 20} WELCOME TO INTERGER CALCULATOR {'*' * 20}")
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"Result = {num1 + num2}")
        main()

    except ValueError:
        print("A whole number is required\n")
        addition_of_integer()
addition_of_integer()
