#!/usr/bin/env python3

# app/routes/resume_routes.py

from flask import Blueprint, render_template

resume_bp = Blueprint('resume', __name__)

@resume_bp.route('/resume')
def resume_form():
    """Resume form."""
    return render_template('resume_form.html')
