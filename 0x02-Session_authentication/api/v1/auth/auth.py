#!/usr/bin/env python3
""" Auth module for the API
"""
from flask import request
from typing import List, TypeVar
import fnmatch as fn


class Auth:
    """ Auth class to manage API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines if authentication is required """
        if path is None:
            return True
        if not excluded_paths:
            return True
        if any(fn.fnmatch(path, s) for s in excluded_paths):
            return False
        # Ensure path ends with a slash for comparison
        if path in excluded_paths:
            return False
        if path + '/' in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Returns the value of the Authorization header """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns the current user """
        return None
