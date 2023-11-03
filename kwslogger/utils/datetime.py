import pytz
from datetime import datetime

class DateTime:
    def __init__(self):
        self.timezone = pytz.timezone('Europe/Madrid')

    def get_current_timestamp(self):
        # Set the timezone to Central European Time (Spain)
        # Return the current time in the specified timezone
        datetime_now = datetime.now(self.timezone)

        # Format the current time to the following format: 01/01/2021 • 00:00:00
        current_time = datetime_now.strftime("%d/%m/%Y • %H:%M:%S")
        return current_time