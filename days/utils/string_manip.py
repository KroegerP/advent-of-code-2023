def str_to_int(data: list[str] | str, split_string=False, deliminator=None):
    if isinstance(data, str):
        if split_string:
            return [int(num.strip()) for num in data.strip().split(deliminator)]
        return [int(str)]
    else:
        return [int(num) for num in data]
