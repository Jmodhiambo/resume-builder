# Flask Resume Builder 🧾

A simple and elegant web application for creating, previewing, and downloading professional resumes. Built with Python, Flask, and a clean, modular architecture.

## 🚀 Features

- User registration and login
- Dynamic resume form input
- Resume preview before download
- PDF generation from styled HTML templates
- Lightweight, clean UI (Bootstrap 5)

## 📦 Tech Stack

- **Backend**: Flask, Python 3
- **Frontend**: Jinja2, HTML5, Bootstrap 5
- **Database**: SQLite (or PostgreSQL)
- **Forms**: Flask-WTF
- **PDF Export**: WeasyPrint / ReportLab
- **Auth**: Flask-Login

## 🏗️ Project Structure

Follows a modular design with Blueprints for authentication and resume functionality. Clean separation of concerns for better maintainability and testing.

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Jmodhiambo/resume-builder.git
   cd resume-builder ```

2. File Structure
<pre><code>

resume_builder/
│
├── app/
│   ├── __init__.py             # App factory setup
│   ├── models.py               # SQLAlchemy models
│   ├── forms.py                # Flask-WTF forms
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth_routes.py      # Login, register
│   │   └── resume_routes.py    # Resume form, preview, download
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   ├── resume_form.html
│   │   └── resume_preview.html
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── resume_templates/   # For styled HTML templates
│   └── utils/
│       └── pdf_generator.py    # Resume PDF logic
│
├── config.py                   # Configuration settings
├── requirements.txt            # Dependencies
├── run.py                      # App entry point
└── README.md                   # Project overview
</code></pre>
