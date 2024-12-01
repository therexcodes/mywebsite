# Therexcodes Portfolio Website

A personal portfolio website built using Django to showcase professional skills, services, and projects. It features a responsive design and includes a contact form to facilitate communication with visitors.

---

## Features

- **Portfolio Showcase**: Display of projects and achievements.
- **Contact Form**: A functional form for visitors to reach out directly.
- **Services Section**: Overview of offered services with details.
- **Responsive Design**: Optimized for all devices using HTML5, CSS, JavaScript, and Bootstrap.

---

## Tech Stack

- **Backend**: Django (v4.2.12)
- **Database**: PostgreSQL
- **Frontend**: HTML5, CSS, JavaScript, Bootstrap
- **Deployment**: Render (currently not working)

---

## Prerequisites

Ensure you have the following installed on your machine:

- Python 3.8 or later
- PostgreSQL
- pip (Python package manager)

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/therexcodes.git
   cd therexcodes
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**
   - Ensure PostgreSQL is running.
   - Create a database named `therexcodes` (or any preferred name).
   - Update the `DATABASES` section in `settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'therexcodes',
             'USER': 'your_postgres_user',
             'PASSWORD': 'your_postgres_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Website**
   - Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Dependencies

The project uses the following dependencies:

```
asgiref==3.8.1
dj-database-url==2.1.0
Django==4.2.12
gunicorn==22.0.0
packaging==24.0
pillow==10.3.0
psycopg2==2.9.9
sqlparse==0.5.0
typing_extensions==4.11.0
tzdata==2024.1
```

---

## Deployment

The website was deployed on Render, but the deployment is currently not active. To redeploy:

1. Push the repository to GitHub.
2. Create a new web service on Render.
3. Follow Render's Django deployment guide [here](https://render.com/docs/deploy-django).
