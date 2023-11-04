class LogLevels:
    """
    A class that defines the hierarchy of log levels and provides methods to get the level value and check if a log should be made.

    Attributes:
    -----------
    HIERARCHY : dict
        A dictionary that maps log level names to their corresponding integer values.

    Methods:
    --------
    get_level(type: str) -> int:
        Returns the integer value of the given log level type.

    should_log(current_level: str, required_level: str) -> bool:
        Returns True if the current log level is equal to or lower than the required log level, False otherwise.
    """
    hierarchy = {
    "DEBUG": 0,
    "INFO": 1,
    "WELCOME": 2,
    "SUCCESS": 3,
    "WARNING": 4,
    "INPUT": 5,
    "ERROR": 6,
    "RATELIMIT": 7,
    "SLEEP": 8,
    "ANY": 9,
    }

    @classmethod
    def get_level(cls, type: str) -> int:
        """
        Returns the integer value of the given log level type.

        Parameters:
        -----------
        type : str
            The log level type.

        Returns:
        --------
        int
            The integer value of the given log level type.
        """
        return cls.hierarchy.get(type)

    @classmethod
    def should_log(cls, current_level: str, required_level: str) -> bool:
        """
        Returns True if the current log level is equal to or greater than the required log level.
        If the required log level is "ANY", returns True.

        Parameters:
        -----------
        - current_level: str
            The current log level.
        - required_level: str
            The required log level.

        Returns:
        --------
        - bool
            True if the current log level is equal to or greater than the required log level,
            False otherwise.
        """
        if required_level == "ANY":
            return True

        current_lvl_value = cls.get_level(current_level)
        required_lvl_value = cls.get_level(required_level)
        
        if current_lvl_value is None or required_lvl_value is None:
            return False
        return current_lvl_value <= required_lvl_value