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
        adam = Ticket([1, 2, 3, 4, 5], "Adam")
        self.raffle.log_raffle_ticket(adam)

        benny = Ticket([1, 2, 3, 4, 6], "Benny")
        self.raffle.log_raffle_ticket(benny)

        carter = Ticket([1, 2, 3, 6, 7], "Carter")
        self.raffle.log_raffle_ticket(carter)

        dennis = Ticket([1, 2, 6, 7, 8], "Dennis")
        self.raffle.log_raffle_ticket(dennis)

        edmund = Ticket([1, 3, 6, 7, 8], "Edmund")
        self.raffle.log_raffle_ticket(edmund)

        winners = self.raffle.find_winners([1, 2, 3, 4, 5])

        self.assertEqual(2, len(winners[2]))
        self.assertTrue(dennis in winners[2])
        self.assertTrue(edmund in winners[2])

        self.assertEqual(1, len(winners[3]))
        self.assertTrue(carter in winners[3])

        self.assertEqual(1, len(winners[4]))
        self.assertTrue(benny in winners[4])

        self.assertEqual(1, len(winners[5]))
        self.assertTrue(adam in winners[5])
