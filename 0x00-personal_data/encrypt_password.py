#!/usr/bin/env python3
"""
Module containing hash_password function to securely hash passwords.
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
