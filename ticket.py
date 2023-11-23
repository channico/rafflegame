import random


def generate_numbers():
    # Generate a list of 5 unique random numbers between 1 and 15
    return random.sample(range(1, 16), 5)


class Ticket:
    def __init__(self, numbers):
        self.numbers = numbers

    @classmethod
    def generate_ticket(cls):
        # Generate a list of 5 unique random numbers between 1 and 15
        numbers = generate_numbers()
        return cls(numbers)

    def display_ticket(self):
        print("Lottery Ticket Numbers:", self.numbers)

    def check_numbers(self, other_ticket):
        # Check if the numbers on two lottery tickets are equal
        return self.numbers == other_ticket.numbers