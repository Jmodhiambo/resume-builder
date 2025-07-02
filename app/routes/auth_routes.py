#!/usr/bin/env python3
"""Log in page."""

# app/routes/auth_routes.py

from flask import Blueprint, render_template, redirect, url_for

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login')
def login():
    """Log in page."""
    return render_template('login.html')
