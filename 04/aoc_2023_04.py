import math

def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]


def partone(lines):
    s = 0
    for line in lines:
        no, number_str = line.split(": ")
        winning_str, my_str = number_str.split("|")
        winning_numbers = set(winning_str.split())
        my_numbers = set(my_str.split())
        no_matches = len(my_numbers.intersection(winning_numbers))
        s += 2**(no_matches - 1) if no_matches > 0 else 0                         
    return s

def parttwo(lines):
    s = 0
    no_cards = [1]*len(lines)
    for k, line in enumerate(lines):
        no, number_str = line.split(": ")
        winning_str, my_str = number_str.split("|")
        winning_numbers = set(winning_str.split())
        my_numbers = set(my_str.split())
        no_matches = len(my_numbers.intersection(winning_numbers))
        for m in range(no_matches):
            if k + m + 1 < len(no_cards):
                no_cards[k + m + 1] += no_cards[k]
    return sum(no_cards)

print(partone(read_input("input.txt")))
print(parttwo(read_input("input.txt")))

