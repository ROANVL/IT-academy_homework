"""
This script allows the user to enter a string of words, swaps the case of the letters in the words,
and then displays the resulting swapped string. The script provides a simple text-based interface
to interact with the user.

Usage:
1. Run the script.
2. Enter a string containing words only when prompted.
3. The script will swap the case of letters in each word of the input string.
4. The swapped string will be displayed.
5. The script will then ask if you want to continue.
6. If you enter 'yes', the process will repeat from step 2.
7. If you enter 'no', the script will terminate.
8. The script handles invalid inputs and keyboard interrupts gracefully.

Note:
- The script considers a word to be a sequence of alphabetic characters without spaces.
- If you enter a string with digits, special characters, or spaces within words,
  it will be considered invalid, and you will be asked to enter a new string.

Enjoy swapping the case of your words with this simple script!
"""


def is_valid_word_input(input_str: str) -> bool:
    words = input_str.split()
    return all(word.isalpha() for word in words)


def get_valid_word_input() -> str:
    while True:
        try:
            user_input = input("Enter a string of words: ")
            if is_valid_word_input(user_input):
                return user_input
            else:
                print("Invalid input. Please enter only words.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            exit(0)


def swap_case(input_str: str) -> str:
    return input_str.swapcase()


def get_continue_choice() -> bool:
    while True:
        try:
            choice = input("Do you want to continue? (yes/no): ").lower()
            if choice == "yes":
                return True
            elif choice == "no":
                return False
            else:
                raise ValueError
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            exit(0)
        except ValueError:
            print("Please enter 'yes' or 'no.'")


def main() -> None:
    while True:
        user_input = get_valid_word_input()
        swapped_string = swap_case(user_input)
        print("Swapped string:", swapped_string)

        if not get_continue_choice():
            break


if __name__ == "__main__":
    main()
