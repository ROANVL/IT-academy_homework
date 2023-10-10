"""
Vowel Counter and Language Detection

This script allows you to input a text string either from the keyboard or 
a file and detect its language. It then counts the number of vowels in the 
input string based on the detected language and plots a histogram to visualize
the distribution of vowel counts across supported languages.

Usage:
1. Choose the source of the input string:
    - If you choose '1', you can input a string from the keyboard.
    - If you choose '2', the script will attempt to read a text file 
    ('test(war and peace)_task3_1.txt') and detect its language.

2. If you input the string from the keyboard:
    - You will be prompted to choose the language of the input string from the 
    following options:
        'en' - English,
        'ru' - Russian,
        'pl' - Polish,
        'de' - German,
        'fr' - French.

3. The script will detect the language of the input string and count the 
number of vowels in it based on the chosen language.

4. A histogram will be plotted, showing the distribution of vowel counts 
for the selected language.

Supported Languages and Vowels:
- English: ['a', 'e', 'i', 'o', 'u']
- Russian: ['а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
- Polish: ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y']
- German: ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü']
- French: ['a', 'e', 'i', 'o', 'u']

Note: The script uses the 'langdetect' library for language detection. Please 
make sure to install it using 'pip install langdetect' before running the 
script.

Author: ROANVL
"""

import time
import matplotlib.pyplot as plt
from langdetect import detect_langs
from typing import List, Tuple, Dict


# Function to detect the language of a given text
def detect_language(text: str) -> Tuple[str, Dict[str, float]]:
    """
    Detects the language of the given text.
    Args:
        text (str): The input text to detect the language.
    Returns:
        tuple: A tuple containing the detected language code and a dictionary of
            language probabilities. The language code represents the detected
            language, and the dictionary contains the language codes as keys and
            their corresponding probabilities as values.
    """
    results = detect_langs(text)
    languages = {}
    for result in results:
        languages[result.lang] = result.prob
    language = max(languages, key=languages.get)
    return language, {language: languages[language]}


# Function to choose the source of the input string (keyboard or file)
VALID_SOURCE_CHOICES = ['1', '2']


def choose_source() -> str:
    while True:
        source_choice = input(
            "Choose the source of the string:\n1 - keyboard input,\n2 - file input.\nYour choice: ")
        if source_choice in VALID_SOURCE_CHOICES:
            return source_choice
        else:
            print("Invalid choice. Please select 1 or 2.")


# Function to choose the language of the input string
VALID_LANGUAGE_CHOICES = ['en', 'ru', 'pl', 'de', 'fr']


def choose_language() -> str:
    while True:
        language = input(
            f"Choose the language of the input string:\nValid choices: {', '.join(VALID_LANGUAGE_CHOICES)}\nYour choice: ")
        if language in VALID_LANGUAGE_CHOICES:
            return language
        else:
            print("Invalid choice. Please select from the provided languages.")


# Function to get the user input based on the source choice
def get_user_input(source_choice: str) -> Tuple[str, str]:
    if source_choice == "1":
        while True:
            language = choose_language()
            user_input = input("Enter a string: ")
            if language and user_input:  # Check if both inputs are valid
                break
            print("Invalid input. Please try again.")
    else:
        try:
            with open('test(war and peace)_task3_1.txt', 'r') as file:
                user_input = file.read().strip()
            detected_language = detect_language(user_input)
            language = detected_language[0]
        except FileNotFoundError:
            print("File not found.")
            return None, None
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return None, None
    return language, user_input


def measure_execution_time(func):
    # Function decorator to measure the execution time of a function
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(
            f"Execution time for '{func.__name__}': {execution_time:.5f} seconds")
        return result
    return wrapper


# Function to count the number of vowels in a string
@measure_execution_time
def count_vowels(input_string: str, vowels: List[str]) -> Dict[str, int]:
    """
    Counts the number of vowels in a given string.

    Args:
        string (str): The input string.
        vowels (list): A list of vowels to count.

    Returns:
        dict: A dictionary containing the vowel counts, where the keys are the vowels and the values are the counts.
    """
    input_string_lower = input_string.lower()
    vowel_counts = {vowel: input_string_lower.count(vowel) for vowel in vowels}
    return vowel_counts


# Function to plot a histogram of vowel counts by language
def plot_histogram(vowel_counts_by_language: Dict[str, Dict[str, int]]) -> None:
    """
    Plots a histogram showing the distribution of vowel counts by language.
    Args:
        vowel_counts_by_language (dict): A dictionary containing the vowel counts for each language.
            The keys represent the language, and the values are dictionaries with vowel counts,
            where the keys are the vowels and the values are the counts.
    Returns:
        None
    """
    fig, ax = plt.subplots()

    for index, (language, vowel_counts) in enumerate(vowel_counts_by_language.items()):
        x_values = range(len(vowel_counts))
        vowel_counts_list = list(vowel_counts.values())
        labels = list(vowel_counts.keys())

        ax.bar(x_values, vowel_counts_list, align='center',
               label=language, color=plt.cm.Set3(index))

        for bar_index, (height, label) in enumerate(zip(vowel_counts_list, labels)):
            ax.text(bar_index, height + 0.02 *
                    max(vowel_counts_list), str(height), ha='center')

            if vowel_counts_list and sum(vowel_counts_list) != 0:
                percentage = (height / sum(vowel_counts_list)) * 100
                ax.text(bar_index, height / 2,
                        f"{percentage:.1f}%", ha='center', color='white')

    ax.set_xlabel('Vowel Characters')
    ax.set_ylabel('Count of Vowels')
    total_vowels = sum(vowel_counts_list)
    ax.set_title(
        f"COUNT OF VOWELS\n(text language - {''.join(language)})\ntotal number of vowels: {total_vowels}")

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.yaxis.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    ax.legend()
    plt.xticks(x_values, labels)

    if not any(vowel_counts_list) or sum(vowel_counts_list) == 0:
        print("No vowels found in the input string.")
    else:
        plt.show()


# Main program loop
while True:
    source_choice = choose_source()
    language, user_input = get_user_input(source_choice)

    if language is not None and user_input is not None:
        # Define the vowels for each supported language
        vowels_by_language = {
            'en': ['a', 'e', 'i', 'o', 'u'],
            'ru': ['а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'],
            'pl': ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y'],
            'de': ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü'],
            'fr': ['a', 'e', 'i', 'o', 'u']
        }

        # Count the number of vowels in the input string for the selected language
        vowel_counts_by_language = {}
        vowel_counts = count_vowels(user_input, vowels_by_language[language])

        vowel_counts_by_language[language] = vowel_counts

        # Plot a histogram of vowel counts by language
        plot_histogram(vowel_counts_by_language)

        # Prompt the user if they want to run the program again or exit
        while True:
            restart_choice = input(
                "Do you want to run the program again? (y/n): ").lower()
            if restart_choice in ['y', 'n']:
                break
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")

        if restart_choice == 'n':
            break  # Exit the loop if the user doesn't want to restart

# End of the program
print("Thank you for using the Vowel Counter and Language Detection script. Goodbye!")
