#!/usr/bin/env python3
"""
Module containing RedactingFormatter class for log formatting.
"""

import logging
import re
from typing import List


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class for log records.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the RedactingFormatter with fields to redact.

        :param fields: List of strings representing fields to redact.
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
