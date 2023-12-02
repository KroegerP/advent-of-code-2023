

def PartOne(file_contents: list[str]):
    
    total = 0
    for line in file_contents:
        number_list = []
        for char in line:
            if char.isnumeric():
                number_list.append(char)
        print(f"{number_list} and {total}")
        total += int(number_list[0] + number_list[-1])

    print(f"Result: {total}")

def PartTwo(file_contents: list[str]):

    number_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    word_numbers = set(list(number_dict.keys()))
    first_letters = [entry[0] for entry in word_numbers]

    print(first_letters)
    
    total = 0
    for line in file_contents:
        number_list = []
        for index, char in enumerate(line):
            if char.isnumeric():
                number_list.append(char)
            elif char in first_letters:
                print(line[index:index + 5])
                if str(line[index:index + 5]) in word_numbers:
                    number_list.append(number_dict[str(line[index:index + 5])])
                elif str(line[index:index + 4]) in word_numbers:
                    number_list.append(number_dict[str(line[index:index + 4])])
                elif str(line[index:index + 3]) in word_numbers:
                    number_list.append(number_dict[str(line[index:index + 3])])
            
        total += int(number_list[0] + number_list[-1])

    print(f"Result: {total}")

