#!/usr/bin/env python3

"""
Module to check if a path requires authentication.
"""

from flask import request, Request
from typing import List, TypeVar, Optional


class Auth:
    """
    Class to manage API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if a path requires authentication.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]):
            Paths that don't require authentication.

        Returns:
            bool: True if authentication is required, False if not.
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

    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header from the Flask request.

        Args:
            request: Flask request object (default: None).

        Returns:
            str: None for now.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user from the Flask request.

        Args:
            request: Flask request object (default: None).

        Returns:
            TypeVar('User'): None for now.
        """
        return None
