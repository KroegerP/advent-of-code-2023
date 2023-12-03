import os
import sys
from three.main import PartOne, PartTwo
from utils import read_file


def main():
    if len(sys.argv) < 2:
        print("User did not supply day!")
        return
    data = read_file(
        f"{os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{sys.argv[1]}/data.txt')}"
    )

    PartOne(data)

    PartTwo(data)


if __name__ == "__main__":
    main()
