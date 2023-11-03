import time
from kwslogger import Logger

"""
This script demonstrates the usage of the kwslogger module.
"""

# Create a logger instance
logger = Logger(debug=True) # Default debug: False

# Clear the console
logger.clear()

# Log a message
logger.welcome("I'm a welcome message!")
logger.info("I'm an info message!")
logger.debug("I'm a debug message!")
logger.success("I'm a success message!")
logger.warning("I'm a warning!")
logger.error("I'm an error!")
logger.input("I'm an input message!")
logger.ratelimit("I'm a rate limit message!")

# Wait for 3 seconds using spinners
logger.sleep("Waiting for 1 second...", 1)

def test_func(number1, number2):
    answer = number1 + number2
    return answer

result = logger.run_with_spinner(test_func, "Calculating...", 1, 1)
print(str(result) + " (Func returned)")
