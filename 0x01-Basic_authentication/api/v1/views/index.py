#!/usr/bin/env python3
"""
Module of Index views for the API.

This module provides endpoints to check the status of the API, retrieve
statistics on objects, and simulate error responses for unauthorized
and forbidden access.

Routes:
    /status (GET): Returns a JSON response with the API status.
    /stats (GET): Returns a JSON response with statistics on various objects.
    /unauthorized (GET): Simulates an endpoint requiring authorization and
        returns a 401 Unauthorized error if access is denied.
    /forbidden (GET): Simulates a restricted endpoint and returns a
        403 Forbidden error if access is restricted.
"""

from flask import jsonify, abort
from api.v1.views import app_views
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """
    GET /api/v1/status
    Check the status of the API.

    Returns:
        JSON: A JSON response indicating the API status.
    Example:
        {
            "status": "OK"
        }
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """
    GET /api/v1/stats
    Retrieve statistics about the objects managed by the API.

    Returns:
        JSON: A JSON object containing the count of each type of object.
    Example:
        {
            "users": 45
        }
    """
    stats = {
        'users': User.count()
    }
    return jsonify(stats)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def authorized_data():
    """
    GET /api/v1/unauthorized
    Simulate an endpoint that requires user authorization.

    If the user is not authorized, returns a 401 Unauthorized error.

    Returns:
        JSON: A JSON response with an error message for unauthorized access.
    Example:
        {
            "error": "Unauthorized access"
        }
    """
    authorized = False
    if not authorized:
        abort(401, description="Unauthorized access")
    return jsonify(message="This is secure data.")


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden():
    """
    GET /api/v1/forbidden
    Simulate an endpoint that is restricted to certain users.

    If access is forbidden, returns a 403 Forbidden error.

    Returns:
        JSON: A JSON response with an error message for forbidden access.
    Example:
        {
            "error": "Forbidden access"
        }
    """
    forbidden = False
    if not forbidden:
        abort(403, description="Forbidden access")
    return jsonify(message="This is secure data.")
