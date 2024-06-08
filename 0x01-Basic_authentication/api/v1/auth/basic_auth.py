#!/usr/bin/env python3
""" BasicAuth module for the API
"""
from api.v1.auth.auth import Auth
import base64
from models.base import Base
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth class for API authentication """

    def extract_base64_authorization_header(
            self, authorization_header: str
            ) -> str:
        """ Extracts the Base64 part of the Authorization header """
        if authorization_header is None or not isinstance(
                authorization_header, str
                ):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
            ) -> str:
        """ Decodes the Base64 part of the Authorization header """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str
                ):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
            ) -> Tuple[str, str]:
        """ Extracts user credentials from the Base64 decoded value """
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str
                ):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        user_email, user_password =
        decoded_base64_authorization_header.split(':', 1)
        return user_email, user_password
