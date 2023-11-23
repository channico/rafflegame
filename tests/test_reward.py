from unittest import TestCase
from ticket import Ticket
from reward import aggregate_tickets_by_name


class TestReward(TestCase):
    def setUp(self) -> None:
        self.tickets = [
            Ticket([1, 2, 3, 4, 5], "Adam"),
            Ticket([1, 2, 3, 4, 6], "Benny"),
            Ticket([1, 2, 3, 6, 7], "Carter"),
            Ticket([1, 2, 6, 7, 8], "Dennis"),
            Ticket([1, 3, 6, 7, 8], "Edmund"),
            Ticket([1, 3, 6, 7, 9], "Edmund")
        ]

    def test_aggregate_tickets_by_name(self):
        winner_list = aggregate_tickets_by_name(self.tickets)
        self.assertEqual(2, winner_list['Edmund'])
        self.assertEqual(1, winner_list['Adam'])
        self.assertEqual(1, winner_list['Benny'])
        self.assertEqual(1, winner_list['Carter'])
        self.assertEqual(1, winner_list['Dennis'])
