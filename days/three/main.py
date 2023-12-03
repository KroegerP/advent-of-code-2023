def check_is_num(string: str, position: int):
    return string[position].isnumeric()


def check_adjacent(cur_line, x_pos, check_pos=True, check_neg=True):
    return (
        True
        if (check_is_num(cur_line, x_pos + 1) and check_pos)
        or (check_is_num(cur_line, x_pos - 1) and check_neg)
        else False
    )


def GetNumber(file_contents: list[str], x: int, y: int):
    cur_char = "" + file_contents[y][x]
    cur_line = file_contents[y]

    # print(f"starting char number {cur_char}")

    if x != 0:
        for left_char in range(x - 1, 0, -1):
            if cur_line[left_char].isnumeric():
                # print(f"Adding {cur_line[left_char]}")
                cur_char = f"{cur_line[left_char]}{cur_char}"
                # print(f"New Char: {cur_char}")
            elif not cur_line[left_char].isalnum():
                break
    if x != len(cur_line) - 1:
        for right_char in range(x + 1, len(cur_line)):
            if cur_line[right_char].isnumeric():
                # print(f"Adding {cur_line[right_char]}")
                cur_char = f"{cur_char}{cur_line[right_char]}"
            elif not cur_line[right_char].isalnum():
                break

    result = int(cur_char)

    print(f"Adding {result}")

    return result


def check_surroundings(file_contents: list[str], cur_x: int, cur_y: int) -> list[tuple]:
    print(f"Snapshot for {file_contents[cur_y][cur_x]}:")
    try:
        [
            print(line)
            for line in [
                file_contents[cur_y - 1][cur_x - 5 : cur_x + 5],
                file_contents[cur_y][cur_x - 5 : cur_x + 5],
                file_contents[cur_y + 1][cur_x - 5 : cur_x + 5],
            ]
        ]
    except:
        print("ERROR")
    surrounding_nums = []
    SURROUNDING_PAIRS = [
        [cur_x + 1, cur_y],
        [cur_x - 1, cur_y],
        [cur_x, cur_y + 1],
        [cur_x, cur_y - 1],
        [cur_x + 1, cur_y + 1],
        [cur_x - 1, cur_y + 1],
        [cur_x - 1, cur_y - 1],
        [cur_x + 1, cur_y - 1],
    ]

    def add_pair(line, x: int, y: int):
        surrounding_nums.append((x, y))

    plus_y_0 = False
    minus_y_0 = False

    for [x, y] in SURROUNDING_PAIRS:
        try:
            char = file_contents[y][x]
        except IndexError:
            print("ERROR")
            continue
        cur_line = file_contents[y]
        if char.isnumeric():
            if y - cur_y == 0:
                add_pair(cur_line, x, y)
            elif y - cur_y == 1 and not plus_y_0:
                if x - cur_x == 0:
                    add_pair(cur_line, x, y)
                    plus_y_0 = True
                elif x - cur_x == 1:
                    add_pair(cur_line, x, y)
                elif x - cur_x == -1:
                    add_pair(cur_line, x, y)
            elif y - cur_y == -1 and not minus_y_0:
                if x - cur_x == 0:
                    add_pair(cur_line, x, y)
                    minus_y_0 = True
                elif x - cur_x == 1:
                    add_pair(cur_line, x, y)
                elif x - cur_x == -1:
                    add_pair(cur_line, x, y)

    return surrounding_nums


def get_special_chars(file_contents: list[str]) -> list[tuple]:
    special_char_locs = []

    for index_y, line in enumerate(file_contents):
        for index_x, char in enumerate(line):
            if not char.isalnum() and char != ".":
                print(f"Found special char {char}")
                special_char_locs.append([index_x, index_y])
    return special_char_locs


def get_particular_char(file_contents: list[str], searching_char="*") -> list[tuple]:
    special_char_locs = []

    for index_y, line in enumerate(file_contents):
        for index_x, char in enumerate(line):
            if char == searching_char:
                print(f"Found special char {char}")
                special_char_locs.append([index_x, index_y])
    return special_char_locs


def PartOne(file_contents: list[str]):
    result = 0

    special_char_coords = get_special_chars(file_contents)

    for [x, y] in special_char_coords:
        numbers_near = check_surroundings(file_contents, x, y)

        if len(numbers_near) == 0:
            print("ERROR")
            raise IndexError

        if len(numbers_near) == 1:
            print("ONLY ONE")

        for numbers in numbers_near:
            number = GetNumber(file_contents, numbers[0], numbers[1])

            result += number

    print(result)

    return result


def PartTwo(file_contents: list[str]):
    result = 0

    special_char_coords = get_particular_char(file_contents)

    for [x, y] in special_char_coords:
        numbers_near = check_surroundings(file_contents, x, y)

        gear_nums = []

        for numbers in numbers_near:
            number = GetNumber(file_contents, numbers[0], numbers[1])

            gear_nums.append(number)

        if len(gear_nums) > 2:
            print("Too many")
            continue
        elif len(gear_nums) <= 1:
            print("Not enough numbers")
            continue

        ratio = gear_nums[0] * gear_nums[1]

        result += ratio

    print(result)

    return result
