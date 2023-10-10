class TextProcessor:
    """
    A  utility  class  for  processing  text  by  splitting  it into chunks and
    adjusting the length of each chunk to fit a specified maximum chunk size.

    Attributes:
        max_chunk_size (int): The maximum allowed number of characters per
        line.

    Methods:
        split_text_into_chunks(text):
            Splits the given text into chunks of words, where each chunk has a
            length not exceeding the specified max_chunk_size.

        adjust_chunk_length(chunk):
            Adjusts the length of a given chunk of text by distributing spaces
            between words. If the input chunk is already equal to or longer
            than the maximum size, it will be returned unchanged.
    """

    def __init__(self, max_chunk_size):
        """
        Initializes a new instance of the TextProcessor class with the
        specified maximum chunk size.

        Args:
            max_chunk_size (int): The maximum allowed number of characters per
            line.
        """
        self.max_chunk_size = max_chunk_size

    def split_text_into_chunks(self, text):
        """
        Splits the given text into chunks of words, where each chunk has a
        length not exceeding the specified max_chunk_size.

        Args:
            text (str): The input text to be split into chunks.

        Returns:
            list: A list of chunks, each containing a portion of the input
            text.
        """
        chunks = []
        start_index = 0

        while start_index < len(text):
            end_index = start_index + self.max_chunk_size
            if end_index < len(text):
                end_index = text.rfind(' ', start_index, end_index)

            if end_index == -1 or end_index == start_index:
                end_index = start_index + self.max_chunk_size

            chunks.append(text[start_index:end_index].strip())
            start_index = end_index

        return chunks

    def adjust_chunk_length(self, chunk):
        """
        Adjusts the length of a given chunk of text by distributing spaces
        between words.
        If the input chunk is already equal to or longer than the maximum size,
        it will be returned unchanged.

        Args:
            chunk (str): The input chunk of text to be adjusted.

        Returns:
            str: The adjusted chunk of text with spaces distributed between
            words.
        """
        if len(chunk) >= self.max_chunk_size:
            return chunk

        words = chunk.split()
        total_spaces = self.max_chunk_size - sum(map(len, words))
        num_words = len(words)

        # If there's only one word, add extra spaces to the right to reach
        # max_chunk_size
        if num_words == 1:
            return words[0] + ' ' * total_spaces

        # Determine the number of gaps (spaces between words) and the number
        # of extra spaces
        gaps = num_words - 1
        spaces_per_gap, extra_spaces = divmod(total_spaces, gaps)

        # Distribute spaces among the words
        adjusted_chunk = words[0]
        for word in words[1:]:
            num_spaces = spaces_per_gap + (1 if extra_spaces > 0 else 0)
            adjusted_chunk += ' ' * num_spaces + word
            extra_spaces -= 1 if extra_spaces > 0 else 0

        return adjusted_chunk
