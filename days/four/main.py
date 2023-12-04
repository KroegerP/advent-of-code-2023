def str_to_int(data: list[str] | str, split_string=False, deliminator=None):
    if isinstance(data, str):
        if split_string:
            return [int(num.strip()) for num in data.strip().split(deliminator)]
        return [int(str)]
    else:
        return [int(num) for num in data]


def PartOne(file_contents: list[str]):
    result = 0
    for line in file_contents:
        point_total = 0

        card_and_sets = line.split(":")
        num_lists = card_and_sets[-1].split("|")
        winning_nums = str_to_int(num_lists[0], True)
        given_nums = str_to_int(num_lists[-1], True)

        for g_num in given_nums:
            if g_num in winning_nums:
                point_total = point_total * 2 if point_total != 0 else 1

        result += point_total

    # print(result)

    return result


def PartTwo(file_contents: list[str]):
    result = 0
    card_counts = [1] * len(file_contents)
    for line in file_contents:
        point_total = 0
        winning_count = 0

        card_and_sets = line.split(":")
        card_num = int(card_and_sets[0].split()[-1]) - 1
        num_lists = card_and_sets[-1].split("|")
        winning_nums = str_to_int(num_lists[0], True)
        given_nums = str_to_int(num_lists[-1], True)

        # print(given_nums)
        # print(winning_nums)

        for g_num in given_nums:
            if g_num in winning_nums:
                winning_count += 1

        print(f"CARD {card_num + 1} has {winning_count} winning numbers")
        print(card_counts)
        print(card_counts[card_num])
        for card in range(card_counts[card_num]):
            for offset in range(1, winning_count + 1):
                card_counts[card_num + offset] += 1

    print(sum(card_counts))

    return result
