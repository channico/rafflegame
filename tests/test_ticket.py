from unittest import TestCase

from ticket import Ticket


class TestTicket(TestCase):
    def test_generate_ticket(self):
        ticket = Ticket.generate_ticket()
        self.assertEqual(type(ticket), Ticket)

    def test_equality(self):
        ticket1 = Ticket([1, 2, 3, 4, 5])
        ticket2 = Ticket([1, 2, 3, 4, 5])
        ticket3 = Ticket([1, 1, 1, 1, 1])
        self.assertEqual(ticket1.numbers, ticket2.numbers)
        self.assertNotEqual(ticket1.numbers, ticket3.numbers)

    def test_different_order_creation(self):
        ticket1 = Ticket([1, 2, 3, 4, 5])
        ticket2 = Ticket([5, 4, 3, 2, 1])
        self.assertEqual(ticket1.numbers, ticket2.numbers)

    def test_check_numbers(self):
        ticket1 = Ticket([1, 2, 3, 4, 5])
        ticket2 = Ticket([5, 4, 3, 2, 1])
        self.assertTrue(ticket1.check_numbers(ticket2))

    def test_check_group5_winner(self):
        ticket1 = Ticket([1, 2, 3, 4, 5])
        self.assertEqual(5, ticket1.check_group_winner([1, 2, 3, 4, 5]))

    def test_check_group4_winner(self):
        ticket1 = Ticket([1, 2, 3, 4, 5])
        self.assertEqual(4, ticket1.check_group_winner([1, 2, 3, 4, 6]))

    def test_check_group3_winner(self):
        ticket1 = Ticket([1, 2, 3, 4, 5])
        self.assertEqual(3, ticket1.check_group_winner([1, 2, 3, 6, 7]))

    def test_check_group2_winner(self):
        ticket1 = Ticket([1, 2, 3, 4, 5])
        self.assertEqual(2, ticket1.check_group_winner([1, 2, 6, 7, 8]))

