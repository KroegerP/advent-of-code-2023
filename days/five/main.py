from utils.string_manip import str_to_int


def build_single_map():
    return {
        "soil": None,
        "fertilizer": None,
        "water": None,
        "light": None,
        "temperature": None,
        "humidity": None,
        "location": None,
    }


def build_seed_maps(seed_line: str):
    parsed_numbers = str_to_int(seed_line, split_string=True)

    # print(f"SEEDS: {parsed_numbers}")

    full_map = {}

    for seed_num in parsed_numbers:
        full_map[f"{seed_num}"] = build_single_map()

    return full_map


def parse_a_to_b_map(line: str):
    parsed = line.split("-")
    return [parsed[0], parsed[-1].split()[0]]


def get_full_str_number(string: str, starting_idx=0):
    cur_string = ""
    for index in range(starting_idx, len(string)):
        if string[index].isnumeric():
            # cur_string.join(string[index])
            cur_string = f"{cur_string}{string[index]}"
        else:
            return [int(cur_string), index]

    return [int(cur_string), len(string)]


def get_map_list(file_contents: list[str], cur_idx):
    cur_list = []
    idx = 0
    while file_contents[cur_idx + idx] != "":
        if file_contents[cur_idx + idx] == "":
            break
        cur_list.append(file_contents[cur_idx + idx])
        idx += 1

        if (cur_idx + idx + 1) >= len(file_contents):
            break

    return cur_list


def find_matching_tuples(tuple_list: list[tuple], current_numbers: list[int]):
    found_pairs = current_numbers

    source_mappings = [values[0] for values in tuple_list]
    destination_mappings = [values[1] for values in tuple_list]

    for index, cur_num in enumerate(current_numbers):
        if cur_num in source_mappings:
            num_index = source_mappings.index(cur_num)

            mapped_value = destination_mappings[num_index]

            found_pairs[index] = mapped_value

    return found_pairs


# def get_data_values(
#     dest: int, source: int, range_len: int, parsed_numbers: list[int], cur_list, i=0
# ):
#     if i == range_len:
#         return cur_list

#     cur_value = source + i

#     # print(cur_list)

#     if cur_value in parsed_numbers:
#         cur_list.append((cur_value, (dest + i)))

#     new_list = get_data_values(dest, source, range_len, parsed_numbers, cur_list, i + 1)

#     return new_list


# def get_data_values(
#     dest: int, source: int, range_len: int, parsed_numbers: list[int], cur_list, i=0
# ):
#     # incremented_numbers = [p + source for p in parsed_numbers]
#     found_pairs = []

#     for p in parsed_numbers:
#         if p >= source and p <= range_len + source:


def PartOne(file_contents: list[str]):
    lowest_location = 0
    parsed_numbers = str_to_int(file_contents[0].split(":")[-1], split_string=True)

    print(parsed_numbers)

    # return

    # print(f"Seed Map: \n {seed_map}")

    # numbers_map = {}

    for index, line in enumerate(file_contents):
        if index < 2:
            continue
        try:
            first_char = line[0]
        except IndexError:
            continue

        if first_char.isalpha() and not first_char.isnumeric():
            a, b = parse_a_to_b_map(line)

            # print(f"Getting {a} to {b} mapping")
            mapping_key = f"{a}-to-{b}"

            # numbers_map[mapping_key] = []

            map_list = get_map_list(file_contents, index + 1)

            print(map_list)

            numbers_map = []

            for mapping_line in map_list:
                [dest, source, range_len] = [int(num) for num in mapping_line.split()]

                print(f"Dest: {dest}, Source: {source}, Range: {range_len}")

                data_values = [
                    (source + i, dest + i)
                    for i in range(range_len)
                    if (source + i) in parsed_numbers
                ]

                # data_values = get_data_values(
                #     dest, source, range_len, parsed_numbers, []
                # )

                # print(f"Data Values {data_values}")

                # numbers_map[mapping_key] += mapped_ranged
                numbers_map += data_values

            print(numbers_map)

            parsed_numbers = find_matching_tuples(numbers_map, parsed_numbers)

            print(f"New Numbers for {mapping_key}: {parsed_numbers}")

    # print(numbers_map)

    # soil_nums = find_matching_tuples(numbers_map["seed-to-soil"], parsed_numbers)
    # fertilizer_nums = find_matching_tuples(numbers_map["soil-to-fertilizer"], soil_nums)
    # water_nums = find_matching_tuples(
    #     numbers_map["fertilizer-to-water"], fertilizer_nums
    # )
    # light_nums = find_matching_tuples(numbers_map["water-to-light"], water_nums)
    # temperature_nums = find_matching_tuples(
    #     numbers_map["light-to-temperature"], light_nums
    # )
    # humidity_nums = find_matching_tuples(
    #     numbers_map["temperature-to-humidity"], temperature_nums
    # )
    # location_nums = find_matching_tuples(
    #     numbers_map["humidity-to-location"], humidity_nums
    # )

    print(parsed_numbers)
    # print(location_nums)

    # print(lowest_location)

    return lowest_location


def expand_seeds(parsed_numbers: list[int]):
    new_seeds = []
    for index in range(int(len(parsed_numbers) / 2)):
        if index % 2 == 1:
            continue
        new_seeds += [
            parsed_numbers[index] + n_seed
            for n_seed in range(parsed_numbers[index + 1])
        ]

        print("Cur Seeds \n")
        print(new_seeds)

    return new_seeds


def PartTwo(file_contents: list[str]):
    lowest_location = 0
    parsed_numbers = str_to_int(file_contents[0].split(":")[-1], split_string=True)

    print(parsed_numbers)

    parsed_numbers = expand_seeds(parsed_numbers)
    print(parsed_numbers)

    return

    # return

    # print(f"Seed Map: \n {seed_map}")

    # numbers_map = {}

    for index, line in enumerate(file_contents):
        if index < 2:
            continue
        try:
            first_char = line[0]
        except IndexError:
            continue

        if first_char.isalpha() and not first_char.isnumeric():
            a, b = parse_a_to_b_map(line)

            # print(f"Getting {a} to {b} mapping")
            mapping_key = f"{a}-to-{b}"

            # numbers_map[mapping_key] = []

            map_list = get_map_list(file_contents, index + 1)

            print(map_list)

            numbers_map = []

            for mapping_line in map_list:
                [dest, source, range_len] = [int(num) for num in mapping_line.split()]

                print(f"Dest: {dest}, Source: {source}, Range: {range_len}")

                data_values = [
                    (source + i, dest + i)
                    for i in range(range_len)
                    if (source + i) in parsed_numbers
                ]

                # data_values = get_data_values(
                #     dest, source, range_len, parsed_numbers, []
                # )

                # print(f"Data Values {data_values}")

                # numbers_map[mapping_key] += mapped_ranged
                numbers_map += data_values

            print(numbers_map)

            parsed_numbers = find_matching_tuples(numbers_map, parsed_numbers)

            print(f"New Numbers for {mapping_key}: {parsed_numbers}")

    print(parsed_numbers)
    print(min(parsed_numbers))

    # print(lowest_location)

    return lowest_location
