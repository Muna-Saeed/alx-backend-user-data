#!/usr/bin/env python3
""" creating a new authentication mechanism """

from api.v1.auth.basic_auth import Auth


class SessionAuth(Auth):
    """Session authentication class that inherits from Auth
       to manage session authentication. """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a session ID for a user_id. """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id
