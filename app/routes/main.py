from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.forms import DeleteForm


main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Render the index page."""
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template('index.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    """Render the dashboard page."""
    resumes = current_user.resumes  # SQLAlchemy relationship to get user's resumes
    delete_form = DeleteForm()
    return render_template('dashboard.html', user=current_user, resumes=resumes, delete_form=delete_form)
