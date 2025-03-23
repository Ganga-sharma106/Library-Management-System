<b>Library Management System:</b>
<br>
This Library Management System is built using Django and MySQL, allowing an admin to perform CRUD operations on books, manage authentication, and retrieve data.
<br><br>

<b>Prerequisites</b>
<br>
Before you begin, ensure you have met the following requirements:<br>
- Python 3.8+ installed on your system.<br>
- Django 3.x or 4.x installed (if not, it will be installed during the setup process).<br>

<b>#Features:</b>
<br>
Book Management: Create , Read ,Update , Delete .
<br><br>

<b>Installation & Setup</b> 
<br>
<b>1. Clone the Repository</b>
<br>
git clone https://github.com/Ganga-sharma106/Library-Management-System.git
<br>
cd Library-Management-System
<br><br>

<b>2. Configure Database (MySQL)</b><br>
DATABASES = {<br>
    'default': { <br>
        'ENGINE': 'django.db.backends.mysql',<br>
        'NAME': 'library_db',<br>
        'USER': 'library_usert',<br>
        'PASSWORD': 'lib@7980',<br>
        'HOST': 'localhost',<br>
        'PORT': '3306',<br>
    }
}<br>
<br><br>

<b>3. Run Migrations</b><br>
python manage.py makemigrations<br>
python manage.py migrate<br><br>

<b>4. Create a Superuser</b><br>
python manage.py createsuperuser<br>
username - Ganga_sharma<br>
Password - ganga1811<br>
Email - ganga1811@gmail.com<br><br>

<b>5. Access the Application:</b><br>
python manage.py runserver<br>
Admin Dashboard: http://localhost:8000/admin<br>
Go to  http://127.0.0.1:8000/admin/ or http://127.0.0.1:8000/api/signup/<br>
Username: Ganga_sharma<br>
Password: ganga1811<br><br>

