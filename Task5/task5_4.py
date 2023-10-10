import re


def count_lower_upper_symbols(input_string: str) -> tuple:
    """
    Counts the number of lowercase and uppercase letters in the input string.

    Parameters:
        input_string (str): The string to be analyzed.

    Returns:
        tuple: A tuple containing the count of lowercase and uppercase letters.

    Raises:
        TypeError: If the input_string is not a string.
    """
    # Check if input_string is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    # Count the lowercase letters using re.findall()
    lower_count = len(re.findall(r'[a-z]', input_string))

    # Count the uppercase letters using re.findall()
    upper_count = len(re.findall(r'[A-Z]', input_string))

    return lower_count, upper_count


# Test cases for count_lower_upper_symbols function
test_cases = [
    'Web Programming is building websites using HTML, CSS, and JavaScript',
    'this is a test string with only lowercase letters',
    'THIS IS A TEST STRING WITH ONLY UPPERCASE LETTERS',
    'String with 123 numbers and !@# symbols',
    '',
    ['a', 'b', 'c'],
    123,
    True,
    None
]

for i, test_string in enumerate(test_cases):
    try:
        print(f"Test Case {i+1}: {test_string}")
        lower_count, upper_count = count_lower_upper_symbols(test_string)
        print(
            f'Lowercase count: {lower_count}, Uppercase count: {upper_count}')
    except TypeError as te:
        print(f"Error: {te}")
    print("---------------------")
