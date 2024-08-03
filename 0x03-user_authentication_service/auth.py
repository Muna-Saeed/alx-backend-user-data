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

    def register_user(self, email: str, password: str) -> User:
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

    def create_session(self, email: str) -> str:
        """Creates a session for the user and returns the session ID."""
        try:
            user = self._db.find_user_by(email=email)
            session_id = str(uuid.uuid4())
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Find user by session ID."""
        if session_id is None:
            return None

        # Find user by session ID
        user = self._db.find_user_by_session_id(session_id)
        return user

    def destroy_session(self, user_id: int) -> None:
        """Destroy the session of the user with the given user_id."""
        # Update the user's session ID to None
        self._db.update_user_session(user_id, None)

    def get_reset_password_token(self, email: str) -> str:
        """Generates a reset password token
         for the user with the given email."""
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user_reset_token(email, reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError("User not found")

    def update_password(self, reset_token: str, new_password: str) -> None:
        """
        Update the user's password using the reset token.

        Args:
            reset_token (str): The reset token for password reset
            new_password (str): The new password to set

        Raises:
            ValueError: If the reset token is invalid or no user is found
        """
        try:
            user = self._db.find_user_by_reset_token(reset_token)
            if user is None:
                raise ValueError("Invalid reset token")

            hashed_password = _hash_password(new_password)
            self._db.update_user(
              user.id, hashed_password=hashed_password, reset_token=None)
        except NoResultFound:
            raise ValueError("Invalid reset token")
