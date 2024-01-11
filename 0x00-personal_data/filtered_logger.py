#!/usr/bin/env python3
"""
A module used for obfusaction of user data
"""
from typing import List
import re
import logging
import os
import mysql.connector


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, seperator: str) -> str:
    """
    Returns an obfuscated log message
    """
    for field in fields:
        message = re.sub(field+'=.*?'+seperator,
                         field+'='+redaction+seperator, message)
    return message
