# Payroll Management System

A full-stack web application designed to manage employee payrolls efficiently. This system allows HR/admins to handle employee details, attendance, salary generation, and payslip management in an organized and automated manner.

## 🛠️ Tech Stack

**Frontend:** React.js, HTML5, CSS3, Bootstrap / Tailwind  
**Backend:** Django (Python)  
**Database:** MySQL  
**API:** RESTful APIs (Django REST Framework)

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
bash
cd payroll-frontend
npm install
npm start

3. Backend Setup
bash
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
bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

🧪 Testing
You can test the features via:

Admin Panel: http://127.0.0.1:8000/admin/

Frontend: http://localhost:3000/

📁 Project Structure
perl
payroll-management-system/
├── payroll-frontend/    # React frontend code
├── payroll-backend/     # Django backend code
└── README.md

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.




