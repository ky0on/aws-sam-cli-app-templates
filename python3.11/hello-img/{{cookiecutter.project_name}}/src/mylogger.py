import os
import logging
import logging.handlers


def setup_logger(module_name):
    logger = logging.getLogger(module_name)
    logger.handlers.clear()

    logger.propagate = False  # To avoid duplicate logs on AWS

    default_log_level = "DEBUG"
    log_level_env = os.getenv("LogLevel", default_log_level).upper()
    log_level = logging.DEBUG if log_level_env == "DEBUG" else logging.INFO

    formatter = logging.Formatter(
        # "%(asctime)s [%(levelname)s] (%(filename)s | %(funcName)s | l%(lineno)s) %(message)s"
        "[%(levelname)s] (%(filename)s | %(funcName)s | L%(lineno)s) %(message)s"
    )

    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    streamHandler.setLevel(log_level)

    logger.setLevel(log_level)
    logger.addHandler(streamHandler)

    log_file = os.getenv("LogFile", False)
    if log_file:
        print("FileHandler is activated.")
        fileHandler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=10**6,
            backupCount=5,
        )
        fileHandler.setFormatter(formatter)
        fileHandler.setLevel(log_level)
        logger.addHandler(fileHandler)

    return logger


if __name__ == "__main__":
    logger = setup_logger(__name__)
    logger.info("info")
    logger.debug("debug")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")
