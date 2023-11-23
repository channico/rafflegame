from constants import INITIAL_POT, TICKET_VALUE
from ticket import Ticket


class Raffle:
    def __init__(self, snowball=0):
        self.raffle_tickets = []
        self.__pot_size = INITIAL_POT + snowball

    def issue_raffle_ticket(self, name="Anonymous"):
        ticket = Ticket.generate_ticket(name)
        self.log_raffle_ticket(ticket)
        return ticket

    def log_raffle_ticket(self, ticket):
        self.raffle_tickets.append(ticket)

    def display_raffle_tickets(self):
        print("Raffle Tickets:")
        for index, ticket in enumerate(self.raffle_tickets, start=1):
            print(f"Ticket {index}: {ticket.numbers} - owner: {ticket.name}")

    def find_winners(self, winning_numbers):
        winners = {2: [], 3: [], 4: [], 5: []}

        for ticket in self.raffle_tickets:
            group = ticket.check_group_winner(winning_numbers)
            if group == 5:
                winners[5].append(ticket)

            if group == 4:
                winners[4].append(ticket)

            if group == 3:
                winners[3].append(ticket)

            if group == 2:
                winners[2].append(ticket)

        return winners

    @property
    def pot_size(self):
        # Calculate the total pot size based on the number of raffle tickets issued
        return self.__pot_size + len(self.raffle_tickets) * TICKET_VALUE  # Each ticket costs 10 units

