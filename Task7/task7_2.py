class FileNotFoundErrorCustom(Exception):
    """Custom exception for file not found error."""

    def __init__(self, file_path):
        self.message = f"File '{file_path}' not found"
        super().__init__(self.message)


def read_file_contents(file_path):
    """Reads file contents and handles errors."""
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        raise FileNotFoundErrorCustom(file_path)


# Example usage of the function
def main():
    file_path = "example.txt"
    try:
        file_contents = read_file_contents(file_path)
        print(file_contents)
    except FileNotFoundErrorCustom as e:
        print(e)


if __name__ == "__main__":
    main()
