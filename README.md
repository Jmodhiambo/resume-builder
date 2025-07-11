# 🧾 Flask Resume Builder

A clean and user-friendly web application for creating, previewing, and downloading professional resumes. Built with **Python** and **Flask**, it follows modular best practices and a clean code architecture.

---

## 🚀 Features

- ✅ User registration and authentication  
- 🧾 Dynamic resume form (Personal Info, Education, Experience, Skills, etc.)  
- 👀 Real-time resume preview on the web  
- 📄 Download resumes as styled PDF  
- 📱 Fully responsive design using Bootstrap 5  

---

## 📦 Tech Stack

| Layer         | Technology              |
|---------------|--------------------------|
| Backend       | Flask, Python, SQLAlchemy |
| Frontend      | Jinja2, Bootstrap 5       |
| Forms         | Flask-WTF, WTForms        |
| Database      | PostgreSQL                |
| PDF Export    | WeasyPrint                |
| Auth & Session| Flask-Login               |

---

## 🧭 How It Works

1. User visits the home page and registers or logs in.  
2. After login, they're redirected to the **dashboard**.  
3. From the dashboard, users launch the **Resume Builder**:
   - Fill in forms for Personal Info, Education, Experience, Skills, etc.
   - Preview the resume in real-time.
   - Click “Download as PDF” to export the resume.
4. (Optional) Users may select from different resume templates, save sessions, or share resumes online.

---

## 🏗️ Project Structure

```
resume_builder/
│
├── app/
│   ├── __init__.py          # App factory setup
│   ├── models.py            # SQLAlchemy models
│   ├── forms.py             # WTForms definitions
│   ├── routes/              # Route blueprints
│   ├── templates/           # Jinja2 HTML templates
│   ├── static/              # CSS, JS, and assets
│   └── utils/               # Helper functions
│
├── config.py                # Configuration settings
├── requirements.txt         # Project dependencies
├── run.py                   # App entry point
└── README.md                # Project documentation
```

---

## 🧪 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Jmodhiambo/resume-builder.git
cd resume-builder
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt

# Setup postgresql
# populate .env with the following
PG_USER=admin
PG_PASS=random-password
PG_DB=resume_db
PG_HOST=localhost

# Make sure setup.sh is executable
./setup.sh
# Check for outputs for any errors.
```

### 4. Run the application

```bash
flask run
```

> ℹ️ The app will be available at `http://127.0.0.1:5000`

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

Created with by [Lincoln Mihigo](https://github.com/LinMihigo) and [Martin Odhiambo](https://github.com/Jmodhiambo).
For questions or feedback, feel free to reach out via GitHub Issues.
