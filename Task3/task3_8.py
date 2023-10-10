"""
Mean Calculator

This script calculates the mean value of a list of numbers provided by the user.
The user will be prompted to enter numbers separated by spaces. The script will
calculate the mean of the provided numbers and display the result.

Usage:
1. Run the script.
2. Enter a list of numbers separated by spaces when prompted.
3. The script will calculate and display the mean value of the numbers.
4. The user will then be asked if they want to continue or exit the program.

"""


def get_valid_numbers_input() -> list:
    """
    Prompt the user to enter numbers separated by spaces and validate the input.

    Returns:
    list: A list of valid numbers entered by the user.
    """
    while True:
        user_input = input("Enter numbers separated by spaces: ")
        numbers = []

        try:
            numbers = [float(num) for num in user_input.split()]
            if len(numbers) < 2:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter at least two numbers.")
            continue

        return numbers


def calculate_mean(numbers: list) -> float:
    """
    Calculate the mean value of a list of numbers.

    Args:
    numbers (list): A list of numbers.

    Returns:
    float: The mean value of the numbers.
    """
    total_sum = sum(numbers)
    count = len(numbers)
    mean = total_sum / count
    return mean


def continue_program() -> bool:
    """
    Ask the user if they want to continue or exit the program.

    Returns:
    bool: True if the user wants to continue, False if the user wants to exit.
    """
    while True:
        choice = input(
            "Do you want to continue? (Enter 'yes' or 'no'): ").lower()
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def main() -> None:
    """
    Main function to execute the mean calculator.

    The function repeatedly prompts the user to enter numbers, calculates the mean
    value, and displays the result. It then asks the user if they want to continue
    or exit the program.
    """
    while True:
        numbers = get_valid_numbers_input()

        result = calculate_mean(numbers)

        print("Mean value:", result)

        if not continue_program():
            print("Exiting the program...")
            break


if __name__ == "__main__":
    main()
