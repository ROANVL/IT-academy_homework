import random
import time
from progressbar import MyProgressBar
import config as cfg
from logger import log_execution

# Function to add two numbers and a random integer within specified range


@log_execution()
def add(a, b):
    """
    Add two numbers and return the result along with a random integer.

    Args:
        a (int): First operand.
        b (int): Second operand.

    Returns:
        int: Sum of a, b, and a random integer.
    """
    time.sleep(cfg.SLEEP_ADD)
    return a + b

# Function to multiply two numbers and a random integer within specified range


@log_execution()
def multiply(x, y):
    """
    Multiply two numbers and return the result multiplied by a random integer.

    Args:
        x (int): First operand.
        y (int): Second operand.

    Returns:
        int: Product of x, y, and a random integer.
    """
    time.sleep(cfg.SLEEP_MULTIPLY)
    return x * y
# Function to subtract two numbers


@log_execution()
def subtract(a, b):
    """
    Subtract b from a and return the result.

    Args:
        a (int): First operand.
        b (int): Second operand.

    Returns:
        int: Difference between a and b.
    """
    time.sleep(cfg.SLEEP_SUBTRACT)
    return a - b


if __name__ == "__main__":
    # Initialize a progress bar
    progress_bar = MyProgressBar(
        cfg.NUM_FUNCTION_CALLS * cfg.ITERATIONS_PER_CALL,
        message="Processing:", width=40
    )

    total_records = cfg.NUM_FUNCTION_CALLS * cfg.ITERATIONS_PER_CALL
    completed_records = 0

    # Iterate through function calls
    for _ in range(cfg.NUM_FUNCTION_CALLS):
        # Generate random operands for each function
        operand1_add = random.randint(cfg.RAND_INT_MIN, cfg.RAND_INT_MAX_ADD)
        operand2_add = random.randint(cfg.RAND_INT_MIN, cfg.RAND_INT_MAX_ADD)

        operand1_multiply = random.randint(
            cfg.RAND_INT_MIN, cfg.RAND_INT_MAX_MULTIPLY)
        operand2_multiply = random.randint(
            cfg.RAND_INT_MIN, cfg.RAND_INT_MAX_MULTIPLY)

        operand1_subtract = random.randint(
            cfg.RAND_INT_MIN, cfg.RAND_INT_MAX_SUBTRACT)
        operand2_subtract = random.randint(
            cfg.RAND_INT_MIN, cfg.RAND_INT_MAX_SUBTRACT)

        # Perform function calls and update progress
        result1 = add(operand1_add, operand2_add)
        progress_bar.update()

        result2 = multiply(operand1_multiply, operand2_multiply)
        progress_bar.update()

        result3 = subtract(operand1_subtract, operand2_subtract)
        progress_bar.update()

        completed_records += cfg.ITERATIONS_PER_CALL

    # Finish the progress bar
    progress_bar.finish()

    # Print summary information
    print("Program completed successfully.")
    print(f"Execution logs are written to the file: {cfg.LOG_FILE_NAME}")
    print(f"Total records: {total_records}")
    print(f"Completed records: {completed_records}")

    # Display the details of the last log entry
    try:
        with open(cfg.LOG_FILE_NAME, "r") as log_file:
            lines = log_file.readlines()
            # Extract last 9 lines (details of the last log entry)
            last_log_details = lines[-9:]
            print("\nLast Log Entry:")
            for line in last_log_details:
                print(line.strip())
    except FileNotFoundError:
        print("No logs found.")
