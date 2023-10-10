"""
Word Filter Script

This script allows the user to input a list of words separated by spaces.
It then filters the words, keeping only those with a length greater than 5 characters.
The filtered list of words is displayed to the user, along with the count of occurrences for each word.

Usage:
    1. Run the script.
    2. Enter a list of words (separated by spaces) when prompted.
    3. The script will filter the words and display the filtered list.
    4. After displaying the filtered list, the script will ask if you want to continue or exit.
    5. Enter 'yes' to continue or 'no' to exit the script.

Note:
    - Words should consist only of alphabetic characters, and empty words will be ignored.
    - The script counts and displays the occurrences of each word with a length greater than 5 characters.

Example:
    Enter a list of words (separated by spaces): apple banana orange cherry pineapple
    Filtered words (length > 5): banana orange pineapple
    Occurrences of words (length > 5): {'banana': 1, 'orange': 1, 'pineapple': 1}

"""
from typing import List, Dict

import re
from collections import Counter


def is_valid_word(word: str) -> bool:
    """
    Check if a word is valid.

    Parameters:
        word (str): The word to be validated.

    Returns:
        bool: True if the word consists only of alphabetic characters, False otherwise.
    """
    return word.isalpha()


def get_valid_words_from_user() -> List[str]:
    """
    Get a valid list of words from the user.

    Returns:
        list: A list of valid words provided by the user.
    """
    while True:
        user_input = input("Enter a list of words (separated by spaces): ")
        # Use regular expression to extract words while ignoring punctuation and special characters
        words_list = re.findall(r'\b\w+\b', user_input.lower())
        # Filter out invalid words
        valid_words_list = [word for word in words_list if is_valid_word(word)]
        if len(valid_words_list) > 0:
            return valid_words_list
        else:
            print("Invalid input. Please enter only words.")


def filter_long_words(words_list: List[str]) -> List[str]:
    """
    Filter a list of words based on their length.

    Parameters:
        words_list (list): A list of words to be filtered.

    Returns:
        list: A new list containing only words with a length greater than 5 characters.
    """
    return [word for word in words_list if len(word) > 5]


def count_word_occurrences(words_list: List[str]) -> Dict[str, int]:
    """
    Count occurrences of words in the list with a length greater than 5 characters.

    Parameters:
        words_list (list): A list of words to be counted.

    Returns:
        dict: A dictionary with words (length > 5) as keys and their respective counts as values.
    """
    word_counts = Counter(words_list)
    # Filter out words with a length less than or equal to 5 characters
    return {word: count for word, count in word_counts.items() if len(word) > 5}


def get_user_choice() -> str:
    """
    Ask the user if they want to continue or exit the script.

    Returns:
        str: The user's choice, either 'yes', 'no', or 'exit'.
    """
    while True:
        try:
            user_choice = input(
                "Do you want to continue? (Enter 'yes' to continue, 'no' to exit): ").lower()
            if user_choice in ["yes", "no", "exit"]:
                return user_choice
            else:
                print("Invalid choice. Please enter 'yes', 'no', or 'exit'.")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting the program.")
            raise SystemExit
        except Exception as e:
            print("An error occurred:", e)
            print("Please try again.")


def main() -> None:
    """
    The main function to run the Word Filter Script.
    """
    while True:
        words_input = get_valid_words_from_user()
        filtered_words = filter_long_words(words_input)
        print("Filtered words (length > 5):", filtered_words)

        word_occurrences = count_word_occurrences(filtered_words)
        print("Occurrences of words (length > 5):", word_occurrences)

        user_choice = get_user_choice()
        if user_choice == "no":
            print("Exiting the program.")
            break
        elif user_choice == "exit":
            print("Program terminated.")
            return  # Program termination


if __name__ == "__main__":
    main()
