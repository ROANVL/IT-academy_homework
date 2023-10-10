import re


def validate_time_format(time_input):
    """
    Validates the correctness of the time input format.

    Arguments:
    - time_input (str): Time in the format "hh:mm".

    Returns:
    - bool: True if the time input format is correct, False otherwise.
    """
    pattern = r'^\d{2}:\d{2}$'
    if re.match(pattern, time_input):
        hour, minute = map(int, time_input.split(':'))
        return all((0 <= hour <= 23, 0 <= minute <= 59))
    return False
