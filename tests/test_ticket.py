from unittest import TestCase

from ticket import Ticket


class TestTicket(TestCase):
    def test_generate_ticket(self):
        ticket = Ticket.generate_ticket()
        ticket.display_ticket()
