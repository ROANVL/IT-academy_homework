import time


def validate_temperature_input(temperature):
    try:
        float(temperature)
        return True
    except ValueError:
        return False


def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.015)
    print()
