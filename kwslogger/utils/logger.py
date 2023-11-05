from pyfiglet import Figlet
from pystyle import Colors, Colorate, Center

class LoggerUtils:
    """
    A utility class for logging messages and creating logos.

    Methods:
    log_to_file(message: str, log_file: str = "mylogs", mode: str = "a") -> None:
        Logs a message to a file.

    create_logo(logo: str, font: str = "big") -> None:
        Creates a logo using the specified font and displays it.

    display_logo(logo: str) -> None:
        Displays a logo.
    """

    def log_to_file(self, message: str, log_file: str = "mylogs", mode: str = "a") -> None:
        """
        Logs a message to a file.

        Args:
        message (str): The message to log.
        log_file (str): The name of the log file. Defaults to "mylogs".
        mode (str): The mode to open the file in. Defaults to "a" (append).
        """
        if not message:
            raise ValueError("Message cannot be empty.")

        with open(f"{log_file}.log", mode, encoding="utf8") as f:
            f.write(f"{message}\n")

    def get_log_file_length(self, log_file: str = "mylogs") -> int:
        """
        Returns the length of a log file.

        Args:
        log_file (str): The name of the log file. Defaults to "mylogs".

        Returns:
        int: The length of the log file.
        """
        with open(f"{log_file}.log", "r", encoding="utf8") as f:
            return len(f.readlines())

    def wipe_log_file(self, log_file: str = "mylogs") -> None:
        """
        Wipes the contents of a log file.

        Args:
        log_file (str): The name of the log file. Defaults to "mylogs".
        """
        with open(f"{log_file}.log", "w", encoding="utf8") as f:
            f.write("")

    def create_logo(self, logo: str, font: str = "big") -> None:
        """
        Creates a logo using the specified font and displays it.

        Args:
        logo (str): The text to use for the logo.
        font (str): The font to use for the logo. Defaults to "big".
        """
        if not logo:
            raise ValueError("Logo cannot be empty.")

        figlet_instance = Figlet(font=font)
        logo_string = figlet_instance.renderText(logo)
        self.display_logo(logo_string)

    def display_logo(self, logo: str) -> None:
        """
        Displays a logo.

        Args:
        logo (str): The logo to display.
        """
        if not logo:
            raise ValueError("Logo cannot be empty.")

        centered_logo = Center.XCenter(Colorate.Vertical(Colors.white_to_blue, logo, 1))
        divider = Center.XCenter(Colorate.Vertical(Colors.white_to_blue, "────────────────────────────────────────────\n", 1))

        print(centered_logo)
        print(divider)