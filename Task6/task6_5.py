import timeit
from typing import Dict


def fibonacci_memoization(n: int, memo: Dict[int, int] = {}) -> int:
    """
    Compute the Nth number in the Fibonacci sequence using memoization.
    Parameters:
        n (int): The position of the Fibonacci number to compute (0-based index).
        memo (Dict[int, int], optional): A dictionary to store previously computed Fibonacci numbers.
            Defaults to an empty dictionary.
    Returns:
        int: The Nth Fibonacci number.
    Raises:
        ValueError: If the input value N is not a non-negative integer.
    """
    if n < 0:
        raise ValueError("Invalid input. N should be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci_memoization(
            n - 1, memo) + fibonacci_memoization(n - 2, memo)

        # Print memo contents before returning the result
        print(f"Memo contents at N={n}: {memo}")

        return memo[n]


def main():
    """
    Interactive function to compute Fibonacci numbers using memoization.
    """
    while True:
        try:
            n = int(input(
                "Enter the position of the Fibonacci number to find\n(or -1 to exit): "))
            if n == -1:
                print("Exiting the program.")
                break

            start_time = timeit.default_timer()
            # Subtract 1 to get the correct index
            result = fibonacci_memoization(n - 1)
            end_time = timeit.default_timer()
            execution_time = end_time - start_time

            print(
                f"{'-' * 50}\nThe {n}th number in the Fibonacci sequence is: {result}")
            print('-' * 50)
            print(f"Execution time: {execution_time:.8f} seconds\n")
        except ValueError:
            print("Error: Please enter a non-negative integer.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
