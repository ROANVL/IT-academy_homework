import time
import user_interface as ui
from time_formatting import convert_time_to_spoken_word as time2spoken
from validation import validate_time_format


def main():
    """
    The main function that runs the time conversion program.

    It presents a menu to the user and performs corresponding actions
    based on the user's choice. The program allows the user to display
    the current time, enter a time manually, or exit the program.
    The program includes error handling for invalid time input and limits
    the number of attempts.

    Returns:
        None
    """
    MAX_ATTEMPTS = 3
    attempt_count = 0

    is_instruction_printed = False  # Flag to track instruction printing

    while attempt_count < MAX_ATTEMPTS:
        ui.clear_screen()
        ui.print_header()

        if not is_instruction_printed:
            ui.print_instruction()
            is_instruction_printed = True

        ui.print_menu()

        user_choice = input("Please enter your choice (1, 2, or 3): ")
        while user_choice not in ["1", "2", "3"]:
            ui.clear_screen()
            ui.print_header()
            ui.print_instruction()
            ui.print_menu()
            print("Invalid choice. Please enter 1, 2, or 3.")
            user_choice = input("Please enter your choice (1, 2, or 3): ")
        ui.print_separator()

        # Handle user's choice
        match user_choice:
            case "1":
                ui.clear_screen()
                ui.print_header()
                print(f'Current time - {time2spoken()}')
                ui.print_separator()

                repeat = ui.ask_to_continue()

                match repeat:
                    case "yes":
                        continue
                    case "no":
                        ui.clear_screen()
                        ui.print_header()
                        ui.print_footer()
                        return
                    case "fail":
                        ui.clear_screen()
                        ui.print_header()
                        ui.print_max_attempts_message()
                        ui.print_footer()
                        return

            case "2":
                ui.clear_screen()
                ui.print_header()
                attempt_count = 0

                while attempt_count < MAX_ATTEMPTS:
                    ui.clear_screen()
                    ui.print_header()
                    time_input = input(
                        "Please enter the time in HH:MM format\n"
                        "(24-hour format): ")
                    ui.print_separator()

                    if validate_time_format(time_input):
                        print(time2spoken(time_input))
                        ui.print_separator()

                        repeat = ui.ask_to_continue()

                        match repeat:
                            case "yes":
                                attempt_count = 0
                            case "no":
                                break
                            case "fail":
                                ui.print_max_attempts_message()
                                ui.print_footer()
                                return

                    else:
                        ui.display_invalid_time_error()
                        time.sleep(1)
                        attempt_count += 1

            case "3":
                ui.clear_screen()
                ui.print_header()
                ui.print_footer()
                return

        if attempt_count == MAX_ATTEMPTS:
            ui.print_max_attempts_message()

    ui.print_footer()


if __name__ == "__main__":
    main()
