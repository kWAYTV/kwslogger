import time
from yaspin import yaspin

class Spinners:
    """
    A class that provides various spinners to display while waiting for a process to complete.
    """

    def __init__(self):
        self.spinner_frames = ['⢹', '⢺', '⢼', '⣸', '⣇', '⡧', '⡗', '⡏']

    def wait_spinner(self, message: str, seconds: int) -> None:
        """
        Displays a random spinner with the given message for the specified number of seconds.
        """
        with yaspin(self.spinner_frames, text=message, timer=True) as sp:
            time.sleep(seconds)
            sp.ok("✔")