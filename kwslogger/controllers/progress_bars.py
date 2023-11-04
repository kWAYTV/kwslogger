from tqdm import tqdm

class ProgressBars:
    """
    A class that provides a spinner to display while waiting for a process to complete.
    """

    def __init__(self):
        self.controller = tqdm

    def progress_bar(self, iterable, desc: str = "Progress", *args, **kwargs):
        """
        Returns a progress bar.

        Args:
        - iterable (iterable): The iterable to loop over.
        - desc (str): The description to display.
        - *args: Positional arguments to pass to tqdm.
        - **kwargs: Keyword arguments to pass to tqdm.
        """
        return self.controller(iterable, desc=desc, *args, **kwargs)