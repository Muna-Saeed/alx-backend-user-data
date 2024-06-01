#!/usr/bin/env python3
"""
This module provides a function to obfuscate specified fields in log messages.
"""

import re
from typing import List


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
