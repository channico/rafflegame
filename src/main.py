# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# TODO: Refactor this into a separate class
pot_size = 100
draw_started = False


def start_new_draw():
    global pot_size, draw_started
    pot_size = 100
    draw_started = True
    print(f"New Raffle draw has been started. Initial pot size: ${pot_size}")
    press_any_key_to_continue()


def buy_tickets():
    print("Enter your name, number of tickets to purchase (for e.g. a valid input will be **James,1** )")
    print()
    press_any_key_to_continue()


def run_raffle():
    print("STUB: Getting winning ticket")
    print("STUB: Getting winners")
    print("STUB: Display Winners")
    print()
    press_any_key_to_continue()


def press_any_key_to_continue():
    input("Press any key to return to main menu")


def main_menu():
    print("Welcome to My Raffle app")
    if draw_started:
        print(f"Status: Draw has is ongoing. Raffle pot size is ${pot_size}")
    else:
        print("Status: Draw has not started")
    print()
    print("[1] Start a New Draw")
    print("[2] Buy Tickets")
    print("[3] Run Raffle")
    print("")


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
    while True:
        main_menu()
        c = get_response()
        if c == 1:
            start_new_draw()
        if c == 2:
            buy_tickets()
        if c == 3:
            run_raffle()
        print("")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
