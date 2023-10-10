from text_processor import TextProcessor
import user_interface

OUTPUT_FILE_NAME = 'formatted_text.txt'


def process_file(input_file_path, max_chunk_size):
    """
    Process  the  input  text  file,  split each line into chunks, and save the
    result in a new file.
    Args:
     input_file_path (str): The path to the input text file.
     max_chunk_size (int): The maximum allowed number of characters per line.
    Process Flow:
     1. Opens the input text file for reading and the output file for writing.
     2. Reads  each  line  from  the  input  file,  strips leading and trailing
    whitespaces, and splits the line into chunks.
    Chunks  are  created  based  on  the  specified  max_chunk_size  using  the
    split_text_into_chunks method from the TextProcessor class.
     3. Adjusts  the  length  of each chunk to fit the specified max_chunk_size
    using the adjust_chunk_length method from the TextProcessor class.
    The adjusted chunks are then written to the output file.
     4. Displays  a  success  message,  indicating  that  the  file  processing
    completed successfully, and provides the path to the output file.
    Exceptions:
     - If  the  input file is not found, the function displays a file not found
    error  message  using  the  display_file_not_found_error  function from the
    user_interface module.
     - If  any  other  unexpected  exception occurs during file processing, the
    function   displays   an  error  message  using  the  display_error_message
    function from the user_interface module.
    Note:
     The max_chunk_size  should  be  greater  than  35 characters for effective
    formatting.
    Returns:
    None:  The  function does not return any value. The processed text is saved
    in the output file.
    """

    # Set the output file path to store the processed text.
    output_file_path = OUTPUT_FILE_NAME

    try:
        # Create an instance of TextProcessor
        processor = TextProcessor(max_chunk_size)

        # Open the input file for reading and the output file for writing.
        with open(input_file_path, 'r') as input_file, \
                open(output_file_path, 'w') as output_file:
            # Process each line in the input file.
            for line in input_file:
                # Remove leading and trailing whitespaces from the line.
                line = line.strip()

                # Split the line into smaller chunks based on the specified \
                # max_chunk_size.
                chunks = processor.split_text_into_chunks(line)

                # Process each chunk.
                for i, chunk in enumerate(chunks, 1):
                    # If the chunk is not the last one, adjust its length to \
                    # the maximum size.
                    if i < len(chunks):
                        adjusted_chunk = processor.adjust_chunk_length(chunk)
                        # Write the adjusted chunk to the output file, \
                        # followed by a newline.
                        output_file.write(adjusted_chunk + '\n')
                    else:
                        # For the last chunk, write it to the output file as \
                        # is, followed by a newline.
                        output_file.write(chunk + '\n')

        # Display a success message after processing the file.
        user_interface.display_success_message(output_file_path)

    except FileNotFoundError:
        # Handle the case where the input file is not found.
        user_interface.display_file_not_found_error(input_file_path)

    except Exception as e:
        # Catch and handle any other exceptions that might occur during file \
        # processing.
        user_interface.display_error_message(e)
