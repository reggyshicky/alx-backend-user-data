#!/usr/bin/env python3
"""
Definition of filter_datum function that returns an obsfuscated
log message
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, seperator: str) -> str:
    """Return an obfuscated log message"""
    for field in fields:
        message = re.sub(field+'=.*?'+seperator,
                         field+'='+redaction+seperator, message)
    return message
