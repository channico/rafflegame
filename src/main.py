# This is a sample Python script.
from constants import MAX_TICKETS
from number_picker import generate_numbers
from raffle import Raffle

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

raffle: Raffle = None
snowball = 0


def start_new_draw():
    global raffle, snowball
    raffle = Raffle(snowball)
    print(f"New Raffle draw has been started. Initial pot size: ${raffle.pot_size}")
    press_any_key_to_continue()


def buy_tickets():
    global raffle

    print("Enter your name, number of tickets to purchase")
    split_input = input("input (e.g. James, 1): ").split(',')
    name = split_input[0].strip()
    number_of_tickets = int(split_input[1].strip())

    # Max tickets is 5
    number_of_tickets = min(number_of_tickets, MAX_TICKETS)

    issued_tickets = []
    for i in range(number_of_tickets):
        issued_tickets.append(raffle.issue_raffle_ticket(name))

    print(f"Hi {name}, you have purchased {len(issued_tickets)} ticket(s)-")
    print_ticket_numbers(issued_tickets)

    print()
    press_any_key_to_continue()


def print_ticket_numbers(issued_tickets):
    for i, ticket in enumerate(issued_tickets, start=1):
        print(f"Ticket {i}: {ticket.numbers}")


def run_raffle():
    print("Getting winning ticket")
    winning_numbers = generate_numbers()

    print(f"Winning Ticket is: {winning_numbers}")
    raffle.find_winners(winning_numbers)

    print("Group 2 Winners:")
    print()

    print("Group 3 Winners:")
    print()

    print("Group 4 Winners:")
    print()

    print("Group 5 Winners (Jackpot):")
    print()


    print()
    press_any_key_to_continue()


def press_any_key_to_continue():
    input("Press any key to return to main menu")


def main_menu():
    print("Welcome to My Raffle app")
    if raffle:
        print(f"Status: Draw is ongoing. Raffle pot size is ${raffle.pot_size}")
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
