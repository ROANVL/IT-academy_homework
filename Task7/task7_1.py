class DivisionByZeroError(Exception):
    """
    Custom exception for division by zero.

    Attributes:
        division_info (str): Information about the division causing the
        exception.
    """

    def __init__(self, division_info):
        """
        Initialize the exception with a provided message.

        Args:
            division_info (str): Information about the division causing the
            exception.
        """
        super().__init__(f"Division by zero is not allowed: {division_info}")


def perform_division(numerator, denominator, division_info):
    """
    Divides two numbers and handles errors.

    Args:
        numerator (float): The numerator for division.
        denominator (float): The denominator for division.
        division_info (str): Information about the division for error handling.

    Returns:
        float: The result of the division.

    Raises:
        DivisionByZeroError: If the denominator is zero.
    """
    if denominator == 0:
        raise DivisionByZeroError(division_info)
    return numerator / denominator


def get_numeric_input(prompt):
    """
    Gets numeric input from the user.

    Args:
        prompt (str): The prompt message for input.

    Returns:
        float: The numeric input from the user.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    """
    Main function to perform division and handle errors.
    """
    try:
        numerator = get_numeric_input("Enter the numerator: ")
        denominator = get_numeric_input("Enter the denominator: ")

        division_info = f"Numerator: {numerator}, Denominator: {denominator}"
        result = perform_division(numerator, denominator, division_info)
        print(f"Result: {result:.2f}")

    except DivisionByZeroError as dbze:
        print(f"Error: {dbze}")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
