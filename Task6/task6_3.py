def count_occurrences(string, char):
    """
    Recursively counts the number of occurrences of a given character in a string.

    Args:
        string (str): The input string in which to count occurrences.
        char (str): The character to count occurrences of.

    Returns:
        int: The number of occurrences of the given character in the string.
    """
    if len(string) == 0:
        return 0
    count = 1 if string[0] == char else 0
    return count + count_occurrences(string[1:], char)


def get_user_input():
    input_string = input("Enter the string: ")
    target_char = input("Enter the character to count occurrences of: ")

    if not input_string:
        print("The string cannot be empty. Please try again.")
        return get_user_input()

    if len(target_char) != 1:
        print("Please enter a single character. Please try again.")
        return get_user_input()

    return input_string, target_char


def main():
    print("Welcome to the Occurrence Counter!")
    input_string, target_char = get_user_input()

    result = count_occurrences(input_string, target_char)

    print(f"Counting the occurrences of '{target_char}' in the string:")
    print(f"String: '{input_string}'")
    print(
        f"The character '{target_char}' occurs {result} times in the string.")


if __name__ == "__main__":
    main()
