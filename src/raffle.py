from ticket import Ticket

INITIAL_POT = 100
TICKET_VALUE = 5


class Raffle:
    def __init__(self, snowball=0):
        self.raffle_tickets = []
        self.__pot_size = INITIAL_POT + snowball

    def issue_raffle_ticket(self):
        ticket = Ticket.generate_ticket()
        self.raffle_tickets.append(ticket)
        return ticket

    def display_raffle_tickets(self):
        print("Raffle Tickets:")
        for index, ticket in enumerate(self.raffle_tickets, start=1):
            print(f"Ticket {index}: {ticket.numbers} - owner: {ticket.name}")

    @property
    def pot_size(self):
        # Calculate the total pot size based on the number of raffle tickets issued
        return self.__pot_size + len(self.raffle_tickets) * TICKET_VALUE  # Each ticket costs 10 units

