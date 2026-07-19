import logging


# Show all logging levels
logging.basicConfig(level=logging.DEBUG)


# Create logger
logger = logging.getLogger(__name__)


# Different logging messages

logger.debug("This is a debug message")

logger.info("This is an info message")

logger.warning("This is a warning message")

logger.error("This is an error message")

logger.critical("This is a critical message")


# logger.log example

username = "example_username"
email = "example_email@mail.com"

logger.log(
    logging.WARNING,
    "Created user %s with email %s",
    username,
    email
)


# logger.exception example

try:
    answer = 9 / 0
    print(f"The answer is: {answer}")

except ZeroDivisionError:
    logger.exception("A divide by zero exception occurred")