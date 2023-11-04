from os import system, name
from colorama import Fore, Style, init
from kwslogger.utils.date import DateHelper
from kwslogger.utils.logger import LoggerUtils
from kwslogger.controllers.spinners import Spinners
from kwslogger.controllers.loglevel import LogLevels
from kwslogger.controllers.progress_bars import ProgressBars


class Logger:
    """
    A class for logging messages with different log levels and options to log to file.

    Attributes:
    - debug_active (bool): Whether debug mode is active or not.
    - log_level (str): The log level to use for logging messages.
    - log_to_file (bool): Whether to log messages to a file or not.
    - log_file_name (str): The name of the log file to use.
    - log_file_mode (str): The mode to use when opening the log file.

    Methods:
    - clear(): Clears the console screen.
    - _log(type: str, color, message: str): Logs a message with the given type and color.
    - info(message: str): Logs an info message.
    - success(message: str): Logs a success message.
    - warning(message: str): Logs a warning message.
    - error(message: str): Logs an error message.
    - input(message: str): Logs an input message.
    - ratelimit(message: str): Logs a ratelimit message.
    - welcome(message: str): Logs a welcome message.
    - debug(message: str): Logs a debug message if debug mode is active.
    - sleep(message: str, seconds: int): Sleeps for the given number of seconds with a spinner.
    - run_with_spinner(func: callable, message: str = "", timer: bool = Flase,*args, **kwargs): Runs a function with a spinner and optional timer.
    """
    def __init__(self, log_level: str = "ANY", log_to_file: bool = False, log_file_name: str = None, log_file_mode: str = None, log_file_format: str = ""):
        """
        Initializes a new instance of the Logger class.

        Args:
        - log_level (str): The log level to use for logging messages.
        - log_to_file (bool): Whether to log messages to a file or not.
        - log_file_name (str): The name of the log file to use.
        - log_file_mode (str): The mode to use when opening the log file.
        """
        self.log_level = log_level
        self.log_to_file = log_to_file
        self.log_file_name = log_file_name
        self.log_file_mode = log_file_mode
        self.spinners = Spinners()
        self.logger_utils = LoggerUtils()
        self.datetime_helper = DateHelper()
        self.progress_bars = ProgressBars()
        self.log_levels_controller = LogLevels()

        init(autoreset=True)

    def clear(self) -> None:
        """
        Clears the console screen.
        """
        return system("cls" if name in ("nt", "dos") else "clear")

    def _log(self, type: str, color, message: str) -> None:
        """
        Logs a message with the given type and color.

        Args:
        - type (str): The type of the message to log.
        - color: The color to use for the message.
        - message (str): The message to log.
        """
        if not self.can_log(type): return
        
        current_time = self.datetime_helper.get_current_timestamp()
        
        if self.log_to_file:
            file_string = f"{current_time} • [{type}] {message}"
            self.logger_utils.log_to_file(file_string, self.log_file_name, self.log_file_mode)

        return print(f"{Style.DIM}{current_time} • {Style.RESET_ALL}{Style.BRIGHT}{color}[{Style.RESET_ALL}{type}{Style.BRIGHT}{color}] {Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}{message}{Style.RESET_ALL}")

    def info(self, message: str) -> None:
        """
        Logs an info message.

        Args:
        - message (str): The message to log.
        """
        return self._log("INFO", Fore.CYAN, message)

    def success(self, message: str) -> None:
        """
        Logs a success message.

        Args:
        - message (str): The message to log.
        """
        return self._log("SUCCESS", Fore.GREEN, message)

    def warning(self, message: str) -> None:
        """
        Logs a warning message.

        Args:
        - message (str): The message to log.
        """
        return self._log("WARNING", Fore.YELLOW, message)

    def error(self, message: str) -> None:
        """
        Logs an error message.

        Args:
        - message (str): The message to log.
        """
        return self._log("ERROR", Fore.RED, message)

    def input(self, message: str) -> None:
        """
        Logs an input message.

        Args:
        - message (str): The message to log.
        """
        return self._log("INPUT", Fore.BLUE, message)

    def ratelimit(self, message: str) -> None:
        """
        Logs a ratelimit message.

        Args:
        - message (str): The message to log.
        """
        return self._log("RATELIMIT", Fore.YELLOW, message)

    def welcome(self, message: str) -> None:
        """
        Logs a welcome message.

        Args:
        - message (str): The message to log.
        """
        return self._log("WELCOME", Fore.GREEN, message)

    def debug(self, message: str) -> None:
        """
        Logs a debug message if debug mode is active.

        Args:
        - message (str): The message to log.
        """
        return self._log("DEBUG", Fore.MAGENTA, message)

    def sleep(self, message: str, seconds: int) -> None:
        """
        Sleeps for the given number of seconds with a spinner.

        Args:
        - message (str): The message to display while sleeping.
        - seconds (int): The number of seconds to sleep.
        """
        return self.spinners.sleep_with_spinner(message, seconds)

    def run_with_spinner(self, func: callable, message: str = "", timer: bool = False,  *args, **kwargs):
        """
        Runs a function with a spinner.

        Args:
        - func (callable): The function to run.
        - message (str): The message to display while running the function.
        - timer (bool): Whether to display a timer or not.
        - *args: Positional arguments to pass to the function.
        - **kwargs: Keyword arguments to pass to the function.
        """
        return self.spinners.func_with_spinner(func, message, timer, *args, **kwargs)
    
    def can_log(self, type: str):
        """
        Returns True if the given log level is equal to or lower than the required log level, False otherwise.

        Parameters:
        -----------
        type : str
            The log level type.

        Returns:
        --------
        bool
            True if the given log level is equal to or lower than the required log level,
            False otherwise.
        """
        return self.log_levels_controller.should_log(type, self.log_level)

    def progress_bar(self, iterable, desc: str = "Progress", *args, **kwargs):
        """
        Returns a progress bar.

        Args:
        - iterable (iterable): The iterable to loop over.
        - desc (str): The description to display.
        - *args: Positional arguments to pass to tqdm.
        - **kwargs: Keyword arguments to pass to tqdm.
        """
        return self.progress_bars.progress_bar(iterable, desc, *args, **kwargs)