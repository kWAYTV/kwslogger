import time, random
from yaspin import yaspin
from yaspin.spinners import Spinners

class Spinners:
    """
    A class that provides various spinners to display while waiting for a process to complete.
    """

    def __init__(self):
        """
        Initializes the Spinners class with a list of available spinners.
        """
        self.spinners = [Spinners.balloon2, Spinners.bouncingBall, Spinners.pong, Spinners.point, Spinners.arc, Spinners.aesthetic, Spinners.star]

    def random_spinner(self) -> None:
        """
        Returns a random spinner from the list of available spinners.
        """
        return random.choice(self.spinners)
    
    def get_spinner(self, name) -> None:
        """
        Returns a spinner with the given name from the list of available spinners.
        """
        for spinner in self.spinners:
            if spinner.name == name:
                return spinner
        return None

    def random_spinner_wait(self, message: str, seconds: int) -> None:
        """
        Displays a random spinner with the given message for the specified number of seconds.
        """
        with yaspin(self.random_spinner(), text=message, timer=True) as sp:
            time.sleep(seconds)
            sp.ok("✔")

    def spinner_wait(self, name: str, message: str, seconds: int) -> None:
        """
        Displays a spinner with the given name and message for the specified number of seconds.
        """
        if self.get_spinner(name) is None: return
        with yaspin(self.get_spinner(name), text=message, timer=True) as sp:
            time.sleep(seconds)
            sp.ok("✔")