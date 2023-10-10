import timeit
from functools import lru_cache
from typing import Union


@lru_cache(maxsize=128)
def power(base: Union[int, float], exponent: int) -> Union[int, float]:
    """
    Calculate the power of a number using fast exponentiation (recursive).

    Args:
        base (int or float): The base number.
        exponent (int): The exponent value.

    Returns:
        int or float: The result of raising the base to the power of the
        exponent.
    """
    if not isinstance(base, (int, float)):
        raise TypeError('Base must be an integer or a float.')
    if not isinstance(exponent, int):
        raise TypeError('Exponent must be an integer.')

    if base == 0 and exponent < 0:

        return float('inf')

    match (base, exponent):
        case (0, 0):
            return 1
        case (base, 0):
            return 1
        case (base, exponent) if exponent < 0:
            return 1 / power(base, -exponent)
        case (base, exponent) if exponent % 2 == 0:
            half_power = power(base, exponent // 2)
            return half_power * half_power
        case (base, exponent):
            return base * power(base, exponent - 1)


base_numbers = [2, 2, 3, 3, 2, 2, 4, 4, 5,
                5, 6, 6, 5, 5, -2, -2, -3, -3, 0, 0, 0, -1, 0]
exponent_values = [3, 3, 5, 5, 2, 2, 4, 4,
                   6, 6, 7, 7, 5, 5, 2, 2, -3, -3, 1, 1, 0, 0, -1]

# Perform the power calculations for each base-exponent pair and measure time
# taken
for base_number, exponent_value in zip(base_numbers, exponent_values):
    # Check if the result is already in cache
    cache_misses_before = power.cache_info().misses
    start_time = timeit.default_timer()
    result = power(base_number, exponent_value)
    end_time = timeit.default_timer()
    cache_misses_after = power.cache_info().misses

    if cache_misses_after > cache_misses_before:
        print(f"{base_number}^{exponent_value} = {result} (New calculation)")
        print(f"Time taken: {end_time - start_time:.8f} seconds")
    else:
        print(
            f"{base_number}^{exponent_value} = {result} "
            f"(Result retrieved from cache)")
        print(
            f"Time taken to retrieve from cache: {end_time - start_time:.8f} "
            f"seconds")
    print('-' * 50)
