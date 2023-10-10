import file_processor
import user_interface

INPUT_FILE_NAME = 'text.txt'


def main():
    """
    Main function of the application that initiates the text file processing.
    Process Flow:
     1. Gets  the path to the input text file (input_file_path) and the maximum
    line size (max_chunk_size)
    using the user interface from the user_interface module.
     2. Processes  the  text  file by splitting lines into chunks and saves the
    result in a separate file.
    This   process   is   done   using   the  process_file  function  from  the
    file_processor module.
    """

    # Path to the input text file (can be changed to another file).
    input_file_path = INPUT_FILE_NAME
    # Get the maximum line size.
    max_chunk_size = user_interface.get_max_chunk_size_from_user()

    # Start processing the text file with the specified maximum line size.
    file_processor.process_file(input_file_path, max_chunk_size)


if __name__ == '__main__':
    main()
