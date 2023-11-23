from ticket import Ticket
from collections import Counter


def calculate_group_reward(group, pot_size):
    if group == 2:
        return pot_size * 0.10
    if group == 3:
        return pot_size * 0.15
    if group == 4:
        return pot_size * 0.25
    if group == 5:
        return pot_size * 0.50

    return 0


def calculate_winning_share(tickets, total_tickets, reward):
    return (tickets / total_tickets) * reward


def aggregate_tickets_by_name(tickets: list[Ticket]):
    winner_list = Counter()
    for ticket in tickets:
        winner_list[ticket.name] += 1

    return winner_list
