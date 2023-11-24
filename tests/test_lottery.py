from unittest import TestCase

from lottery import Lottery
from constants import *


class TestLottery(TestCase):
    def setUp(self) -> None:
        self.lotto = Lottery()
        self.lotto.start_new_draw()

    def test_issue_tickets(self):
        self.assertEqual(INITIAL_POT, self.lotto.new_draw.pot_size)

        self.lotto.issue_tickets("Adam", 1)
        self.assertEqual(INITIAL_POT + (1 * TICKET_VALUE), self.lotto.new_draw.pot_size)

        self.lotto.issue_tickets("Barbie", 2)
        self.assertEqual(INITIAL_POT + (3 * TICKET_VALUE), self.lotto.new_draw.pot_size)

        self.lotto.issue_tickets("Charlie", 3)
        self.assertEqual(INITIAL_POT + (6 * TICKET_VALUE), self.lotto.new_draw.pot_size)

