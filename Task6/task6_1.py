import timeit


# Define the input string and the number of iterations
string = 'Hello World' * 90
iterations = 1000


def recursive_reverse_string(string, acc=""):
    """
    Reverses a given string recursively using tail recursion.
    Parameters:
        string (str): The input string to be reversed.
        acc (str, optional): The accumulator to store the reversed string.
        Defaults to ''.
    Returns:
        str: The reversed string.
    Raises:
        TypeError: If the input is not a string.
    """

    if not isinstance(string, str):
        raise TypeError('Input must be a string')

    if not string:
        return acc
    else:
        return recursive_reverse_string(string[1:], string[0] + acc)


def iterative_reverse_string(string):
    """
    Reverses a given string iteratively.
    Parameters:
        string (str): The input string to be reversed.
    Returns:
        str: The reversed string.
    """

    reversed_string = ""
    for char in string:
        reversed_string = f'{char}{reversed_string}'
    return reversed_string


def reversed_reverse_string(string):
    """
    Reverses a given string using the built-in reversed method.
    Parameters:
        string (str): The input string to be reversed.
    Returns:
        str: The reversed string.
    """

    reversed_string = ''.join(reversed(string))
    return reversed_string


def slice_reverse_string(string):
    """
    Reverses a given string using slicing.
    Parameters:
        string (str): The input string to be reversed.
    Returns:
        str: The reversed string.
    """

    return string[::-1]

# Function to measure the execution time of a given function


def measure_execution_time(func):
    """
    Measure the execution time of a given function.
rameters:
        func (callable): The function to be measured.
    Returns:
        float: The total time taken by the function to execute.
    """

    return timeit.timeit(lambda: func(string), number=iterations)


# Dictionary of functions to be tested
functions = {
    'recursive': recursive_reverse_string,
    'iterative': iterative_reverse_string,
    'reversed': reversed_reverse_string,
    'slice': slice_reverse_string
}

# Measure the execution time for all functions and store the results in a list
# of tuples
results = [(name, measure_execution_time(function))
           for name, function in functions.items()]

# Sort the results in ascending order of time
sorted_results = sorted(results, key=lambda item: item[1])

# Get the best time and its name
best_time, best_name = sorted_results[0][1], sorted_results[0][0]

# Calculate the maximum length of the function names for proper alignment
max_name_length = max(len(name) for name, _ in sorted_results)

# Print the results in a table format
print(f"{'#': <3} {'Function': <{max_name_length}} {'Time (s)': <10} "
      f"{'Slower by a factor'}")
for i, (name, time) in enumerate(sorted_results):
    if i == 0:
        print(f"{i: <3} {name: <{max_name_length}} {time:.8f}")
    else:
        ratio = time / best_time
        print(f"{i: <3} {name: <{max_name_length}} {time:.8f} {ratio:.2f}"
              f" times slower than {best_name}")
