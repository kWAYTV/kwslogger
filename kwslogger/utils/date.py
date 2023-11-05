import pytz
from datetime import datetime

class DateHelper:
    """
    A class for handling date and time operations.

    Attributes:
    timezone (pytz.timezone): The timezone to use for date and time operations.
    """

    def __init__(self, timezone: str = "Europe/Madrid"):
        self.timezone = pytz.timezone(timezone)

    def get_current_timestamp(self) -> datetime:
        """
        Get the current timestamp in the specified timezone.

        Returns:
        datetime: The current timestamp.
        """
        return datetime.now(self.timezone)

    def get_formatted_timestamp(self) -> str:
        """
        Get the current timestamp in the specified timezone.

        Returns:
        str: The current timestamp in the format "dd/mm/yyyy • hh:mm:ss".
        """
        datetime_now = datetime.now(self.timezone)
        current_time = datetime_now.strftime("%d/%m/%Y • %H:%M:%S")
        
        return current_time