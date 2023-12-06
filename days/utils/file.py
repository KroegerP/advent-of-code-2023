import os


def read_file(path: str):
    with open(path) as data:
        result = data.read()
        # print(result)
        split = result.split("\n")
        # print(split)
        return split
