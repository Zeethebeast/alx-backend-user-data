#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views
from models.user import User  

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})

@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each object
    """
    stats = {
        'users': User.count()
    }
    return jsonify(stats)

@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def authorized_data():
    authorized = False
    if not authorized:
        abort(401, description="Unauthorized access")
    return jsonify(message="This is secure data.")

@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden():
    forbidden = False
    if not forbidden:
        abort(403, description="Forbidden access")
    return jsonify(message="This is secure data.")
