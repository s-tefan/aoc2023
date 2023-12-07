# AoC 2023, day 7
# S-tefan

def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]


class Hand:
    ALL_CARDS = "23456789TJQKA"

    def __init__(self, cards):
        self.cards = cards

    def strength(self):
        c = {}
        for card in self.cards:
            c[card] = self.cards.count(card)
        if len(c) == 1:
            return 6  # five of a kind
        elif len(c) == 2:
            if 4 in c.values():
                return 5  # four of a kind
            else:
                return 4  # full house
        elif len(c) == 3:
            if 3 in c.values():
                return 3  # three of a kind
            else:
                return 2  # two pairs
        elif len(c) == 4:
            return 1  # one pair
        else:
            return 0  # high card

    def full_strength(self):
        return 13**5 * self.strength() \
            + sum(13**(4-k) *
                  self.ALL_CARDS.index(self.cards[k]) for k in range(5))

    def __repr__(self):
        return self.cards


class HandJoker(Hand):
    ALL_CARDS = "J23456789TQKA"

    def strength(self):
        c = {}
        for card in self.cards:
            c[card] = self.cards.count(card)
        if len(c) == 1:
            return 6  # five of a kind
        elif len(c) == 2:
            if 4 in c.values():
                if 'J' in c:
                    return 6  # five of a kind with joker(s)
                else:
                    return 5  # four of a kind
            else:
                if 'J' in c:
                    return 6  # five of a kind with joker(s)
                else:
                    return 4  # full house
        elif len(c) == 3:
            if 3 in c.values():
                if 'J' in c:
                    return 4 if c['J'] == 1 and 2 in c.values() else 5
                    # full house with two pairs plus one joker
                    # four of a kind otherwise
                else:
                    return 3  # three of a kind
            else:
                if 'J' in c:
                    return 5 if c['J'] == 2 else 4
                    # four of a kind with joker pair
                    # full house with one joker
                else:
                    return 2  # two pairs
        elif len(c) == 4:
            if 'J' in c:
                return 3  # three of a kind with joker(s)
            else:
                return 1  # one pair
        else:
            return 1 if 'J' in c else 0  # high card or one pair with joker


def partone(lines):
    hands_bids = []
    for line in lines:
        hand_s, bid_s = line.split()
        hands_bids.append({'hand': Hand(hand_s), 'bid': int(bid_s)})
    sorted_hb = sorted(hands_bids, key=lambda x: x['hand'].full_strength())
    return sum((k+1)*hb['bid'] for k, hb in enumerate(sorted_hb))


def parttwo(lines):
    hands_bids = []
    for line in lines:
        hand_s, bid_s = line.split()
        hands_bids.append({'hand': HandJoker(hand_s), 'bid': int(bid_s)})
    sorted_hb = sorted(hands_bids, key=lambda x: x['hand'].full_strength())
    return sum((k+1)*hb['bid'] for k, hb in enumerate(sorted_hb))


print(partone(read_input("input.txt")))
print(parttwo(read_input("input.txt")))
