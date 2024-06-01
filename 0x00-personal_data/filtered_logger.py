#!/usr/bin/env python3
"""
Module containing get_logger function and PII_FIELDS constant.
"""
import re
import logging
from logging import StreamHandler


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class for log records.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: tuple):
        """
        Initialize the RedactingFormatter with fields to redact.

        :param fields: Tuple of strings representing fields to redact.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record.

        :param record: The log record to format.
        :return: The formatted log message.
        """
        message = super().format(record)
        return self.filter_message(message)

    def filter_message(self, message: str) -> str:
        """
        Filter specified fields in the log message.

        :param message: The log message to filter.
        :return: The filtered log message.
        """
        for field in self.fields:
            message = re.sub(
                    fr'{field}=[^;]+', f'{field}={self.REDACTION}', message
                    )
        return message


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """
    Create and configure a logging.Logger object named "user_data".

    :return: The configured logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


if __name__ == "__main__":
    logger = get_logger()
    logger.info("This is a test log message with sensitive information.")
