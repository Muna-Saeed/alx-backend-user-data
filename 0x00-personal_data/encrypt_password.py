#!/usr/bin/env python3
"""
Module containing functions to hash and validate passwords using bcrypt.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Generate a salted, hashed password using bcrypt.

    :param password: The plaintext password to be hashed.
    :return: A salted, hashed password as a byte string.
    """
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate if a plaintext password matches a hashed password.

    :param hashed_password: The hashed password to be validated.
    :param password: The plaintext password to be checked.
    :return: True if the password matches the hashed password, False otherwise.
    """
    # Use bcrypt to check if the password matches the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
