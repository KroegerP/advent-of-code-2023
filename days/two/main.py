NUM_RED = 12
NUM_BLUE = 14
NUM_GREEN = 13


def PartOne(file_contents: list[str]):
    valid_game_nums = []
    for line in file_contents:
        game_and_sets = line.split(":")
        game_num = int(game_and_sets[0].split(" ")[-1])

        game_sets = game_and_sets[-1].split(";")

        red = 0
        blue = 0
        green = 0
        valid = True

        for cur_set in game_sets:
            displayed_colors = cur_set.split(",")

            print(f"DISPLAYED COLORS: {displayed_colors}")

            for color in displayed_colors:
                count = int(color.lstrip().split(" ")[0])
                if "red" in color:
                    if count > NUM_RED:
                        valid = False
                    # red += int(color.split(" ")[0])
                elif "green" in color:
                    if count > NUM_GREEN:
                        valid = False
                    # green += int(color.split(" ")[0])
                elif "blue" in color:
                    if count > NUM_BLUE:
                        valid = False
                    # blue += int(color.split(" ")[0])

        if valid:
            valid_game_nums.append(game_num)

    result = sum(valid_game_nums)
    print(result)


def PartTwo(file_contents: list[str]):
    valid_game_nums = []
    for line in file_contents:
        game_and_sets = line.split(":")
        game_num = int(game_and_sets[0].split(" ")[-1])

        game_sets = game_and_sets[-1].split(";")

        red = 0
        blue = 0
        green = 0
        valid = True

        for cur_set in game_sets:
            displayed_colors = cur_set.split(",")

            print(f"DISPLAYED COLORS: {displayed_colors}")

            for color in displayed_colors:
                count = int(color.lstrip().split(" ")[0])
                if "red" in color:
                    if count > red:
                        red = count
                elif "green" in color:
                    if count > green:
                        green = count
                    # green += int(color.split(" ")[0])
                elif "blue" in color:
                    if count > blue:
                        blue = count
                    # blue += int(color.split(" ")[0])

        valid_game_nums.append(blue * red * green)

    result = sum(valid_game_nums)
    print(result)
