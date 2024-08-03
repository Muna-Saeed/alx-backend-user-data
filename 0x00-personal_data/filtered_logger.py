#!/usr/bin/env python3
"""
Module containing get_logger function and PII_FIELDS constant.
"""
import re
import logging
import mysql.connector
import os
from logging import StreamHandler
from typing import List, Tuple


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    """
    Obfuscate specified fields in the log message.

    :param fields: List of field names to obfuscate.
    :param redaction: String to replace the field values with.
    :param message: The log message containing the fields.
    :param separator: The character that separates fields in the log message.
    :return: The obfuscated log message.
    """
    pattern = '|'.join([f'(?<={field}=)[^{separator}]*' for field in fields])
    return re.sub(pattern, redaction, message)


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connect to the database using credentials from environment variables.

    :return: A MySQLConnection object representing the database connection.
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )


def main():
    """
    Read and filter data from the users table in the database.
    Retrieve all rows from the users table and
    display each row under a filtered format.
    """
    logger = logging.getLogger("user_data")
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    for row in cursor:
        filtered_row = {
          key: "***" if key in ["name", "email", "phone", "ssn", "password"]
          else value for key, value in zip(cursor.column_names, row)}
        logger.info(filtered_row)
    cursor.close()
    db.close()
