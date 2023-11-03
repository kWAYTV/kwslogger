class LoggerUtils:
    def __init__(self):
        pass

    def log_to_file(self, message, log_file: str ="mylogs", mode: str ="a"):
        with open(f"{log_file}.log", mode, encoding="utf8") as f:
            f.write(f"{message}\n")