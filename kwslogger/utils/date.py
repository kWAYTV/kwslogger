import pytz
from datetime import datetime

class DateTime:
    """
    A class for handling date and time operations.

    Attributes:
    timezone (pytz.timezone): The timezone to use for date and time operations.
    """

    def __init__(self):
        self.timezone = pytz.timezone('Europe/Madrid')

    def get_current_timestamp(self) -> str:
        """
        Get the current timestamp in the specified timezone.

        Returns:
        str: The current timestamp in the format "dd/mm/yyyy • hh:mm:ss".
        """
        datetime_now = datetime.now(self.timezone)
        current_time = datetime_now.strftime("%d/%m/%Y • %H:%M:%S")
        
        return current_time