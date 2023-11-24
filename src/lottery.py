from number_picker import generate_numbers
from raffle import Raffle
from reward import calculate_group_reward
from ticket import Ticket


class Lottery:
    def __init__(self):
        self.new_draw = None
        self.snowball = 0
        self.winners = None
        self.winning_numbers = None
        self.pot_size = 0

    def start_new_draw(self):
        self.new_draw = Raffle(self.snowball)
        self.snowball = 0

    def issue_tickets(self, name) -> list[Ticket]:
        pass

    def run_draw(self):
        self.winning_numbers = generate_numbers()

        # Save the pot size
        self.pot_size = self.new_draw.pot_size
        self.winners = self.new_draw.find_winners(self.winning_numbers)
        self.snowball = self.calculate_snowball()

        # Reset the raffle
        self.new_draw = None

    def calculate_snowball(self):
        snowball = 0
        for group in range(2, 6):
            group_reward = calculate_group_reward(group, self.pot_size)
            if len(self.winners[group]) == 0:
                snowball += group_reward

        return snowball
