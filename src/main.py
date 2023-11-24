from lottery import Lottery
from reward import *
from constants import MAX_TICKETS

lottery = Lottery()


def start_new_draw(lotto):
    lottery.start_new_draw()
    print(f"New Raffle draw has been started. Initial pot size: ${lotto.new_draw.pot_size}")
    press_any_key_to_continue()


def buy_tickets(lotto):
    name, number_of_tickets = name_tickets_input()
    issued_tickets = lotto.issue_tickets(name, number_of_tickets)

    print(f"Hi {name}, you have purchased {len(issued_tickets)} ticket(s)-")
    print_ticket_numbers(issued_tickets)
    print()

    press_any_key_to_continue()


def name_tickets_input():
    print("Enter your name, number of tickets to purchase")
    split_input = input("input (e.g. James, 1): ").split(',')

    name = split_input[0].strip()
    number_of_tickets = int(split_input[1].strip())
    number_of_tickets = min(number_of_tickets, MAX_TICKETS)     # Max tickets is MAX_TICKETS

    return name, number_of_tickets


def print_ticket_numbers(issued_tickets):
    for i, ticket in enumerate(issued_tickets, start=1):
        print(f"Ticket {i}: {ticket.numbers}")


def run_raffle(lotto):

    print("Getting winning ticket")
    lotto.run_draw()

    print(f"Winning Ticket is: {lotto.winning_numbers}")

    print("Group 2 Winners:")
    print_group_winners(lotto.pot_size, lotto.winners, 2)
    print()

    print("Group 3 Winners:")
    print_group_winners(lotto.pot_size, lotto.winners, 3)
    print()

    print("Group 4 Winners:")
    print_group_winners(lotto.pot_size, lotto.winners, 4)
    print()

    print("Group 5 Winners (Jackpot):")
    print_group_winners(lotto.pot_size, lotto.winners, 5)
    print()

    press_any_key_to_continue()


def print_group_winners(pot_size, winners, group):
    if len(winners[group]) == 0:
        print("Nil")
        return

    winner_dict = aggregate_tickets_by_name(winners[group])
    group_reward = calculate_group_reward(group, pot_size)
    for winner in winner_dict:
        share = calculate_winning_share(winner_dict[winner], winner_dict.total(), group_reward)
        print(f"{winner} with {winner_dict[winner]} winning ticket(s) - ${share:.2f}")


def press_any_key_to_continue():
    input("Press any key to return to main menu")


def main_menu(lotto):
    print("Welcome to My Raffle app")
    if lotto.new_draw:
        print(f"Status: Draw is ongoing. Raffle pot size is ${lotto.new_draw.pot_size}")
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


if __name__ == '__main__':
    while True:
        main_menu(lottery)
        c = get_response()
        if c == 1:
            start_new_draw(lottery)
        if c == 2:
            buy_tickets(lottery)
        if c == 3:
            run_raffle(lottery)
        print("")
