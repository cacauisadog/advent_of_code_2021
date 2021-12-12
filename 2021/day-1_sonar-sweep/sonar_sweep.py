import os

FILE_NAME = 'input.txt'


def read_input_file(file_name: str) -> str:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, file_name)
    input = open(file_path, 'r')
    input_str = input.read()
    input.close()
    return input_str.split('\n')


def count_measurement_increases(input: str) -> None:
    increases = 0
    for i, entry in enumerate(input):
        if i > 0:
            if int(entry) > int(input[i-1]):
                increases += 1

    return increases


input = read_input_file(FILE_NAME)
print(count_measurement_increases(input))
