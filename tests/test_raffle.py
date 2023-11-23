from unittest import TestCase

from raffle import Raffle
from ticket import Ticket


class TestRaffle(TestCase):
    def setUp(self):
        self.raffle = Raffle()

    def test_init(self):
        self.assertEqual(100, self.raffle.pot_size)
        self.assertFalse(self.raffle.raffle_tickets)

    def test_issue_raffle_ticket(self):
        self.raffle.issue_raffle_ticket()
        self.assertEqual(1, len(self.raffle.raffle_tickets))
        self.assertEqual(105, self.raffle.pot_size)

    def test_display_raffle_tickets(self):
        self.raffle.issue_raffle_ticket()
        self.raffle.issue_raffle_ticket()
        self.raffle.display_raffle_tickets()

    def test_find_winners(self):
        self.raffle.log_raffle_ticket(Ticket([1, 2, 3, 4, 5], "Adam"))
        self.raffle.log_raffle_ticket(Ticket([1, 2, 3, 4, 6], "Benny"))
        self.raffle.log_raffle_ticket(Ticket([1, 2, 3, 6, 7], "Carter"))
        self.raffle.log_raffle_ticket(Ticket([1, 2, 6, 7, 8], "Dennis"))
        self.raffle.log_raffle_ticket(Ticket([1, 3, 6, 7, 8], "Edmund"))

        winners = self.raffle.find_winners([1, 2, 3, 4, 5])
        print(winners[2])
        print(winners[3])
        print(winners[4])
        print(winners[5])
