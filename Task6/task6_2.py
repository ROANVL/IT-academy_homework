"""
Web Text Analysis Module

This module facilitates fetching texts from web pages, checking for
palindromes, and categorizing them based on their properties.

It provides functions to extract texts from URLs, clean and normalize text by
removing non-alphanumeric characters and converting to lowercase, check if a
string is a palindrome, and categorize strings into different categories such
as pure palindromes and those with spaces.

Dependencies:
    - re (regular expressions)
    - requests (HTTP requests)
    - BeautifulSoup (HTML parsing)
    - collections (defaultdict)

Constants:
    - CATEGORY_PALINDROME: String label for pure palindromes
    - CATEGORY_PALINDROME_WITH_SPACES: String label for palindromes with spaces
    - CATEGORY_NON_PALINDROME: String label for non-palindromes
    - TEST_STRINGS: List of test strings to start with
    - ELEMENTS_TO_FETCH: List of dictionaries containing URL information for
    fetching texts

Functions:
    - fetch_texts_from_url: Fetches texts from a web page by URL and extracts
      from specific elements
    - clean_and_normalize_text: Cleans and normalizes input text for palindrome
      checking
    - recursive_palindrome_check: Recursive helper function to check if a text
      is a palindrome
    - is_string_palindrome: Checks if a given string is a palindrome
    - categorize_strings: Categorizes a list of strings into different
      palindrome categories
    - print_strings_with_label: Prints a list of strings with a label
    - main: Main function to orchestrate text fetching, categorization, and
      printing
"""

import re
import requests
from bs4 import BeautifulSoup
from collections import defaultdict


# Constants for test strings
TEST_STRINGS = [" ", 'A', '  ', '   ', 'Ток как кот']

# Constants for URL fetching
ELEMENTS_TO_FETCH = [
    # List of dictionaries with URL information to fetch texts from
    {
        'url': 'http://english2017.ru/english-palindrome',
        'element_name': 'span',
        'start_index': 7,
        'end_index': 57,
        'limit': None
    },
    {
        'url': ('https://www.analogi.net/igra/'
                'slova-palindromy-i-stroka-palindrom'),
        'element_name': 'li',
        'start_index': 70,
        'end_index': 130,
        'limit': None
    },
]

# Constants for categorized strings
CATEGORY_PALINDROME = 'palindrome'
CATEGORY_PALINDROME_WITH_SPACES = 'palindrome_with_spaces'
CATEGORY_NON_PALINDROME = 'non_palindrome'

HORIZONTAL_LINE = '-' * 40


def fetch_texts_from_url(url, element_name, start_index,
                         end_index, limit=None):
    """
    Fetch texts from a web page by URL and extract them from specific elements.

    Args:
        url (str): The URL of the web page to fetch texts from.
        element_name (str): The name of the HTML element to find and extract
        texts from.
        start_index (int): The starting index for slicing the elements.
        end_index (int): The ending index for slicing the elements.
        limit (int, optional): The maximum number of elements to fetch and
        process.

    Returns:
        list: A list of cleaned and normalized texts extracted from the
        specified elements.
    """
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all elements with the specified element_name
        all_elements = soup.find_all(element_name)

        if limit is not None:
            all_elements = all_elements[:limit]

        # Extract and return the text from the elements, excluding empty texts
        result = [element.text for element in
                  all_elements[start_index:end_index]
                  if element.text.strip()]
        return result

    else:
        raise ConnectionError(
            f"Failed to fetch the URL: {url}. Status code: "
            f"{response.status_code}")


def clean_and_normalize_text(text):
    """
    Clean and normalize the input text by removing non-alphanumeric characters
    and spaces, and converting it to lowercase.

    Args:
        text (str): The input text to be cleaned and normalized.

    Returns:
        str: The cleaned and normalized text.
    """
    cleaned_text = re.sub(r'[^a-zA-Zа-яА-Я0-9]', '', text)
    cleaned_text = cleaned_text.strip().lower()
    return cleaned_text


def recursive_palindrome_check(text):
    """
    Recursive helper function to check if the text is a palindrome.

    Args:
        text (str): The text to be checked for a palindrome.

    Returns:
        bool: True if the text is a palindrome, False otherwise.
    """
    text = re.sub(r'[^\w\s]', '', text)
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return recursive_palindrome_check(text[1:-1])


def is_string_palindrome(the_string):
    """
    Check if a given string is a palindrome.

    Args:
        the_string (str): The input string to be checked for a palindrome.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    cleaned_string = clean_and_normalize_text(the_string)
    return recursive_palindrome_check(cleaned_string)


def categorize_strings(strings):
    """
    Categorize a list of strings into different palindrome categories.

    Args:
        strings (list): The list of strings to be categorized.

    Returns:
        tuple: A tuple containing two defaultdict objects:
            - The first defaultdict contains counters for different categories.
            - The second defaultdict contains lists of strings for each
              category.
    """
    # Initialize counters for different categories and defaultdict for
    # categorized strings
    counters = defaultdict(int)
    categorized_strings = defaultdict(list)

    # Iterate through the input strings to categorize and count palindromes
    for text in strings:
        cleaned_text = clean_and_normalize_text(text)

        if is_string_palindrome(cleaned_text):
            counters[CATEGORY_PALINDROME] += 1
            if len(text) > 1 and text.strip() and " " in text\
                    and recursive_palindrome_check(text.lower()):
                counters[CATEGORY_PALINDROME_WITH_SPACES] += 1
                categorized_strings[CATEGORY_PALINDROME_WITH_SPACES].append(
                    text)
            categorized_strings[CATEGORY_PALINDROME].append(text)
        else:
            counters[CATEGORY_NON_PALINDROME] += 1
            categorized_strings[CATEGORY_NON_PALINDROME].append(text)

    return counters, categorized_strings


def print_strings_with_label(strings_list, label_text):
    """
    Print a list of strings with a label.

    Args:
        strings_list (list): The list of strings to print.
        label_text (str): The label to print before the list.

    Returns:
        None
    """
    if strings_list:
        max_index_width = len(str(len(strings_list)))
        print(label_text)
        for index, string in enumerate(strings_list, 1):
            index_str = f"{index:>{max_index_width}}"
            print(f"{index_str}. '{string}'")
    else:
        print(f"No {label_text.lower()} found.")


def main():
    print("Fetching texts from web pages...")

    counters, categorized_strings = categorize_strings(TEST_STRINGS)

    for url_info in ELEMENTS_TO_FETCH:
        try:
            parsed_texts = fetch_texts_from_url(**url_info)
            TEST_STRINGS.extend(parsed_texts)
        except ConnectionError as e:
            print(f"Failed to fetch the URL: {url_info['url']}. Error: {e}")

    counters, categorized_strings = categorize_strings(TEST_STRINGS)

    # Sort categorized_strings by category
    sorted_categorized_strings = {
        category: sorted(strings) for category, strings in categorized_strings.items()
    }

    for category, count in counters.items():
        print_strings_with_label(
            sorted_categorized_strings[category],
            f"\n{HORIZONTAL_LINE}\n{category.upper()} "
            f"({count}):\n{HORIZONTAL_LINE}")


if __name__ == "__main__":
    main()
