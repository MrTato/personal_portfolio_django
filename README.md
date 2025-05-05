# 🛠️ Django Backend for Personal Portfolio

This is the backend API for my personal portfolio site. Built with **Django** and **Django REST Framework**, it serves blog content to a Vue 3 frontend. The backend is read-only for the public and fully managed via the Django Admin panel. It is designed to be lightweight, secure, and easy to maintain.

---

## 🚀 Features

- 📝 **Blog API**  
  - Markdown-based content storage (rendered client-side)  
  - Draft support via `is_published` field  
  - Comment system planned (not yet implemented)  
  - No authentication or admin endpoints — only public `GET` endpoints

- 📃 **OpenAPI Schema**  
  - Exposed via [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/)  
  - Accessible at `/swagger/` and `/redoc/`

- 🌐 **CORS Enabled**  
  - Configured for safe interaction with the Vue frontend  

- 📦 **Hosted on Render**  
  - Managed PostgreSQL database  
  - Automatic deployment on `git push`  
  - Static files served via Django

---

## 🛠 Tech Stack

### 🔹 Core
- [Django 5.x](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [drf-spectacular](https://drf-spectacular.readthedocs.io/)
- [PostgreSQL](https://www.postgresql.org/)

### 🔹 Middleware
- [WhiteNoise](https://whitenoise.evans.io/) for static file handling
- [django-cors-headers](https://pypi.org/project/django-cors-headers/)

---

## ⚙️ Setup Instructions

### 🧱 Prerequisites

- Python 3.13.2  
- PostgreSQL database  
- `virtualenv` installed

### ▶️ Local Development

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the server:
   ```bash
   python manage.py runserver
   ```

6. Access the admin panel at:
   ```
   http://localhost:8000/admin
   ```

---

## 📤 Deployment (Render)

This app is hosted on **Render** using a **native Python environment**. When deploying, the app will use your env variables to create a super user in order to control the admin panel. The environment variables you need to set are:
SECRET_KEY=
DEBUG=True
DB_NAME=personal_portfolio
DB_USER=
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=5432
ALLOWED_HOSTS=127.0.0.1,localhost
CORS_ALLOWED_ORIGINS=http://127.0.0.1:5173,http://localhost:5173
DJANGO_SUPERUSER_USERNAME
DJANGO_SUPERUSER_EMAIL
DJANGO_SUPERUSER_PASSWORD

If on development, you have to first create the databas in PostgreSQL along with the database user you will use to connect to the database (the default is fine for development).

The DJANGO_* environment variables are used for creating the admin super user automatically.

Auto-deploy is triggered on `git push` to the main branch.

---

## 📄 License

This project is for personal use and learning.  
Feel free to explore and learn from it.

---

## 🔗 Related Projects

- Frontend repo: [Vue Portfolio](https://bayardolopez.com)

