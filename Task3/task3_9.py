"""
Reversing String Program

This script allows the user to enter a string containing words only, then it reverses the input string and prints the reversed version.

Usage:
1. Run the script.
2. Enter a string containing words only when prompted.
3. The program will reverse the input string and display the result.
4. The program will then ask if you want to continue.
5. Enter 'yes' to repeat the process or 'no' to exit.

Note:
- The input should contain at least one word with alphabetic characters.
- Punctuation marks and numbers will be ignored during the reversal.
- Press 'Ctrl+C' to terminate the program at any time.

"""


def contains_only_words(input_str: str) -> bool:
    words = input_str.split()
    return all(any(char.isalpha() for char in word) for word in words)


def get_valid_input() -> str:
    while True:
        try:
            user_input = input("Enter a string containing words: ")
            if contains_only_words(user_input):
                return user_input
            else:
                print("Invalid input. Please enter a string with words only.")
        except KeyboardInterrupt:
            print("\nProgram terminated by the user.")
            exit(0)


def reverse_string(input_str: str) -> str:
    return input_str[::-1]


def prompt_continue() -> bool:
    while True:
        try:
            choice = input("Do you want to continue? (yes/no): ").lower()
            if choice in ["yes", "no"]:
                return choice == "yes"
            else:
                print("Please enter either 'yes' or 'no'.")
        except KeyboardInterrupt:
            print("\nProgram terminated by the user.")
            exit(0)


def main() -> None:
    while True:
        user_input = get_valid_input()
        reversed_str = reverse_string(user_input)
        print("Reversed string:", reversed_str)

        if not prompt_continue():
            print("Exiting the program.")
            break


if __name__ == "__main__":
    main()
