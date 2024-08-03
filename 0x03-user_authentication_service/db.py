#!/usr/bin/env python3
"""
DB module
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError, NoResultFound
from user import Base, User

class DB:
    """DB class to handle user data operations
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database

        Args:
            email (str): The email of the user
            hashed_password (str): The hashed password of the user

        Returns:
            User: The created User object
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Find a user by keyword arguments

        Args:
            **kwargs: Query parameters (e.g., email="example@example.com")

        Returns:
            User: The first matching User object

        Raises:
            NoResultFound: If no user matches the criteria
            InvalidRequestError: If the query arguments are invalid
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound("No user found with the given criteria.")
            return user
        except TypeError:
            raise InvalidRequestError("Invalid query arguments.")

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user's attributes

        Args:
            user_id (int): The ID of the user to update
            **kwargs: Attributes to update (e.g., email="new@example.com")

        Raises:
            ValueError: If an argument does not correspond to a user attribute
        """
        valid_attributes = {"email", "hashed_password", "session_id", "reset_token"}

        # Find the user by ID
        user = self.find_user_by(id=user_id)

        # Update user attributes
        for key, value in kwargs.items():
            if key not in valid_attributes:
                raise ValueError(f"Invalid attribute: {key}")
            setattr(user, key, value)

        # Commit the changes to the database
        self._session.commit()
