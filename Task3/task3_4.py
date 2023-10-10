"""
This script allows you to find the n-th largest number from a list of numeric values.

Usage:
1. Run the script.
2. Enter a list of numeric values separated by spaces or in the format [1, 2, 3].
3. Enter the position (index) of the largest number from the end (1 to length of the list).
4. The script will find the n-th largest number from the list and display the result.
5. You can choose to continue or exit after each calculation.

"""
from typing import List, Optional

import ast


def get_nth_largest_number(numbers: List[float], n: int) -> Optional[float]:
    """
    Returns the n-th largest number from the list.

    Args:
        numbers (list): A list of numeric values.
        n (int): The position of the largest number from the end (1-based index).

    Returns:
        float or None: The n-th largest number from the list or None if it doesn't exist.
    """
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("The list should contain only numeric values.")

    if len(numbers) < n:
        return None

    unique_numbers = sorted(set(numbers), reverse=True)
    if n > len(unique_numbers):
        return None

    return unique_numbers[n - 1]


def user_input_to_list(user_input: str) -> List[float]:
    """
    Converts user input string to a list of numeric values.

    Args:
        user_input (str): User input string containing numbers.

    Returns:
        list: A list of numeric values.
    """
    try:
        numbers_list = ast.literal_eval(user_input)
        if not isinstance(numbers_list, list):
            numbers_list = [numbers_list]
    except (ValueError, SyntaxError):
        numbers_list = [float(num) for num in user_input.split()]
    return numbers_list


def get_valid_numbers_list_input() -> List[float]:
    """
    Prompts the user to enter a list of numbers and validates the input.

    Returns:
        list: A list of numeric values with more than one element.
    """
    while True:
        user_input = input("Enter numbers separated by spaces: ")
        try:
            numbers_list = user_input_to_list(user_input)
            if len(numbers_list) < 2:
                print("The list should contain more than one number.")
            else:
                return numbers_list
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter numbers in the correct format.")


def get_valid_index_from_user(numbers_list: List[float]) -> int:
    """
    Prompts the user to enter the index (position) of the largest number from the end.

    Args:
        numbers_list (list): A list of numeric values.

    Returns:
        int: The valid index (position) of the largest number from the end.
    """
    valid_index = None
    while not valid_index:
        try:
            valid_index = int(input(
                f"Enter the position of the largest number from the end (1-{len(numbers_list)}): "))
            if valid_index < 1 or valid_index > len(numbers_list):
                raise ValueError
        except ValueError:
            print(
                f"Invalid position. Please enter a number from 1 to {len(numbers_list)}.")
    return valid_index


def ask_for_continue() -> bool:
    """
    Asks the user whether to continue or exit the program.

    Returns:
        bool: True if the user chooses to continue, False if the user chooses to exit.
    """
    while True:
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice == "yes":
            return True
        elif choice == "no":
            print("Exiting the program. Goodbye!")
            return False
        else:
            print("Invalid choice. Please enter only 'yes' or 'no'.")


def display_result(valid_index: int, result: Optional[float]) -> None:
    """
    Displays the result of finding the n-th largest number.

    Args:
        valid_index (int): The index (position) of the largest number from the end.
        result (float or None): The n-th largest number from the list, or None if it doesn't exist.
    """
    if result is not None:
        print(
            f"The {valid_index}-th largest number from the end in the list:", result)
    else:
        print("The list does not have enough elements.")


def main() -> None:
    """
    Main function to run the script. Asks the user for input, finds the n-th largest number,
    displays the result, and allows the user to continue or exit.
    """
    while True:
        try:
            numbers_list = get_valid_numbers_list_input()
            valid_index = get_valid_index_from_user(numbers_list)

            result = get_nth_largest_number(numbers_list, valid_index)

            display_result(valid_index, result)

        except ValueError as e:
            print(f"Error: {e}")

        if not ask_for_continue():
            break


if __name__ == "__main__":
    main()
