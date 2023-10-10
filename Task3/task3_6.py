"""
Vowel Remover Script

This script allows the user to remove vowels from a given input string in different languages.
The user can choose the language of the input string from a predefined set of languages, and
the script will remove the corresponding vowels based on the selected language.

Usage:
1. Run the script.
2. Enter the input string when prompted.
3. Choose the language of the input string from the provided options.
4. The script will display the input string with vowels removed.
5. Optionally, you can choose to continue and input another string.

Supported languages and their corresponding vowels:
- English (en): ['a', 'e', 'i', 'o', 'u']
- Russian (ru): ['а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
- Polish (pl): ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y']
- German (de): ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü']
- French (fr): ['a', 'e', 'i', 'o', 'u']

"""

import re

# Language-specific vowel sets
vowels = {
    'en': ['a', 'e', 'i', 'o', 'u'],
    'ru': ['а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'],
    'pl': ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y'],
    'de': ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü'],
    'fr': ['a', 'e', 'i', 'o', 'u']
}


def remove_vowels(input_string: str, vowels_set: list) -> str:
    """Remove vowels from the input string.

    Args:
        input_string (str): The input string from which vowels will be removed.
        vowels_set (list): List of vowels specific to the chosen language.

    Returns:
        str: The input string with vowels removed.
    """
    return ''.join(char for char in input_string if char.lower() not in vowels_set)


def get_valid_string_input() -> str:
    """Get a valid input string from the user.

    Returns:
        str: The valid input string.
    """
    while True:
        user_input = input("Enter a string: ")

        # Use regex to check if the input contains any characters (including symbols and spaces)
        if re.match(r'^[^\n]+$', user_input):
            return user_input
        else:
            print("Invalid input. Please enter a valid string.")


def choose_language() -> str:
    """Prompt the user to choose the language of the input string.

    Returns:
        str: The selected language code ('en', 'ru', 'pl', 'de', or 'fr').
    """
    while True:
        language_choice = input(
            "Choose the language of the input string:\n'en' - English,\n'ru' - Russian,\n"
            "'pl' - Polish,\n'de' - German,\n'fr' - French.\nYour choice: ").lower()
        try:
            if language_choice in ['en', 'ru', 'pl', 'de', 'fr']:
                return language_choice
            else:
                raise ValueError(
                    "Invalid choice. Please select from the provided languages.")
        except ValueError as err:
            print(err)


def get_continue_choice() -> str:
    """Prompt the user to choose whether to continue or exit the program.

    Returns:
        str: The user's choice ('yes' or 'no').
    """
    while True:
        continue_choice = input("Do you want to continue? (yes/no): ").lower()
        if continue_choice in ["yes", "no"]:
            return continue_choice
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def main() -> None:
    """Main function to execute the vowel remover script."""
    while True:
        try:
            selected_language = choose_language()
        except KeyboardInterrupt:
            print("\nExiting the program due to user interruption.")
            break

        user_input_string = get_valid_string_input()

        result = remove_vowels(
            user_input_string, vowels.get(selected_language, []))
        print("String without vowels:", result)

        continue_choice = get_continue_choice()
        if continue_choice == "no":
            print("Exiting the program. Goodbye!")
            break


if __name__ == "__main__":
    main()
