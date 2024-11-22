#!/usr/bin/env python3
"""Authentication file
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes the given password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The hashed password.
    """
    salt = bcrypt.gensalt()  # Generate a salt
    hashed_pass = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_pass
