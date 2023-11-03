from os import system, name
from kwslogger.utils.date import DateHelper
from kwslogger.utils.spinners import Spinners
from colorama import Fore, Style, init


class Logger:
    """
    A class for logging messages with different levels and colors.

    Attributes:
    -----------
    debug : bool
        A flag to indicate whether debug messages should be logged or not.

    Methods:
    --------
    clear() -> None:
        Clears the console.

    info(message: str) -> None:
        Logs an information message.

    success(message: str) -> None:
        Logs a success message.

    warning(message: str) -> None:
        Logs a warning message.

    sleep(message: str) -> None:
        Logs a sleep message.

    error(message: str) -> None:
        Logs an error message.

    input(message: str) -> None:
        Logs an input message.

    ratelimit(message: str) -> None:
        Logs a rate limit message.

    welcome(message: str) -> None:
        Logs a welcome message.

    debug(message: str) -> None:
        Logs a debug message if debug flag is set to True.

    random_spinner_wait(message: str, seconds: int) -> None:
        Displays a random spinner and waits for the specified number of seconds.

    spinner_wait(name: str, message: str, seconds: int) -> None:
        Displays a spinner with the specified name and waits for the specified number of seconds.
    """
    def __init__(self, debug: bool = False):
        self.debug_active = debug
        self.spinners = Spinners()
        self.datetime_helper = DateHelper()

        # Initialize colorama
        init(autoreset=True)

    def clear(self) -> None:
        """
        Clears the console.
        """
        return system("cls" if name in ("nt", "dos") else "clear")

    def _log(self, type, color, message) -> None:
        """
        Logs a message with the specified type and color.

        Parameters:
        -----------
        type : str
            The type of the message (e.g. INFO, SUCCESS, WARNING, etc.).
        color : str
            The color of the message (e.g. Fore.CYAN, Fore.GREEN, Fore.YELLOW, etc.).
        message : str
            The message to be logged.
        """
        current_time = self.datetime_helper.get_current_timestamp()
        return print(f"{Style.DIM}{current_time} • {Style.RESET_ALL}{Style.BRIGHT}{color}[{Style.RESET_ALL}{type}{Style.BRIGHT}{color}] {Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}{message}{Style.RESET_ALL}")

    def info(self, message: str) -> None:
        """
        Logs an information message.

        Parameters:
        -----------
        message : str
            The message to be logged.
        """
        return self._log("INFO", Fore.CYAN, message)

    def success(self, message: str) -> None:
        """
        Logs a success message.

        Parameters:
        -----------
        message : str
            The message to be logged.
        """
        return self._log("SUCCESS", Fore.GREEN, message)

    def warning(self, message: str) -> None:
        """
        Logs a warning message.

        Parameters:
        -----------
        message : str
            The message to be logged.
        """
        return self._log("WARNING", Fore.YELLOW, message)

    def sleep(self, message: str) -> None:
        """
        Logs a sleep message.

        Parameters:
        -----------
        message : str
            The message to be logged.
        """
        return self._log("SLEEP", Fore.YELLOW, message)

    def error(self, message: str) -> None:
        """
        Logs an error message.

        Parameters:
        -----------
        message : str
            The message to be logged.
        """
        return self._log("ERROR", Fore.RED, message)

    def input(self, message: str) -> None:
        """
        Logs an input message.

        Parameters:
        -----------
        message : str
            The message to be logged.
        """
        return self._log("INPUT", Fore.BLUE, message)

    def ratelimit(self, message: str) -> None:
        """
        Logs a rate limit message.

        Parameters:
        -----------
        message : str
            The message to be logged.
        """
        return self._log("RATELIMIT", Fore.YELLOW, message)

    def welcome(self, message: str) -> None:
        """
        Logs a welcome message.

        Parameters:
        -----------
        message : str
            The message to be logged.
        """
        return self._log("WELCOME", Fore.GREEN, message)

    def debug(self, message: str) -> None:
        """
        Logs a debug message if debug flag is set to True.

        Parameters:
        -----------
        message : str
            The message to be logged.
        """
        if not self.debug_active: return
        return self._log("DEBUG", Fore.MAGENTA, message)

    def spinner_wait(self, message: str, seconds: int) -> None:
        """
        Displays a spinner with the specified name and waits for the specified number of seconds.

        Parameters:
        -----------
        name : str
            The name of the spinner to be displayed.
        message : str
            The message to be displayed with the spinner.
        seconds : int
            The number of seconds to wait.
        """
        return self.spinners.wait_spinner(message, seconds)
