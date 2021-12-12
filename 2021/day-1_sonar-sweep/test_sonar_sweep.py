import pytest
import os
from sonar_sweep import count_measurement_increases


@pytest.fixture
def input():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "test_input.txt")
    input = open(file_path, 'r')
    input_str = input.read()
    input.close()
    return input_str.split('\n')


def test_measurement_increases(input):
    expected_increases = 7
    actual_increases = count_measurement_increases(input)
    assert actual_increases == expected_increases
