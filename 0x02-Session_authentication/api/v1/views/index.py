#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Blueprint
from flask import jsonify
from api.v1.views import app_views

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.session_auth import *

User.load_from_file()

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Return status"""
    return jsonify({"status": "OK"})
