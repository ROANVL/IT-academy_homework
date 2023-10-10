import functools
import time
from datetime import datetime
from config import LOG_FILE_NAME, LOG_SEPARATOR


def get_next_log_number(file_name=LOG_FILE_NAME):
    """
    Get the next available log number based on the existing log file.

    Args:
        file_name (str, optional): The name of the log file. Defaults to
        LOG_FILE_NAME.

    Returns:
        int: The next available log number.
    """
    try:
        with open(file_name, "r") as log_file:
            lines = log_file.readlines()
            last_log_line = [
                line for line in lines if "Log Number:" in line][-1]
            log_number = int(last_log_line.split()[-1]) + 1
        return log_number
    except FileNotFoundError:
        return 1


def log_execution(file_name=LOG_FILE_NAME):
    """
    Decorator function for logging the execution details of a wrapped function.

    Args:
        file_name (str, optional): The name of the log file. Defaults to
        LOG_FILE_NAME.

    Returns:
        function: Decorator function.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            log_counter = get_next_log_number(file_name)

            start_time = time.time()
            result = func(*args)
            end_time = time.time()

            execution_time = end_time - start_time
            formatted_time = "{:.6f}".format(execution_time)
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(file_name, "a") as log_file:
                log_file.write(LOG_SEPARATOR)
                log_file.write(f"Log Number: {log_counter}\n")
                log_file.write(f"Date and Time: {current_datetime}\n")
                log_file.write(f"Function: {func.__name__}\n")
                log_file.write(f"Arguments: {args}\n")
                log_file.write(f"Return Value: {result}\n")
                log_file.write(f"Execution Time: {formatted_time} seconds\n")
                log_file.write(LOG_SEPARATOR)

            return result
        return wrapper
    return decorator
