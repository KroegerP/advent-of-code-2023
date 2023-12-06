from utils.string_manip import str_to_int



def PartOne(file_contents: list[str]):
    times = str_to_int(file_contents[0].split(":")[-1].strip(), split_string=True)
    distances = str_to_int(file_contents[1].split(":")[-1].strip(), split_string=True)
    
    print(times)
    print(distances)

    for time_and_distance in zip(times, distances):
        for button_time_speed in range(time_and_distance[0]):
            if ((button_time_speed - time_and_distance[0]) + button_time_speed):
                print("LOL")

    return

def PartTwo(file_contents: list[str]):
    return