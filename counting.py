def end():
    try:
        response = input("Do you want to continue? type Y for yes or N for No: ").lower()

        if response == "yes" or response == "y":
            count_words()

        elif response == "no" or response == "n":
            print(f"\n{'*' * 20} Thanks for using this app, goodbye.. {'*' * 20}")
            exit()
        else:
            print("Invalid response, please try again.\n")
            end()
    except ValueError:
        end()


# start of program checks for total words input.
def count_words():
    print(f"{'*' * 20} WELCOME TO SIMPLE CONSOLE WORDS COUNTING APP {'*' * 20}\n")
    string = input("Enter words to be counted: ")
    print("Total Words:", len(string.split()))
    end()
count_words()