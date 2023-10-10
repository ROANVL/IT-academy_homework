from itertools import groupby
from typing import List


def get_ranges(numbers: List[int]) -> str:
    """
    Returns a string representing ranges in a list of numbers.
    Parameters:
        numbers (List[int]): The list of integers to find ranges in.
    Returns:
        str: A string representing the ranges in the list of numbers.
    Raises:
        TypeError: If the input is not a list of integers.
    """
    # Check if numbers is a list of integers
    if not isinstance(numbers, list) or not \
            all(isinstance(item, int) for item in numbers):
        raise TypeError("Input must be a list of integers.")

    # Remove duplicates and sort the list
    unique_numbers = sorted(set(numbers))

    # Initialize the result list
    result = []

    # Group the numbers into ranges using groupby
    for _, group in groupby(enumerate(unique_numbers), lambda x: x[1] - x[0]):
        group = list(group)
        start = group[0][1]
        end = group[-1][1]
        if start == end:
            result.append(str(start))
        else:
            result.append(f'{start}-{end}')

    # Join the result list into a single string
    return ', '.join(result)


def pretty_print_ranges(test_cases):
    for i, numbers in enumerate(test_cases):
        try:
            result = get_ranges(numbers)
            print(f'{"=" * 50}\nTest Case {i+1}:\n{"-" * 50}\n'
                  f'Input: {numbers}\n'
                  f'Output: "{result}"')
        except TypeError as te:
            print(f'{"=" * 50}\nTest Case {i+1}:\n{"-" * 50}\n'
                  f'Input: {numbers}\n'
                  f'Error: {te}')


# Test cases for get_ranges function
test_cases = [
    [0, 1, 2, 3, 4, 7, 8, 10],
    [4, 7, 10],
    [2, 3, 8, 9],
    [],
    [1, 1, 1, 1, 1, 1],
    [8],
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 5, 6, 10, 11, 12],
    [20, 21],
    [30, 35],
    [40, 41, 42, 45],
    [59, 58, 59, 50, 50, 51, 52, 52, 52, 53],
    [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4],
    [100, 101, 105, 106, 109, 110, 112],
    [1, 2, 3, '4', 5],
    [True, False, 1, 2],
    [1, 2, 3, [4, 5]],
    [1, 2, 3, {'a': 1, 'b': 2}],
    [1, 2, None, 3],
]

pretty_print_ranges(test_cases)
