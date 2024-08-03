#!/usr/bin/env python3
"""
Hash password
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hash a password with bcrypt

    Args:
        password (str): The password to hash

    Returns:
        bytes: The hashed password
    """
    # Convert password to bytes if it's not already
    password_bytes = password.encode('utf-8')

    # Generate a salt and hash the password
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    return hashed_password
