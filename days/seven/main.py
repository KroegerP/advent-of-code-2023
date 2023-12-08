CARD_TYPES = {
    "Five": "Five of a Kind",
    "Four": "Four of a Kind",
    "Full": "Full House",
    "Three": "Three of a Kind",
    "TwoPair": "Two Pair",
    "OnePair": "One Pair",
    "High": "High Card",
}

card_dict = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}


class CamelCardsHand:
    hand: str = ""
    hand_type: str = None
    bid: int = 0
    rank: int = 0

    def __init__(self, _hand: str, _bid: int) -> None:
        self.hand = _hand
        self.bid = _bid

    def is_of_a_kind(self, num_to_match: int, two_pairs=False, use_j=True):
        freq_map = {"J": 0}
        for card in self.hand:
            # if len(freq_map.keys())
            if card not in freq_map.keys():
                freq_map[card] = 1
            else:
                freq_map[card] += 1

        # print(f"J's: {freq_map.get('J', 0)}")

        j_freq = freq_map.get("J")

        del freq_map["J"]

        if num_to_match == 5 and j_freq == 5:
            return True

        if use_j:
            matching_num = num_to_match - j_freq
        else:
            matching_num = num_to_match

        if matching_num in list(freq_map.values()):
            if (num_to_match) == 2 and two_pairs:
                match_count = [
                    c for c in list(freq_map.values()) if c == (num_to_match)
                ]

                if j_freq > 0 and use_j:
                    match_count.append("J")
                    # print(f"MATCH COUNT: {match_count}, HAND: {self.hand}")
                elif not use_j and j_freq == 0:
                    return True

                if len(match_count) < 2:
                    return False
            return True

        return False

    def is_five_of_a_kind(self):
        return self.is_of_a_kind(5)

    def is_four_of_a_kind(self):
        return self.is_of_a_kind(4)

    def is_three_of_a_kind(self):
        return self.is_of_a_kind(3)

    # Two pairs var allows to check for 2 pairs with this
    def has_two_of_a_kind(self, two_pairs=False, use_j=True):
        return self.is_of_a_kind(2, two_pairs, use_j)

    def determine_hand_type(self):
        if self.hand_type != None:
            return

        if self.is_five_of_a_kind():
            # print(f"{self.hand} 5 MATCHES.")
            self.hand_type = CARD_TYPES["Five"]
            return

        if self.is_four_of_a_kind():
            print(f"{self.hand} 4 MATCHES.")
            self.hand_type = CARD_TYPES["Four"]
            return

        if self.is_three_of_a_kind():
            if self.has_two_of_a_kind(two_pairs=True, use_j=False):
                # print(f"{self.hand} FULL HOUSE.")
                self.hand_type = CARD_TYPES["Full"]
            else:
                # print(f"{self.hand} 3 MATCHES.")
                self.hand_type = CARD_TYPES["Three"]
            return

        if self.has_two_of_a_kind(two_pairs=True):
            # print(f"{self.hand} TWO PAIRS.")
            self.hand_type = CARD_TYPES["TwoPair"]
            return

        if self.has_two_of_a_kind():
            # print(f"{self.hand} ONE PAIR.")
            self.hand_type = CARD_TYPES["OnePair"]
            return

        self.hand_type = CARD_TYPES["High"]

        return


# def check_


def sort_by_cards(hands: list[CamelCardsHand], rank):
    for h in hands:
        h.rank = rank


# This is gross
def set_hand_ranks(hands: list[CamelCardsHand]):
    five_kinds = [h for h in hands if h.hand_type == CARD_TYPES["Five"]]
    sort_by_cards(five_kinds, 7)

    four_kinds = [h for h in hands if h.hand_type == CARD_TYPES["Four"]]
    sort_by_cards(four_kinds, 6)

    full_houses = [h for h in hands if h.hand_type == CARD_TYPES["Full"]]
    sort_by_cards(full_houses, 5)

    three_kinds = [h for h in hands if h.hand_type == CARD_TYPES["Three"]]
    sort_by_cards(three_kinds, 4)

    two_pairs = [h for h in hands if h.hand_type == CARD_TYPES["TwoPair"]]
    sort_by_cards(two_pairs, 3)

    one_pairs = [h for h in hands if h.hand_type == CARD_TYPES["OnePair"]]
    sort_by_cards(one_pairs, 2)

    highs = [h for h in hands if h.hand_type == CARD_TYPES["High"]]
    sort_by_cards(highs, 1)


def PartOne(file_contents: list[str]):
    hands = [
        CamelCardsHand(line.split(" ")[0], int(line.split(" ")[-1]))
        for line in file_contents
    ]

    for hand in hands:
        hand.determine_hand_type()

        # print(f"{hand.hand}: {hand.hand_type}")

    set_hand_ranks(hands)

    def sorter(hand: CamelCardsHand):
        return hand.rank

    sorted_ranks = sorted(
        hands,
        key=lambda h: (
            h.rank,
            card_dict[h.hand[0]],
            card_dict[h.hand[1]],
            card_dict[h.hand[2]],
            card_dict[h.hand[3]],
            card_dict[h.hand[4]],
        ),
    )

    # print("Final sort")
    # [print(f"{s.hand} {s.hand_type}") for s in sorted_ranks]

    result = 0

    for index, hand in enumerate(sorted_ranks):
        result += hand.bid * (index + 1)

    print(result)

    return result


def PartTwo(file_contents: list[str]):
    return
