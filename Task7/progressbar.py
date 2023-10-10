import time
import sys

# ANSI escape codes to hide and show the cursor
HIDE_CURSOR = '\x1b[?25l'
SHOW_CURSOR = '\x1b[?25h'


class MyProgressBar(object):
    """
    A custom progress bar implementation for tracking the progress of tasks.

    Args:
        max_value (int): The maximum value that represents 100% completion.
        message (str, optional): An optional message to display alongside the
        progress bar. width (int, optional): The width of the progress bar
        (number of characters).

    Methods:
        update(n=1): Update the progress bar with the specified progress.
        finish(): Finish and display the final state of the progress bar.
    """

    def __init__(self, max_value, message='', width=40):
        """
        Initialize the MyProgressBar instance.

        Args:
            max_value (int): The maximum value that represents 100% completion.
            message (str, optional): An optional message to display alongside
            the progress bar. width (int, optional): The width of the progress
            bar (number of characters).
        """
        self.max_value = max_value
        self.message = message
        self.width = width
        self.start_ts = time.monotonic()
        self._ts = self.start_ts
        self.index = 0

        # Hide the cursor if the standard error is a terminal
        if sys.stderr.isatty():
            print(HIDE_CURSOR, end='')

    def update(self, n=1):
        """
        Update the progress bar with the specified progress.

        Args:
            n (int, optional): The amount of progress to add. Default is 1.
        """
        now = time.monotonic()
        self._ts = now
        self.index += n

        # Calculate progress percentage and display bars
        percent = min(1, self.index / self.max_value)
        filled_length = int(self.width * percent)
        empty_length = self.width - filled_length
        filled_bar = '#' * filled_length
        empty_bar = ' ' * empty_length

        # Calculate elapsed and remaining time
        elapsed = int(now - self.start_ts)
        remaining = int((self.max_value - self.index) *
                        (elapsed / self.index)) if self.index > 0 else 0

        # Construct and display the progress line
        progress_line = (
            f'\r{self.message} [{filled_bar}{empty_bar}] '
            f'{self.index}/{self.max_value} '
            f'Elapsed: {elapsed}s Remaining: {remaining}s'
        )

        sys.stderr.write(progress_line)
        sys.stderr.flush()

    def finish(self):
        """
        Finish and display the final state of the progress bar.
        """
        # Show the cursor and add a newline
        if sys.stderr.isatty():
            print(SHOW_CURSOR, end='')
        print('\n')
