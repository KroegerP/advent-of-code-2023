from utils.string_manip import int_list_to_single_int, str_to_int


def find_successful_runs(times: list[int], distances: list[int]) -> int:
    result = 1

    for time_and_distance in zip(times, distances):
        successful_times = []
        for button_time_speed in range(time_and_distance[0]):
            num_seconds_left = time_and_distance[0] - button_time_speed
            if (num_seconds_left * button_time_speed) > time_and_distance[1]:
                successful_times.append(button_time_speed)

        print(f"Successful times: {successful_times}")
        result *= len(successful_times)

    print(result)

    return result


def PartOne(file_contents: list[str]):
    times = str_to_int(file_contents[0].split(":")[-1].strip(), split_string=True)
    distances = str_to_int(file_contents[1].split(":")[-1].strip(), split_string=True)

    print(times)
    print(distances)

    result = find_successful_runs(times, distances)

    return result


def PartTwo(file_contents: list[str]):
    times = str_to_int(file_contents[0].split(":")[-1].strip(), split_string=True)
    distances = str_to_int(file_contents[1].split(":")[-1].strip(), split_string=True)

    times = [int_list_to_single_int(times)]
    distances = [int_list_to_single_int(distances)]

    result = find_successful_runs(times, distances)

    return result
