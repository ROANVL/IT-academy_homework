import random


def generate_random_number(left, right):
    """
    Generates a random number within the specified range [left, right].

    Parameters:
    - left: the left border of the range
    - right: the right border of the range

    Returns:
    - A random number within the specified range.
    """
    random_number = random.SystemRandom().randint(left, right)
    return random_number


def validate_input(value):
    """
    Validates the user input to ensure it is a valid number.

    Parameters:
    - value: the user input value

    Returns:
    - True if the value is a number, False otherwise.
    """
    return value.replace(".", "").isdigit()


def main():
    print("----------------------------------")
    print("Program to Generate a Random Number")
    print("----------------------------------")

    while True:
        left = input("Enter the left border of the range: ")
        if not validate_input(left):
            print("Invalid input. The left border should be a numeric value.")
            continue

        right = input("Enter the right border of the range: ")
        if not validate_input(right):
            print("Invalid input. The right border should be a numeric value.")
            continue

        left = float(left)
        right = float(right)

        if left >= right:
            print("Invalid range. The left border should be smaller "
                  "than the right border.")
            continue

        random_number = generate_random_number(left, right)
        print("Random number:", random_number)

        choice = input("Do you want to generate another random number? "
                       "(Yes/No): ").lower()

        while choice not in ["yes", "no"]:
            choice = input("Invalid choice. Please enter Yes or No: ").lower()

        if choice == "no":
            print("Thank you for using the program. Goodbye!")
            break


if __name__ == "__main__":
    main()
