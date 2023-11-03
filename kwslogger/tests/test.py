import kwslogger

# Create a logger
logger = kwslogger.Logger()

# Clear the console
logger.clear()

# Log a message
logger.info("I'm an info message!")
logger.success("I'm a success message!")
logger.warning("I'm a warning!")
logger.error("I'm an error!")

# Wait for the user to input something to exit the program
input("\nPress enter to exit...")
logger.clear()
exit()