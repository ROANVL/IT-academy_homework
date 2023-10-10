from typing import List


def filter_strings_by_length(input_list: List[str]) -> List[str]:
    """
    Filters a list of strings to include only strings with length greater
    than 5.

    Parameters:
        input_list (List[str]): The list of strings to be filtered.

    Returns:
        List[str]: A new list containing only strings with length greater
    than 5.

    Raises:
        TypeError: If the input_list contains elements that are not strings.
    """
    # Check if all elements in input_list are strings
    if not all(isinstance(item, str) for item in input_list):
        raise TypeError("All elements in input_list must be strings.")

    # Filter strings with length greater than 5 using filter() and lambda\
    # function
    filtered_list = list(filter(lambda x: len(x) > 5, input_list))
    return filtered_list


web_development_words = ['HTML', 'CSS', 'JavaScript', 'Backend',
                         'Frontend', 'Database', 'API', 'Framework',
                         'Responsive', 'Hosting']

# Test cases for filter_strings_by_length function
test_cases = [
    web_development_words,
    ['API', 'Frontend', 'DB'],
    [],
    [5, 6, 'HTML'],
    ['a', 'bb', 'ccc', 'dddd'],
    ['Python', 'JavaScript', 'C#'],
    ['hello', 'world', 'apple', 'grape']
]

for i, words_list in enumerate(test_cases):
    try:
        print(f"Test Case {i+1}: {words_list}")
        filtered_words = filter_strings_by_length(words_list)
        print("Filtered List:", filtered_words)
    except TypeError as te:
        print(f"Error: {te}")
    print("---------------------")
