from os import system, name
from colorama import Fore, Style, init
from ..utils.datetime import DateTime

class Logger:
    def __init__(self):
        self.datetime_helper = DateTime()

        # Initialize colorama
        init(autoreset=True)

    # Clear console function
    def clear(self):
        system("cls" if name in ("nt", "dos") else "clear")

    # General logging function
    def _log(self, type, color, message):
        current_time = self.datetime_helper.get_current_timestamp()
        print(f"{Style.DIM}{current_time} • {Style.RESET_ALL}{Style.BRIGHT}{color}[{Style.RESET_ALL}{type}{Style.BRIGHT}{color}] {Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}{message}{Style.RESET_ALL}")

    def info(self, message):
        self._log("INFO", Fore.CYAN, message)

    def success(self, message):
        self._log("SUCCESS", Fore.GREEN, message)

    def warning(self, message):
        self._log("WARNING", Fore.YELLOW, message)

    def sleep(self, message):
        self._log("SLEEP", Fore.YELLOW, message)

    def error(self, message):
        self._log("ERROR", Fore.RED, message)

    def input(self, message):
        self._log("INPUT", Fore.BLUE, message)

    def ratelimit(self, message):
        self._log("RATELIMIT", Fore.YELLOW, message)

    def welcome(self, message):
        self._log("WELCOME", Fore.GREEN, message)
