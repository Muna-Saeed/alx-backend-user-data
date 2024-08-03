#!/usr/bin/env python3
"""
Hash password
"""

import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


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


def _generate_uuid() -> str:
    """Generates a new UUID."""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(email: str, password: str) -> User:
        """
        Register a new user with email and password.

        Args:
            email (str): The email of the user
            password (str): The password of the user

        Returns:
            User: The created User object

        Raises:
            ValueError: If the user with the given email already exists
        """
        # Check if a user with the given email already exists
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # Hash the password
            hashed_password = _hash_password(password)
            # Add the user to the database
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Validates login credentials."""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                    password.encode('utf-8'), user.hashed_password
                    )
        except NoResultFound:
            return False
