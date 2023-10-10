"""
Library System

This script provides a command-line interface for efficiently managing a
library system.
Users can perform various actions including listing items, adding new entries,
searching based on various criteria,
deleting items, and exiting the application.

The script interacts with a backend module to handle data storage and
retrieval.

Usage:
1. Run this script.
2. Follow the on-screen menu prompts to perform desired actions.

Usage Examples:
- To list all available items, select option 1 from the menu.
- To add a new item, choose option 2 and provide the required details.
- To find items by title, select option 3 and enter the title.
- For searching items by author, select option 4 and input the author's name.
- If searching items by year of release piques your interest, opt for option 5
and input the year.
- To search items by genre, select option 6 and enter the genre.
- To search items using multiple filters, select option 7 and input filters.
- To delete an item by its ID, select option 8 and input the corresponding ID.
- To gracefully conclude your interaction with the application, select
option 9.

"""

import backend  # Import the backend module for data handling


COLUMN_SEPARATOR_WIDTH = 3
TABLE_RIGHT_MARGIN = 1
DATA_FIELDS = ["title", "author", "year", "genre"]
MENU_OPTIONS = ["List all items", "Add a new item", "Search by title",
                "Search by author", "Search by year", "Search by genre",
                "Multi-Criteria Search", "Delete an item by ID", "Quit"
                ]


def get_new_item_input():
    """
    Get input from the user for creating a new item.

    Returns:
        dict: A dictionary containing item details (title, author, year,
        genre).
    """
    prompts = [
        "Enter title: ",
        "Enter author: ",
        "Enter year: ",
        "Enter genre: "
    ]
    user_inputs = []

    for prompt in prompts:
        while True:
            input_value = input(prompt)
            if not input_value:
                print("This field is required. Please provide a value.")
            else:
                user_inputs.append(input_value)
                break

    new_item = dict(zip(DATA_FIELDS, user_inputs))
    return new_item


def add_book_record(data_store):
    """
    Add a new item to the library.

    Args:
        data_store (object): The data storage object from the backend module.

    Returns:
        None
    """
    new_item = get_new_item_input()
    data_store.add_book_record(new_item)
    print("\n\033[1;32mThe item has been successfully added.\033[0m")


def delete_item(data_store, item_id):
    """
    Delete an item from the library based on its ID.

    Args:
        data_store (object): The data storage object from the backend module.
        item_id (int): The ID of the item to be deleted.

    Returns:
        None
    """
    # Check if the item with the specified ID exists in the data store
    if data_store.delete_item_by_id(item_id):
        print("The item has been successfully deleted.")
    else:
        print(
            "\n\033[1;31mSorry, the item with the specified ID was not found.\033[0m")


def list_items(items):
    """
    Display a list of items in a tabular format.

    Args:
        items (list): List of item dictionaries to be displayed.

    Returns:
        None
    """
    items_list = list(items)
    if not items_list:
        print("\n\033[1;31mNo items found.\033[0m")
        return

    # Define headers for the columns in the table
    headers = ["ID", "Title", "Author", "Year", "Genre"]

    # Calculate the appropriate column widths for formatting
    column_widths = {
        header: max(len(str(item[header.lower()])) for item in items_list)
        for header in headers
    }

    # Update the column widths to accommodate header lengths
    column_widths.update(
        {header: max(len(header), width)
         for header, width in column_widths.items()}
    )

    # Calculate the total width of the table
    total_width = sum(column_widths.values()) + len(headers) * \
        COLUMN_SEPARATOR_WIDTH + TABLE_RIGHT_MARGIN
    horizontal_line = "-" * total_width

    # Format strings for the table header and data rows
    header_format = " | ".join(
        [f"{{:<{column_widths[header]}}}" for header in headers]
    )
    data_format = " | ".join(
        [f"{{:<{column_widths[header]}}}" for header in headers]
    )

    # Print the header row and horizontal line
    print(horizontal_line, header_format.format(
        *headers), horizontal_line, sep="\n")

    # Extract values for each item and print them in a formatted row
    formatted_items = map(
        lambda item: [item[header.lower()] for header in headers], items_list
    )
    for values in formatted_items:
        print(data_format.format(*values))

    # Print the horizontal line to complete the table
    print(horizontal_line)


def main():
    """
    Main function to run the Library System.

    Args:
        None

    Returns:
        None
    """
    # Create a data storage object using the backend module
    data_store = backend.create_data_store('data.json')

    # Define the menu options available to the user as a dictionary
    options = {str(index + 1): option for index,
               option in enumerate(MENU_OPTIONS)}

    # Main loop to repeatedly present the menu to the user
    while True:
        print(
            "\n\033[1;4mWelcome to the Library System!\033[0m\n\n\033[1;32mChoose an option:\033[0m")

        # Display the menu options with corresponding indices
        for key, value in options.items():
            print(f"{key}. {value}")

        # Get the user's choice from the menu
        choice = input("\n\033[1;32mEnter your choice: \033[0m")

        # Process the user's choice using match case
        match choice:
            case "1":
                list_items(data_store.get_all_items())
            case "2":
                add_book_record(data_store)
            case "3" | "4" | "5" | "6":
                field_mapping = {}
                for i, field in enumerate(DATA_FIELDS, start=3):
                    field_mapping[str(i)] = field

                field = field_mapping[choice]
                search_term = input(f"Enter {field} to search: ")
                search_result = list(
                    data_store.search_by_field(field, search_term))
                list_items(search_result)
            case "7":  # Handle the new "Search by filter" option
                filters = {}
                for field in DATA_FIELDS:
                    search_term = input(f"Enter {field} to search: ")
                    if search_term:
                        filters[field] = search_term
                search_result = data_store.search_With_Multiple_Parameters(
                    filters)
                list_items(search_result)
            case "8":
                item_id = int(
                    input("Please enter the ID of the item you want to delete: "))
                delete_item(data_store, item_id)
            case "9":
                print("\n\033[1;32mUntil next time!\n"
                      "Remember, books open doors to new worlds.\n"
                      "Have a good day!\033[0m")
                break
            case _:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
