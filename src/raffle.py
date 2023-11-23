from ticket import Ticket

INITIAL_POT = 100
TICKET_VALUE = 5


class Raffle:
    def __init__(self):
        self.raffle_tickets = []

    def issue_raffle_ticket(self):
        ticket = Ticket.generate_ticket()
        self.raffle_tickets.append(ticket)
        return ticket

    def display_raffle_tickets(self):
        print("Raffle Tickets:")
        for index, ticket in enumerate(self.raffle_tickets, start=1):
            print(f"Ticket {index}: {ticket.numbers}")

    @property
    def pot_size(self):
        # Calculate the total pot size based on the number of raffle tickets issued
        return INITIAL_POT + len(self.raffle_tickets) * TICKET_VALUE  # Each ticket costs 10 units

