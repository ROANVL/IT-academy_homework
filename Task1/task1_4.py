from bs4 import BeautifulSoup
import requests
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP


def get_usd_to_byn_rate():
    # replace with the URL of the currency rate page
    url = "https://myfin.by/currency/usd"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    rate_element = soup.find("span", class_="accent")
    rate = rate_element.text
    return Decimal(rate)


def validate_amount_input(amount):
    try:
        amount = Decimal(amount)
        if amount <= 0:
            return False
        else:
            return True
    except ValueError:
        return False


def main():
    print("=============================")
    print("USD to BYN Conversion Program")
    print("=============================")

    usd_to_byn_rate = get_usd_to_byn_rate()
    print(
          f"Best USD to BYN rate as of {datetime.now().strftime('%Y-%m-%d')}: "
          f"{usd_to_byn_rate} (according to myfin.by)"
         )

    while True:
        amount_usd = input("Enter the amount in USD: ")

        if not amount_usd.replace(".", "").isdigit():
            print("Invalid amount. Please enter a positive number.")
            continue

        if validate_amount_input(amount_usd):
            amount_usd = Decimal(amount_usd)
            amount_byn = amount_usd * usd_to_byn_rate
            rounded_amount_byn = amount_byn.quantize(
                Decimal("0.00"), rounding=ROUND_HALF_UP
            )
            print(f"Amount in BYN: {rounded_amount_byn}")
        else:
            print("Invalid amount. Please enter a positive number.")
            continue

        choice = input("Do you want to continue the conversion?"
                       " (Yes/No): ").lower()

        while choice not in ["yes", "no"]:
            choice = input("Invalid choice. Please enter Yes or No: ").lower()

        if choice == "no":
            print("Thank you for using the USD to BYN Conversion Program."
                  " Goodbye!")
            break


if __name__ == "__main__":
    main()
