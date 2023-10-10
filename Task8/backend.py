import json


class DataStore:
    """
    DataStore Class

    A class responsible for managing data storage and retrieval operations.
    It provides methods for loading, saving, adding, deleting, and searching
    items in a data store.

    Attributes:
        filename (str): The name of the JSON file used for data storage.
        data (list): The list containing the data items stored in the data
        store.

    Methods:
        load_data(): Loads data from the JSON file into the data store.
        save_data(): Saves the current data store content to the JSON file.
        add_book_record(item): Adds a new item to the data store.
        delete_item_by_id(item_id): Deletes an item from the data store by its
        ID.
        get_all_items(): Retrieves all items from the data store.
        recalculate_ids(): Recalculates IDs of items after deletion.
        search_by_field(field_name, search_term): Searches items by a specific
        field value.
        search_With_Multiple_Parameters(filters): Searches items using multiple filters.

    """

    def __init__(self, filename):
        """
        Initialize a DataStore instance.

        Args:
            filename (str): The name of the JSON file used for data storage.

        """
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        """
        Load data from the JSON file into the data store.

        Returns:
            list: The loaded data from the JSON file.

        """
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self):
        """
        Save the current data store content to the JSON file.

        """
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def add_book_record(self, item):
        """
        Add a new item to the data store.

        Args:
            item (dict): A dictionary containing the item's details (title,
            author, year, genre).

        """
        new_id = len(self.data) + 1
        new_item = {
            'title': item['title'],
            'author': item['author'],
            'year': item['year'],
            'genre': item['genre'],
            'id': new_id
        }
        self.data.append(new_item)
        self.save_data()

    def delete_item_by_id(self, item_id):
        """
        Delete an item from the data store by its ID.

        Args:
            item_id (int): The ID of the item to be deleted.

        Returns:
            bool: True if the item was successfully deleted, False otherwise.

        """
        item_to_delete = next(
            (item for item in self.data if item['id'] == item_id), None)
        if item_to_delete:
            self.data.remove(item_to_delete)
            self.recalculate_ids()
            self.save_data()
            return True
        return False

    def get_all_items(self):
        """
        Retrieve all items from the data store.

        Returns:
            list: A list containing all items in the data store.

        """
        return self.data

    def recalculate_ids(self):
        """
        Recalculate IDs of items after deletion.

        """
        for index, item in enumerate(self.data, start=1):
            item['id'] = index

    def search_by_field(self, field_name, search_term):
        """
        Search items by a specific field value.

        Args:
            field_name (str): The name of the field to be searched (title,
            author, year, genre).
            search_term (str): The search term to match.

        Yields:
            dict: Items matching the search criteria.

        """
        search_term = search_term.lower()
        search_results = []

        for item in self.data:
            field_value = item[field_name].lower()
            if any(word.startswith(search_term) for word in field_value.split()):
                search_results.append(item)

        return search_results

    def search_With_Multiple_Parameters(self, filters):
        """
        Search items using multiple filters.

        Args:
            filters (dict): A dictionary of field-value pairs for filtering.

        Returns:
            list: Items matching the combined filter criteria.

        """
        results = self.data

        for field, search_term in filters.items():
            search_term = search_term.lower()
            search_results = []
            for item in results:
                field_value = item[field].lower()
                if any(word.startswith(search_term) for word in field_value.split()):
                    search_results.append(item)
            results = search_results

        return results


def create_data_store(filename):
    """
    Create a DataStore instance.

    Args:
        filename (str): The name of the JSON file used for data storage.

    Returns:
        DataStore: An instance of the DataStore class.

    """
    return DataStore(filename)
