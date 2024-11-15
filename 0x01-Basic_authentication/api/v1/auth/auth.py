#!/usr/bin/env python3
Module for API authentication management.

This module contains the Auth class, which provides methods for managing
authentication in a Flask API, including checking required authentication
and retrieving the current user.
"""

from flask import request, Request
from typing import List, TypeVar, Optional

class Auth:
    """
    Auth class to manage API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a given path requires authentication.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list of paths that do not require authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
                  Returns True if path is None, or excluded_paths is None or empty.
                  Returns False if path is in excluded_paths (slash-tolerant).
        """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True

        new_path = path.rstrip('/')

        for excluded_path in excluded_paths:
            if excluded_path.rstrip('/') == new_path:
                return False
        return True

    def authorization_header(self, flask_request: Optional[Request] = None) -> str:
        """
        Retrieves the authorization header from the Flask request object.

        Args:
            flask_request: The Flask request object (default: None).

        Returns:
            str: None for now; logic to be implemented later.
        """
        return None

    def current_user(self, flask_request: Optional[Request] = None) -> Optional[TypeVar('User')]:
        """
        Retrieves the current user from the Flask request object.

        Args:
            flask_request: The Flask request object (default: None).

        Returns:
            TypeVar('User'): None for now; logic to be implemented later.
        """
        return None
