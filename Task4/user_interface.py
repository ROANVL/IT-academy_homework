MIN_CHUNK_SIZE = 35


def get_max_chunk_size_from_user():
    """
    Prompt  the  user  to  input  the  maximum  number  of  characters per line
    (max_chunk_size).
    Returns:
    int:  The  maximum  allowed  number of characters per line, provided by the
    user.
    Note:
    -  The  function  uses  a  while loop to repeatedly prompt the user until a
    valid integer greater than MIN_CHUNK_SIZE is provided.
    -  If  the  user  enters a non-integer value, a ValueError is raised and an
    error message is displayed.
    """

    while True:
        try:
            max_chunk_size = int(input(
                'Enter the maximum number of characters per line\n'
                f'(should be greater than {MIN_CHUNK_SIZE}): '))

            if max_chunk_size <= MIN_CHUNK_SIZE:
                print(f'Error: The maximum chunk size should be greater'
                      f' than {MIN_CHUNK_SIZE}.')
            else:
                return max_chunk_size

        except ValueError:
            print('Error: Please enter a valid integer for the '
                  'maximum chunk size.')


def display_success_message(output_file_path):
    """
    Display a success message after file processing is completed.
    Args:
    output_file_path  (str):  The  path  to the output file where the processed
    text is saved.
    Note:
    -   The  function  prints  a  success  message  indicating  that  the  file
    processing is completed successfully.
    -  It also provides the path to the output file where the processed text is
    saved.
    """

    print(f'File processing completed successfully.\n'
          f'Processed text saved in {output_file_path}.')


def display_file_not_found_error(input_file_path):
    """
    Display an error message when the input file is not found.
    Args:
    input_file_path (str): The path to the input file that is not found.
    Note:
    -  The function prints an error message indicating that the specified input
    file is not found.
    """

    print(f'Error: File {input_file_path} not found.')


def display_error_message(error):
    """
    Display an error message for any other exceptions during file processing.
    Args:
    error (Exception): The exception that occurred during file processing.
    Note:
    -  The  function  prints an error message indicating that an error occurred
    during file processing.
    - It displays the specific error message from the caught exception.
    """

    print(f'An error occurred: {error}')
