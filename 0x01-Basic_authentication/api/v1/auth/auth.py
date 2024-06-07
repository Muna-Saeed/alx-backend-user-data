#!/usr/bin/env python3
""" Auth module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class to manage API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines if authentication is required """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        # Ensure path ends with a slash for comparison
        if not path.endswith('/'):
            path += '/'
        for ep in excluded_paths:
            if ep.endswith('/') and ep == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Returns the value of the Authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns the current user """
        return None
