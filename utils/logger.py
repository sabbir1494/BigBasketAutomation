import logging
import os


class Logger:

    @staticmethod
    def get_logger(name):

        log_directory = "logs"

        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        logger = logging.getLogger(name)

        if logger.hasHandlers():
            return logger

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        file_handler = logging.FileHandler(
            os.path.join(log_directory, "automation.log")
        )

        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger