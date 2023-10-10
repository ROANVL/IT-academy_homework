def kph_to_mps(speed):
    return round(speed * 1000 / 3600, 2)


def validate_speed_input(speed):
    try:
        speed = float(speed)
        if speed < 0:
            return False
        else:
            return True
    except ValueError:
        return False


def main():
    print("-----------------------------------------------")
    print("Kilometers per Hour to Meters per Second Converter")
    print("-----------------------------------------------")

    while True:
        speed = input("Enter the speed in kilometers per hour: ")

        if validate_speed_input(speed):
            speed = float(speed)
            converted_speed = kph_to_mps(speed)
            print("The speed in meters per second is:", converted_speed)
        else:
            print("Invalid speed value. Please enter a non-negative number.")
            continue

        choice = input("Do you want to convert another speed?"
                       " (Yes/No): ").lower()

        while choice not in ["yes", "no"]:
            choice = input("Invalid choice. Please enter Yes or No: ").lower()

        if choice == "no":
            print("Thank you for using the Kilometers per Hour to Meters per"
                  " Second Converter. Goodbye!")
            break


if __name__ == "__main__":
    main()
