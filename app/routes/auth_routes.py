#!/usr/bin/env python3
"""Log in page."""
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models import User, db
from app.forms import RegistrationForm, LoginForm, DeleteForm


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Register a new user."""
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Log in page."""
    form = LoginForm()
    delete_form = DeleteForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            print('next_page:', next_page)
            return redirect(next_page) if next_page else redirect(url_for('main.dashboard', delete_form=delete_form))
        else:
            flash('Invalid credentials', 'danger')
    else:
        print(form.errors)
    return render_template('login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    """Log out the user."""
    logout_user()
    return redirect(url_for('main.index'))
