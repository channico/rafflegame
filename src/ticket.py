from number_picker import generate_numbers


class Ticket:
    def __init__(self, numbers, name="Anonymous"):
        self.numbers = sorted(numbers)
        self.name = name

    @classmethod
    def generate_ticket(cls, name="Anonymous"):
        # Generate a list of 5 unique random numbers between 1 and 15
        numbers = generate_numbers()
        return cls(numbers, name)

    def display_ticket(self):
        print("Lottery Ticket Numbers:", self.numbers)

    def check_numbers(self, other_ticket):
        # Check if the numbers on two lottery tickets are equal
        return self.numbers == other_ticket.numbers
