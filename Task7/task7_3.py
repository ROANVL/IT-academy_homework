class InvalidInputType(Exception):
    def __init__(self):
        super().__init__("Invalid input type")


class InvalidElementType(Exception):
    def __init__(self):
        super().__init__("Invalid element type in the list")


def validate_input_type(value, expected_type, error_type):
    if not isinstance(value, expected_type):
        raise error_type


def validate_element_type(element, expected_type, error_type):
    if not isinstance(element, expected_type):
        raise error_type


def sum_even_numbers(input_list):
    try:
        validate_input_type(input_list, list, InvalidInputType)
        even_sum = 0
        for num in input_list:
            validate_element_type(num, int, InvalidElementType)
            if num % 2 == 0:
                even_sum += num
        return even_sum
    except (InvalidInputType, InvalidElementType) as e:
        return str(e)


# Example usage of the function
def main():
    numbers = [1, 2, 3, 4, 5, 6, 8, 10]
    result = sum_even_numbers(numbers)
    print(result)

    non_integer_list = [2, 4, '6', 8, 10]
    result = sum_even_numbers(non_integer_list)
    print(result)


if __name__ == "__main__":
    main()
