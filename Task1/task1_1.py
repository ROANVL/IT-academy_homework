import temp_converter
from utilities import print_slow as ps
from utilities import validate_temperature_input as vti


def main():
    ps("==============================================")
    ps("Welcome to the Temperature Conversion Program!")
    ps("==============================================")
    ps("Instructions:")
    ps("- Choose the temperature type: C - Celsius, F - Fahrenheit.")
    ps("- Enter the temperature value when prompted.")
    ps("- The program will convert the temperature and "
       "display the result.")
    ps("- You can choose to continue or exit after each conversion.")
    ps("============================================================")

    while True:
        option = input("Please select the temperature type "
                       "(C - Celsius, F - Fahrenheit): ")

        if option.upper() == "C":
            while True:
                celsius = input("Enter the temperature in Celsius: ")
                if vti(celsius):
                    break
                else:
                    print("Invalid temperature value. "
                          "Please enter a valid number.")

            celsius = float(celsius)
            fahrenheit = temp_converter.celsius_to_fahrenheit(celsius)
            print("The temperature in Fahrenheit is:", round(fahrenheit, 2))
            print()

        elif option.upper() == "F":
            while True:
                fahrenheit = input("Enter the temperature in Fahrenheit: ")
                if vti(fahrenheit):
                    break
                else:
                    print("Invalid temperature value. "
                          "Please enter a valid number.")

            fahrenheit = float(fahrenheit)
            celsius = temp_converter.fahrenheit_to_celsius(fahrenheit)
            print("The temperature in Celsius is:", round(celsius, 2))
            print()

        else:
            print("Invalid temperature type. Please choose C for Celsius "
                  "or F for Fahrenheit.")
            continue

        while True:
            choice = input("Do you want to continue with another conversion?"
                           " (Yes/No): ").lower()
            if choice == "yes" or choice == "no":
                break
            else:
                print("Invalid choice. Please enter Yes or No.")

        if choice == "no":
            ps("Thank you for using the Temperature Conversion "
               "Program. Goodbye!")
            break


if __name__ == "__main__":
    main()
