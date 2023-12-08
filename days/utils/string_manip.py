def str_to_int(data: list[str] | str, split_string=False, deliminator=None):
    if isinstance(data, str):
        if split_string:
            return [int(num.strip()) for num in data.strip().split(deliminator)]
        return [int(str)]
    else:
        return [int(num) for num in data]


def int_list_to_single_int(int_list: list[int]) -> int:
    return [int("".join(map(str, int_list)))]
