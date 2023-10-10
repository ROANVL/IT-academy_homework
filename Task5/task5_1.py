from functools import reduce


def sum_two_integers(*args: int) -> int:
    # Check if at least two arguments are provided
    if len(args) < 2:
        raise ValueError('Please provide at least two integers.')

    # Check if all arguments are integers
    if not all(isinstance(arg, int) for arg in args):
        invalid_args = [str(arg) for arg in args if not isinstance(arg, int)]
        raise TypeError(
            f'Invalid arguments: {", ".join(invalid_args)}. All arguments must'
            'be integers.')

    # Calculate the sum using the reduce function
    return reduce(lambda x, y: x + y, args)


test_cases = [
    [5, 6],
    [-3, 8],
    [10, 20],
    [0, 0],
    [100, 200],
    [5, '6'],
    [5.5, 6.6],
    [1],
    [],
]

for numbers in test_cases:
    try:
        if len(numbers) >= 2:
            result = sum_two_integers(*numbers)
            print(
                f'The sum of {numbers[0]} and {numbers[1]} '
                f'is equal to {result}')
        else:
            raise ValueError("Please provide at least two integers.")
    except ValueError as ve:
        print(f'Error: {ve}')
    except TypeError as te:
        print(f'Error: {te}')
