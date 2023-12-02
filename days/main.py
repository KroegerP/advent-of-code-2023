import os

from one.main import PartOne, PartTwo
from utils import read_file


def main(*args, **kwargs):

    print(args)
    data = read_file(f"{os.path.join(os.path.dirname(os.path.abspath(__file__)), f'one/data.txt')}")

    # PartOne(data)

    PartTwo(data)



if __name__ == '__main__':
    main()