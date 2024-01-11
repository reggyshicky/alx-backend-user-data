#!/usr/bin/env python3
"""
Defines a hash_password function to return a hashed
password
"""
import bcrypt
from bcrypt import hashpw


def hash_password(password: str) -> bytes:
    """
    Returns a hashed password
    """
    b = password.encode()
    hashed = hashpw(b, bcrypt.gensalt())
    return hashed
