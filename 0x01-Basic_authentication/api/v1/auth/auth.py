#!/usr/bin/env python3
from flask import request
from typing import List, TypeVar

class Auth():
    """Module for aunthentication"""
    
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return False
    
    def authorization_header(self, request=None) -> str:
        return None
    
    def current_user(self, requst=None) -> TypeVar('User'):
        return None