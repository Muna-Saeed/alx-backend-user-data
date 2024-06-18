#!/usr/bin/env python3
""" creating a new authentication mechanism """

from api.v1.auth.basic_auth import Auth


class SessionAuth(Auth):
    """Session authentication class that inherits from Auth"""
    pass
