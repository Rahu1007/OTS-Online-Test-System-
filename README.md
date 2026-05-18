# Online Testing System (OTS) 📝

A simple and user-friendly **Online Testing System** built with Django. This web application allows students to register, login, take tests, and view their test results and history.

---

## ⚡ Quick Start (How to Run)

Follow these simple steps to run the project immediately:

1. **Open Command Prompt/Terminal** and navigate to the project directory:
   ```bash
   cd "C:\Users\RAHUL SHARMA\Downloads\myproject"
   ```

2. **Activate the Virtual Environment**:
   - For Windows:
     ```bash
     .\.venv\Scripts\activate
     ```
   - For Mac/Linux:
     ```bash
     source .venv/bin/activate
     ```

3. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

4. **Open in your Web Browser**:
   - Main Application: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

*(For full setup from scratch, see the [Installation Guide](#-installation-guide) below.)*

---

## 🌟 Features

- **User Registration**: New students can create an account
- **User Login**: Secure login system for registered users
- **Take Tests**: Students can attempt multiple-choice questions
- **View Results**: See test scores immediately after completing a test
- **Test History**: View all previous test attempts and scores
- **Admin Panel**: Manage questions, users, and results through Django admin

---

## 🛠️ Technologies Used

- **Backend**: Django 5.2 (Python Web Framework)
- **Database**: SQLite (default Django database)
- **Frontend**: HTML, CSS
- **Language**: Python 3.x

---

## 📋 Prerequisites

Before you start, make sure you have the following installed on your computer:

1. **Python** (version 3.8 or higher)
   - Download from: https://www.python.org/downloads/
   - During installation, check "Add Python to PATH"

2. **pip** (Python package manager - comes with Python)

3. **Virtual Environment** (recommended)

---

## 🚀 Installation Guide

Follow these steps carefully to set up the project on your computer:

### Step 1: Download the Project

Download or clone this project to your computer.

### Step 2: Open Command Prompt/Terminal

- **Windows**: Press `Win + R`, type `cmd`, and press Enter
- **Mac/Linux**: Open Terminal

### Step 3: Navigate to Project Folder

```bash
cd C:\Users\RAHUL SHARMA\Downloads\myproject
```

**Note**: Replace the path with your actual project location.

### Step 4: Create Virtual Environment (Recommended)

A virtual environment keeps your project dependencies separate from other Python projects.

```bash
python -m venv venv
```

**What this does**: Creates a folder named `venv` with an isolated Python environment.

### Step 5: Activate Virtual Environment

**For Windows:**
```bash
venv\Scripts\activate
```

**For Mac/Linux:**
```bash
source venv/bin/activate
```

**How to know it worked**: You'll see `(venv)` at the beginning of your command line.

### Step 6: Install Django

```bash
pip install django
```

**What this does**: Installs the Django framework needed to run the project.

### Step 7: Install Other Dependencies (if any)

```bash
pip install -r requirements.txt
```

**Note**: If you get an error saying "requirements.txt not found", skip this step.

---

## 🗄️ Database Setup

### Step 8: Apply Database Migrations

Migrations create the necessary database tables for your application.

```bash
python manage.py makemigrations
```

**What this does**: Creates migration files based on your models.

```bash
python manage.py migrate
```

**What this does**: Applies the migrations and creates database tables.

---

## 👤 Create Admin User

### Step 9: Create a Superuser Account

This account lets you access the admin panel to add questions and manage users.

```bash
python manage.py createsuperuser
```

**You'll be asked to enter:**
- Username (e.g., admin)
- Email address (optional, you can skip by pressing Enter)
- Password (type carefully, it won't show on screen)
- Password confirmation (type the same password again)

---

## ▶️ Running the Application

### Step 10: Start the Development Server

```bash
python manage.py runserver
```

**What this does**: Starts the Django development server.

**You should see output like:**
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Step 11: Open the Application in Browser

Open your web browser and go to:

- **Main Application**: http://127.0.0.1:8000/OTS/
- **Admin Panel**: http://127.0.0.1:8000/admin/

---

## 📚 How to Use the Application

### For Students:

1. **Register**: 
   - Go to http://127.0.0.1:8000/OTS/new-candidate/
   - Fill in username, password, and name
   - Click "Register"

2. **Login**:
   - Go to http://127.0.0.1:8000/OTS/login/
   - Enter your username and password
   - Click "Login"

3. **Take a Test**:
   - After login, click "Start Test"
   - Answer the questions
   - Submit the test

4. **View Results**:
   - See your score immediately after submitting
   - View test history to see all previous attempts

5. **Logout**:
   - Click "Logout" when you're done

### For Admin:

1. **Login to Admin Panel**:
   - Go to http://127.0.0.1:8000/admin/
   - Enter superuser credentials you created earlier

2. **Add Questions**:
   - Click on "Questions"
   - Click "Add Question"
   - Fill in:
     - Question text
     - Option A, B, C, D
     - Correct answer (a, b, c, or d)
   - Click "Save"

3. **Manage Users**:
   - Click on "Candidates" to view all registered users
   - View or edit user information

4. **View Results**:
   - Click on "Results" to see all test results

---

## 📁 Project Structure

```
myproject/
│
├── OTS/                          # Main application folder
│   ├── migrations/               # Database migration files
│   ├── static/                   # CSS, JavaScript, images
│   │   ├── login.css
│   │   ├── registration.css
│   │   └── result.css
│   ├── templates/                # HTML templates
│   │   ├── welcome.html          # Welcome page
│   │   ├── login.html            # Login page
│   │   ├── registrationForm.html # Registration form
│   │   ├── registration.html     # Registration success page
│   │   ├── home.html             # Student dashboard
│   │   ├── test_paper.html       # Test page
│   │   ├── result.html           # Test result page
│   │   └── test_history.html     # Test history page
│   ├── admin.py                  # Admin panel configuration
│   ├── models.py                 # Database models
│   ├── views.py                  # View functions (logic)
│   └── urls.py                   # URL routing
│
├── myproject/                    # Project settings folder
│   ├── settings.py               # Django settings
│   ├── urls.py                   # Main URL configuration
│   └── wsgi.py                   # WSGI configuration
│
├── db.sqlite3                    # SQLite database file
├── manage.py                     # Django management script
└── README.md                     # This file
```

---

## 🔗 URL Routes

Here are all the available URLs in the application:

| URL | Purpose | Access |
|-----|---------|--------|
| `/OTS/` | Welcome page | Everyone |
| `/OTS/new-candidate/` | Registration form | Everyone |
| `/OTS/store-candidate/` | Process registration | System |
| `/OTS/login/` | Login page | Everyone |
| `/OTS/home/` | Student dashboard | Logged-in users |
| `/OTS/test-paper/?n=10` | Test with 10 questions | Logged-in users |
| `/OTS/calculate-result/` | Calculate test score | System |
| `/OTS/result/` | View latest result | Logged-in users |
| `/OTS/test-history/` | View all test attempts | Logged-in users |
| `/OTS/logout/` | Logout | Logged-in users |
| `/admin/` | Admin panel | Admin only |

---

## 🎯 Database Models

### 1. Candidate (User)
- **username**: Unique username (Primary Key)
- **password**: User password
- **name**: Full name
- **email**: Email address
- **test_attempted**: Number of tests taken
- **points**: Average score

### 2. Question
- **qid**: Question ID (Auto-generated)
- **que**: Question text
- **a, b, c, d**: Four options
- **ans**: Correct answer (a/b/c/d)

### 3. Result
- **resultid**: Result ID (Auto-generated)
- **username**: Link to Candidate
- **date**: Test date
- **time**: Test time
- **attempt**: Questions attempted
- **right**: Correct answers
- **wrong**: Wrong answers
- **points**: Score obtained

---

## 🔧 Common Commands

### Check Django Version
```bash
python -m django --version
```

### Create a New App
```bash
python manage.py startapp app_name
```

### Make Migrations (after model changes)
```bash
python manage.py makemigrations
python manage.py migrate
```

### Run Server
```bash
python manage.py runserver
```

### Run Server on Different Port
```bash
python manage.py runserver 8080
```

### Run Server on Different IP
```bash
python manage.py runserver 0.0.0.0:8000
```

### Open Django Shell (Python interactive shell)
```bash
python manage.py shell
```

### Create Superuser
```bash
python manage.py createsuperuser
```

### Collect Static Files (for production)
```bash
python manage.py collectstatic
```

### Clear Database (Delete db.sqlite3 and recreate)
```bash
# Delete db.sqlite3 file manually, then run:
python manage.py migrate
python manage.py createsuperuser
```

---

## 🐛 Troubleshooting

### Problem 1: "python is not recognized"
**Solution**: Python is not installed or not added to PATH
- Reinstall Python and check "Add Python to PATH" during installation

### Problem 2: "No module named django"
**Solution**: Django is not installed
```bash
pip install django
```

### Problem 3: Port already in use
**Solution**: Another application is using port 8000
```bash
python manage.py runserver 8080
```

### Problem 4: "Table doesn't exist"
**Solution**: Run migrations
```bash
python manage.py migrate
```

### Problem 5: Can't login to admin
**Solution**: Create superuser again
```bash
python manage.py createsuperuser
```

### Problem 6: Static files not loading
**Solution**: Check STATIC_URL in settings.py
```python
STATIC_URL = 'static/'
```

---

## 📝 How to Add Questions

### Method 1: Using Admin Panel (Recommended)

1. Start the server: `python manage.py runserver`
2. Go to: http://127.0.0.1:8000/admin/
3. Login with superuser credentials
4. Click on "Questions" → "Add Question"
5. Fill in the question and options
6. Save

### Method 2: Using Django Shell

```bash
python manage.py shell
```

Then in the shell:
```python
from OTS.models import Question

# Create a new question
q = Question()
q.que = "What is the capital of France?"
q.a = "London"
q.b = "Paris"
q.c = "Berlin"
q.d = "Madrid"
q.ans = "b"
q.save()

# Exit shell
exit()
```

---

## 🔒 Security Notes

⚠️ **Important for Production:**

1. **Change SECRET_KEY** in `settings.py`
2. **Set DEBUG = False** in `settings.py`
3. **Add allowed hosts** in `ALLOWED_HOSTS`
4. **Use environment variables** for sensitive data
5. **Use a proper database** (PostgreSQL, MySQL) instead of SQLite
6. **Hash passwords properly** (Django does this by default)
7. **Use HTTPS** in production

---

## 📦 Creating requirements.txt

To create a list of all installed packages:

```bash
pip freeze > requirements.txt
```

To install from requirements.txt:

```bash
pip install -r requirements.txt
```

---

## 🚀 Deploying to Vercel

This project includes configuration files for easy deployment to Vercel.

### Prerequisites

1. **GitHub Account** - Your code should be on GitHub
2. **Vercel Account** - Sign up at https://vercel.com (free)

### Deployment Steps

#### Step 1: Push to GitHub

Make sure all your code is pushed to GitHub:

```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

#### Step 2: Import Project to Vercel

1. Go to https://vercel.com/dashboard
2. Click "Add New" → "Project"
3. Import your GitHub repository
4. Vercel will automatically detect the configuration

#### Step 3: Configure Environment Variables (Optional)

For production, add these environment variables in Vercel:

- `SECRET_KEY` - Your Django secret key
- `DEBUG` - Set to `False`
- `DATABASE_URL` - If using external database

#### Step 4: Deploy

Click "Deploy" and Vercel will:
- Install dependencies from `requirements.txt`
- Run migrations
- Collect static files
- Deploy your application

### Configuration Files Included

- **vercel.json** - Vercel deployment configuration
- **requirements.txt** - Python dependencies
- **index.py** - Vercel entry point
- **build.sh** - Build script for migrations

### Important Notes for Vercel Deployment

⚠️ **Database Limitation**

SQLite doesn't work well on Vercel (serverless environment). For production:

1. **Use PostgreSQL** (recommended):
   - Sign up for free PostgreSQL at https://neon.tech or https://supabase.com
   - Add database URL to Vercel environment variables
   - Update `settings.py`:

```python
import os
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}
```

2. **Install dj-database-url**:
```bash
pip install dj-database-url psycopg2-binary
```

⚠️ **Security Settings**

Update `settings.py` for production:

```python
import os

# Use environment variables
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Update ALLOWED_HOSTS with your Vercel domain
ALLOWED_HOSTS = [
    'your-app.vercel.app',
    'localhost',
    '127.0.0.1'
]
```

### Accessing Your Deployed App

After deployment, your app will be available at:
- `https://your-app-name.vercel.app/OTS/`

### Redeploying After Changes

```bash
git add .
git commit -m "Your changes"
git push origin main
```

Vercel will automatically redeploy!

---

## 🤝 Contributing

If you want to improve this project:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## 📄 License

This project is open-source and available for educational purposes.

---

## 👨‍💻 Developer

**Rahul Sharma**

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the Troubleshooting section above
2. Review Django documentation: https://docs.djangoproject.com/
3. Search for solutions on Stack Overflow

---

## 🎓 Learning Resources

- **Django Official Tutorial**: https://docs.djangoproject.com/en/stable/intro/tutorial01/
- **Python Documentation**: https://docs.python.org/3/
- **W3Schools Django**: https://www.w3schools.com/django/

---

## ✅ Quick Start Checklist

- [ ] Python installed
- [ ] Virtual environment created and activated
- [ ] Django installed
- [ ] Migrations applied
- [ ] Superuser created
- [ ] Questions added via admin panel
- [ ] Server running
- [ ] Application accessible in browser

---

**Happy Testing! 🎉**

---

*Last Updated: December 2025*
