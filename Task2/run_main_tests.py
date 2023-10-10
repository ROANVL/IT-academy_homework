from time_formatting import convert_time_to_spoken_word
from validation import validate_time_format
from itertools import product
import time


def run_main_tests():
    """
    Test function for the main() function.

    It runs various test cases to validate the functionality of the main()
    function.
    This includes testing different scenarios, inputs, and expected outputs.

    Returns:
        None
    """
    MAX_ATTEMPTS = 3
    attempt_count = 0

    res = [f"{h:02d}:{m:02d}" for h, m in product(range(24), range(0, 60, 1))]

    for i in res[770:]:  # Необходимо изменить срез для проверки второй \
        # половины
        while attempt_count < MAX_ATTEMPTS:

            time_input = i

            if validate_time_format(time_input):
                print(convert_time_to_spoken_word(i))
            time.sleep(0.0)

            break


if __name__ == "__main__":
    run_main_tests()
