from unittest import TestCase

from raffle import Raffle


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

