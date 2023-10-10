from typing import List


def reverse_strings(input_list: List[str]) -> List[str]:
    """
    Reverses the strings in a given list.

    Parameters:
        input_list (List[str]): The list of strings to be reversed.

    Returns:
        List[str]: A new list containing the reversed strings.

    Examples:
        >>> reverse_strings(['hello', 'world'])
        ['olleh', 'dlrow']
        >>> reverse_strings(['abc', '123'])
        ['cba', '321']

    Raises:
        TypeError: If the input_list contains elements that are not strings.
    """
    # Check if all elements in input_list are strings
    if not all(isinstance(item, str) for item in input_list):
        raise TypeError("All elements in input_list must be strings.")

    # Using map() and a lambda function to reverse each string in the\
    # input_list
    reversed_list = list(map(lambda x: x[::-1], input_list))
    return reversed_list


web_development_words = ['HTML', 'CSS', 'JavaScript', 'Backend',
                         'Frontend', 'Database', 'API', 'Framework',
                         'Responsive', 'Hosting']

# Test cases for reverse_strings function
test_cases = [
    web_development_words,
    ['HTML', 'CSS', 'JavaScript'],
    ['Backend', 'Frontend', 123],
    [],
    ['API', 'Database', ''],
    ['Framework', 'Responsive'],
    ['Hosting', True, 'Python'],
    ['JavaScript', 'Web', None],
    ['CSS', 'Design', '123'],
    ['123', '456', '789']
]


for i, words_list in enumerate(test_cases):
    try:
        print(f"Test Case {i+1}: {words_list}")
        reversed_words = reverse_strings(words_list)
        print("Reversed List:", reversed_words)
    except TypeError as te:
        print(f"Error: {te}")
    print("---------------------")
