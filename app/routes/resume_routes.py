#!/usr/bin/env python3
"""app/routes/resume_routes.py
"""
import os
from flask import Blueprint, current_app, send_file, session, render_template, flash, redirect, url_for
from app.forms import ResumeForm, DeleteForm
from app.models import Resume
from app.utils import db
from flask_login import current_user, login_required
from datetime import datetime
from weasyprint import HTML


resume_bp = Blueprint('resume', __name__)

@resume_bp.route('/resume/new', methods=['GET', 'POST'])
@login_required
def resume_form():
    form = ResumeForm()
    if form.validate_on_submit():
        resume = Resume(
            full_name=form.full_name.data,
            email=form.email.data,
            phone=form.phone.data,
            summary=form.summary.data,
            education=form.education.data,
            experience=form.experience.data,
            skills=form.skills.data,
            user_id=current_user.id
        )
        db.session.add(resume)
        db.session.commit()
        flash('Resume created successfully!', 'success')
        return redirect(url_for('resume.resume_preview', resume_id=resume.id))
    return render_template('resume_form.html', form=form, edit=False)


@resume_bp.route('/resume/<int:resume_id>/preview', methods=['GET'])
@login_required
def resume_preview(resume_id):
    resume = Resume.query.get_or_404(resume_id)
    if resume.user_id != current_user.id:
        flash('You do not have permission to view this resume.', 'danger')
        return redirect(url_for('main.dashboard'))
    return render_template('resume_preview.html', resume=resume, delete_form=DeleteForm())


@resume_bp.route('/resume/<int:resume_id>/edit', methods=['GET', 'POST'])
@login_required
def resume_edit(resume_id):
    resume = Resume.query.get_or_404(resume_id)
    if resume.user_id != current_user.id:
        flash('You do not have permission to edit this resume.', 'danger')
        return redirect(url_for('main.dashboard'))
    form = ResumeForm(obj=resume)
    if form.validate_on_submit():
        resume.full_name = form.full_name.data
        resume.email = form.email.data
        resume.phone = form.phone.data
        resume.summary = form.summary.data
        resume.education = form.education.data
        resume.experience = form.experience.data
        resume.skills = form.skills.data
        #resume.projects = form.projects.data
        db.session.commit()
        flash('Resume updated successfully!', 'success')
        return redirect(url_for('resume.resume_preview', resume_id=resume.id))
    return render_template('resume_form.html', form=form, edit=True, resume=resume)

@resume_bp.route('/resume/<int:resume_id>/download', methods=['GET'])
@login_required
def download_pdf(resume_id):
    resume = Resume.query.get_or_404(resume_id)
    if resume.user_id != current_user.id:
        flash('You do not have permission to download this resume.', 'danger')
        return redirect(url_for('main.dashboard'))
    # PDF generation logic
    rendered = render_template('resume_pdf.html', resume=resume)
    pdf_filename = f"resume_{resume.id}_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
    pdf_dir = os.path.join(current_app.root_path, 'generated_pdfs')
    os.makedirs(pdf_dir, exist_ok=True)
    pdf_path = os.path.join(pdf_dir, pdf_filename)

    HTML(string=rendered).write_pdf(pdf_path)

    if 'pdfs' not in session:
        session['pdfs'] = []
    session['pdfs'].append(pdf_filename)
    return send_file(pdf_path, as_attachment=True, download_name=pdf_filename)


@resume_bp.route('/resume/<int:resume_id>/delete', methods=['POST'])
@login_required
def resume_delete(resume_id):
    resume = Resume.query.get_or_404(resume_id)
    if resume.user_id != current_user.id:
        flash('You do not have permission to delete this resume.', 'danger')
        return redirect(url_for('main.dashboard'))
    db.session.delete(resume)
    db.session.commit()
    flash('Resume deleted successfully!', 'success')
    return redirect(url_for('main.dashboard'))
