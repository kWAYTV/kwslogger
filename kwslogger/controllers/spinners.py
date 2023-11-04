import time
from yaspin import yaspin

class Spinners:
    """
    A class that provides a spinner to display while waiting for a process to complete.
    """

    def __init__(self):
        self.spinner_frames = ['⢹', '⢺', '⢼', '⣸', '⣇', '⡧', '⡗', '⡏']

    def sleep_with_spinner(self, message: str, seconds: int) -> None:
        """
        Displays a random spinner with the given message for the specified number of seconds.
        """

        with yaspin(self.spinner_frames, text=message, timer=True) as sp:
            time.sleep(seconds)
            sp.ok("✔")

    def func_with_spinner(self, func: callable, message: str = "", timer: bool = False, *args, **kwargs):
        """
        Runs a function with the given arguments and keyword arguments while displaying a spinner.
        """

        result = None
        with yaspin(self.spinner_frames, text=message, timer=timer) as sp:
            result = func(*args, **kwargs)
            sp.ok("✔")
        return result