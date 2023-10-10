"""
Even Sum Calculator

This script allows the user to input a list of numbers separated by spaces.
It calculates the sum of all even numbers in the list and displays the result.

Usage:
1. Run the script.
2. Enter a list of numbers separated by spaces.
3. The script will calculate the sum of all even numbers in the list.
4. If the user wants to continue, they can enter 'yes' when prompted.
5. To exit the program, enter 'no' when prompted or type 'exit' during number input.

The program ensures that at least two numbers are entered before calculating the sum.
"""

from typing import List


# Function to get a list of numbers from the user
def get_numbers_from_user() -> List[int]:
    """
    Asks the user to input a list of numbers separated by spaces.

    Returns:
        list: A list of integer numbers entered by the user.
              Returns None if the user inputs 'exit'.
    """
    while True:
        try:
            user_input = input(
                "Enter numbers separated by spaces (type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                return None

            numbers_list = [int(num) for num in user_input.split()]
            if len(numbers_list) < 2:
                print("Please enter at least two numbers.")
            else:
                return numbers_list
        except ValueError:
            print("Input error. Please enter only integer numbers separated by spaces.")

# Function to calculate the sum of all even numbers in the list


def get_even_sum(numbers: List[int]) -> int:
    """
    Calculates the sum of all even numbers in the given list.

    Args:
        numbers (list): A list of integer numbers.

    Returns:
        int: The sum of all even numbers in the list.
    """
    even_sum = sum(num for num in numbers if num % 2 == 0)
    return even_sum

# Function to display the result


def display_result(result: int) -> None:
    """
    Displays the result of the even sum calculation.

    Args:
        result (int): The sum of all even numbers.

    Returns:
        None
    """
    if result == 0:
        print("There are no even numbers in the list.")
    else:
        print("Sum of all even numbers in the list:", result)

# Main function to control the program


def main() -> None:
    """
    Main function to handle user input and display the result.
    """
    while True:
        try:
            numbers_list = get_numbers_from_user()

            if numbers_list is None:
                break

            if not numbers_list:
                print("Invalid input. Please try again.")
                continue

            result = get_even_sum(numbers_list)
            display_result(result)

            while True:
                choice = input("Do you want to continue? (yes/no): ").lower()
                if choice == "yes" or choice == "no":
                    break
                else:
                    print("Please enter only 'yes' or 'no'.")

            if choice != "yes":
                break

        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break


if __name__ == "__main__":
    main()
