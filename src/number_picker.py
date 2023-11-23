import random

from constants import LOTTO_NUMBER_RANGE_MAX, RANDOM_NUMBERS_PER_TICKET


def generate_numbers():
    # Generate a list of 5 unique random numbers between 1 and 15
    return random.sample(range(1, LOTTO_NUMBER_RANGE_MAX + 1), RANDOM_NUMBERS_PER_TICKET)
