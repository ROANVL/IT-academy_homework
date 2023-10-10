"""
Prime Number Finder

This script allows the user to find the largest prime number from a list of numbers. It offers three main options:
1. Enter numbers manually: The user can input numbers directly to create a list.
2. Generate an ordered or random list: The user can generate a list of numbers in a specific range, either ordered or random.
3. Create a generator: The user can generate numbers in descending order using a generator.

Miller-Rabin Primality Test is used to efficiently check if a number is prime.

How to Use:
1. Run the script, and it will present the user with three main options.
2. Choose an option by entering the corresponding number (1, 2, or 3).
3. Depending on the option, the script will prompt you to enter the numbers or range of numbers.
4. The script will find the largest prime number in the list and display the result.
5. After each iteration, the script will ask if you want to continue or exit.

Note:
- The Miller-Rabin primality test used in this script is probabilistic, but the probability of false positives decreases with a higher number of iterations (k).
- The script provides execution time for each operation, allowing you to gauge the efficiency of finding the largest prime.

For educational and demonstration purposes only.

Author: ROANVL
"""

import random
import time
from typing import List, Union, Generator


# Constant for user interface options - first set of options
UI_OPTIONS = {
    "1": "Enter numbers manually",
    "2": "Generate an ordered or random list",
    "3": "Create a generator"
}

# Constant for user interface options - second set of options
CONTINUE_OPTIONS = {
    "yes": "Yes",
    "no": "No"
}

OPTION_MANUAL = "1"
OPTION_RANDOM_LIST = "2"
OPTION_GENERATOR = "3"

# Function to perform the Miller-Rabin primality test


def miller_rabin_primality_test(n: int, k: int = 5) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False

    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        if not check(a, s, d, n):
            return False
    return True


# User Interface
# Function to get the user's choice from the UI_OPTIONS
def get_user_choice() -> str:
    while True:
        print("Choose one of the following options:")
        for key, value in UI_OPTIONS.items():
            print(f"{key}. {value}")

        choice = input("Enter your choice (1, 2, or 3): ").strip()

        try:
            if choice in [OPTION_MANUAL, OPTION_RANDOM_LIST, OPTION_GENERATOR]:
                return choice
            else:
                raise ValueError()
        except ValueError:
            print("Invalid choice. Please enter 1, 2, or 3.")


# Process user's choice
def process_choice(choice: str) -> Union[List[int], None]:
    if choice == OPTION_MANUAL:
        numbers_list = get_manual_numbers_list()
    elif choice == OPTION_RANDOM_LIST:
        sub_choice = input(
            "Enter 1 for an ordered list or 2 for a random list: ").strip()
        if sub_choice == "1":
            upper_limit = get_generator_upper_limit()
            numbers_list = generate_ordered_list(upper_limit)
        elif sub_choice == "2":
            list_length = get_random_list_length()
            upper_limit = list_length
            numbers_list = generate_random_list(upper_limit, list_length)
        else:
            print("Invalid choice. Please enter 1 or 2.")
            return None
    elif choice == OPTION_GENERATOR:
        upper_limit = get_generator_upper_limit()
        numbers_list = generate_numbers(upper_limit)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return None

    return numbers_list


# Ask if the user wants to continue
def continue_program() -> str:
    while True:
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice in CONTINUE_OPTIONS:
            return choice
        else:
            print("Please enter 'yes' or 'no'.")


# Function to manually input numbers from the user
def get_manual_numbers_list() -> List[int]:
    while True:
        user_input = input(
            "Enter numbers separated by spaces or a list (e.g. [1, 2, 3]): ")
        numbers_list = []
        try:
            if "[" in user_input and "]" in user_input:
                numbers_list = [int(num)
                                for num in user_input[1:-1].split(",")]
            else:
                numbers_list = [int(num) for num in user_input.split()]
        except ValueError:
            print("Invalid input. Please enter only numbers or a valid list.")
            continue
        return sorted(numbers_list)

# Function to generate an ordered list from 1 to the specified upper limit


def generate_ordered_list(upper_limit: int) -> List[int]:
    return list(range(1, upper_limit + 1))


# Validation functions
def get_random_list_length() -> int:
    while True:
        list_length_input = input("Enter the length of the random list: ")
        try:
            list_length = int(list_length_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if list_length <= 0:
            print("Invalid input. Please enter a positive integer.")
            continue

        return list_length


def get_generator_upper_limit() -> int:
    while True:
        upper_limit_input = input(
            "Enter the upper limit for generating numbers: ")
        try:
            # Use eval to evaluate scientific notation and obtain the actual value
            upper_limit = eval(upper_limit_input)
            if not isinstance(upper_limit, int) or upper_limit <= 0:
                raise ValueError()
        except (ValueError, SyntaxError):
            print(
                "Invalid input. Please enter a positive integer or valid scientific notation (e.g., 1*10**20).")
            continue

        return upper_limit

# Function to generate a random list of specified length with numbers from 1 to the upper limit


def generate_random_list(upper_limit: int, list_length: int) -> List[int]:
    random_list = [random.randint(1, upper_limit) for _ in range(list_length)]
    return list(set(random_list))


# Function to generate a list of numbers in descending order
def generate_numbers(upper_limit: int) -> Generator[int, None, None]:
    num = upper_limit
    while num >= 1:
        yield num
        num -= 1


# Decorator to measure execution time of functions
def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Execution time: {:.6f} seconds".format(execution_time))
        return result
    return wrapper


# Function to find the largest prime number in the list
@measure_execution_time
def get_largest_prime(numbers_list: Union[List[int], range, Generator[int, None, None]]) -> Union[int, None]:
    largest_prime = None

    if isinstance(numbers_list, list):
        for num in reversed(numbers_list):
            if miller_rabin_primality_test(num):
                largest_prime = num
                break
    elif isinstance(numbers_list, range):
        for num in numbers_list:
            if miller_rabin_primality_test(num):
                largest_prime = num
                break
    else:
        for num in numbers_list:
            if miller_rabin_primality_test(num):
                largest_prime = num
                break

    return largest_prime


# Main function to run the program
def main() -> None:
    while True:
        choice = get_user_choice()
        numbers_list = process_choice(choice)

        if numbers_list is None:
            # Terminate the program if an invalid choice is made or user chooses to exit.
            print("Exiting the program.")
            break

        print("Your list:", numbers_list)

        largest_prime = get_largest_prime(numbers_list)
        if largest_prime is not None:
            print("The largest prime number in the list:", largest_prime)
        else:
            print("No prime numbers found in the list.")

        choice = continue_program()
        if choice == "no":
            print("Exiting the program.")
            break


if __name__ == "__main__":
    main()
