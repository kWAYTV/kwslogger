import kwslogger

def main():
    """
    This function creates a logger using the kwslogger module and logs various messages using different log levels.
    It also waits for 3 seconds using a spinner and prompts the user to exit the program by pressing enter.
    """
    
    # Create a logger
    logger = kwslogger.Logger()

    # Clear the console
    logger.clear()

    # Log a message
    logger.welcome("I'm a welcome message!")
    logger.info("I'm an info message!")
    logger.debug("I'm a debug message!")
    logger.success("I'm a success message!")
    logger.warning("I'm a warning!")
    logger.error("I'm an error!")
    logger.sleep("I'm a sleep message!")
    logger.input("I'm an input message!")
    logger.ratelimit("I'm a rate limit message!")

    # Wait for 3 seconds using spinners
    logger.random_spinner_wait("Waiting for 3 seconds...", 3)

    # Wait for the user to input something to exit the program
    input("\nPress enter to exit...")
    logger.clear()
    exit()


if __name__ == "__main__":
    main()