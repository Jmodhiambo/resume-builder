# ── Reusable Subforms ─────────────────────────────

from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, TextAreaField, SubmitField, FormField, FieldList
)
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])  # <-- Add this line
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])  # <-- Add this line
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class EducationForm(FlaskForm):
    institution = StringField('Institution', validators=[DataRequired(), Length(max=100)])
    degree = StringField('Degree / Program', validators=[DataRequired(), Length(max=100)])
    year = StringField('Year Completed', validators=[DataRequired(), Length(max=10)])

class ExperienceForm(FlaskForm):
    company = StringField('Company', validators=[DataRequired(), Length(max=100)])
    role = StringField('Role / Position', validators=[DataRequired(), Length(max=100)])
    duration = StringField('Duration', validators=[DataRequired(), Length(max=50)])

# ── Main Resume Form ──────────────────────────────
class ResumeForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=7, max=20)])
    summary = TextAreaField('About Me / Summary', validators=[Length(max=500)])

    education = FieldList(FormField(EducationForm), min_entries=1, max_entries=5)
    experience = FieldList(FormField(ExperienceForm), min_entries=1, max_entries=5)
    skills = TextAreaField('Skills (comma-separated)', validators=[Length(max=300)])
    submit = SubmitField('Preview Resume')


class DeleteForm(FlaskForm):
    submit = SubmitField('Delete')
