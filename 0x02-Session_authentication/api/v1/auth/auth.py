#!/usr/bin/env python3
"""Module for authentication"""
from flask import request
from typing import List, TypeVar


class Auth():
    """Module for aunthentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns True if the path is not in excluded_paths"""
        if path is not None and excluded_paths is not None:
            if path[-1] != "/":
                path = path + "/"
            if path in excluded_paths:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """validates all requests to secure the API"""
        if request is not None:
            dict_key = request.headers.get('Authorization')
            if dict_key is not None:
                return dict_key
        return None

    def current_user(self, requst=None) -> TypeVar('User'):
        """Validates all requests to secure the API"""
        return None
