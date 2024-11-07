#!/usr/bin/env python3
"""
This module provides a function to filter out sensitive Personally Identifiable
Information (PII) fields from a message by replacing them with a redacted value.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Replaces the value of specified PII fields in a message with a redacted
    placeholder.

    Args:
        fields (list of str): List of PII field names to be redacted.
        redaction (str): The replacement text for each PII field.
        message (str): The input message containing PII data.
        separator (str): The character that separates each field in the message.

    Returns:
        str: The message with specified PII fields redacted.
    """
    for fd in fields:
        message = re.sub(
            f'{fd}=.*?{separator}',
            f'{fd}={redaction}{separator}',
            message
        )
    return message
