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

        if (cur_idx + idx + 1) > len(file_contents):
            break

    return cur_list


def find_matching_tuples(tuple_list: list[tuple], current_numbers: list[int]):
    found_pairs = [False] * len(current_numbers)

    source_mappings = [values[0] for values in tuple_list]
    destination_mappings = [values[1] for values in tuple_list]

    for index, cur_num in enumerate(current_numbers):
        if cur_num in source_mappings:
            num_index = source_mappings.index(cur_num)

            mapped_value = destination_mappings[num_index]

            found_pairs[index] = mapped_value

    for index, pair in enumerate(found_pairs):
        if not pair:
            found_pairs[index] = current_numbers[index]

    return found_pairs


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

            # print(map_list)

            numbers_map = []

            for mapping_line in map_list:
                dest_start, dest_final_idx = get_full_str_number(mapping_line, 0)
                source_start, source_final_idx = get_full_str_number(
                    mapping_line, dest_final_idx + 1
                )
                range_len, _ = get_full_str_number(mapping_line, source_final_idx + 1)

                # print(f"Dest: {dest_start}, Source: {source_start}, Range: {range_len}")

                dest_range = [int(dest_start) + i for i in range(range_len)]
                source_range = [int(source_start) + i for i in range(range_len)]

                mapped_ranged = zip(source_range, dest_range)

                # numbers_map[mapping_key] += mapped_ranged
                numbers_map += mapped_ranged

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


def PartTwo(file_contents: list[str]):
    return
