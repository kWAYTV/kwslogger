class LoggerUtils:
    def __init__(self):
        pass

    def log_to_file(self, message, log_file: str ="mylogs", mode: str ="a"):
        """
        Logs the given message to a file.

        Args:
            message (str): The message to be logged.
            log_file (str, optional): The name of the log file. Defaults to "mylogs".
            mode (str, optional): The mode in which the file should be opened. Defaults to "a".
        """
        with open(f"{log_file}.log", mode, encoding="utf8") as f:
            f.write(f"{message}\n")