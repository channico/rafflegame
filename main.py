# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def main_menu():
    print("Welcome to My Raffle app")
    print("Status: Draw has not started")
    print()
    print("[1] Start a New Draw")
    print("[2] Buy Tickets")
    print("[3] Run Raffle")
    print()


def get_response():
    while True:
        try:
            # Read input from the user
            choice = int(input("Enter your choice (1-3): "))

            # Check if the choice is between 1 and 3
            if 1 <= choice <= 3:
                break  # Break out of the loop if the choice is valid
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Continue with the rest of your code using the validated choice
    return choice


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_menu()
    c = get_response()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
