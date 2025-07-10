# Payroll Management System

A full-stack web application designed to manage employee payrolls efficiently. This system allows HR/admins to handle employee details, salary generation, and payslip management in an organized and automated manner.

# 🚀 Deployment Links

🔗 https://payroll-system-jp4s.onrender.com

🔐 Test Credentials

username-ruksana

password-sharuk@14

🔗 https://payroll-system-jp4s.onrender.com/admin/ ( to add new users and manage permissions)

## 🛠️ Tech Stack

**Frontend:** React.js, HTML5, CSS3, Bootstrap  
**Backend:** Django (Python)  
**Database:** MySQL  
**API:** RESTful APIs (Django REST Framework) 
**Deployment:** Render.com, Whitenoise

## 📌 Features

- 🧑‍💼 Employee Management (Add, Edit, Delete)
- 💰 Salary Calculation
- 📄 Payslip Generation & Download
- 🔐 Admin Login Authentication
- 📊 Dashboard with Key Metrics
- 🗂 Department and Role Management


## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/syedruksana34/payroll-management-system.git

2. Frontend Setup

cd payroll-frontend
npm install
npm start

3. Backend Setup

cd payroll-backend
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py runserver

4. MySQL Configuration
Create a MySQL database (e.g. payroll_db)
Update database settings in payroll_project/settings.py

python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'payroll_db',
        'USER': 'ruksana',
        'PASSWORD': 'sharuk@14',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5. Migrate and Create Superuser

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

🧪 Testing
You can test the features via:

Admin Panel: http://127.0.0.1:8000/admin/

Frontend: http://localhost:3000/

📁 Project Structure

payroll-management-system/
├── payroll-frontend/    # React frontend code
├── payroll-backend/     # Django backend code
└── README.md

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.




