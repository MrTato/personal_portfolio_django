# 🛠️ Django Backend for Personal Portfolio

This is the backend API for my personal portfolio site. Built with **Django** and **Django REST Framework**, it serves blog content to a Vue 3 frontend. The backend is read-only for the public and fully managed via the Django Admin panel. It is designed to be lightweight, secure, and easy to maintain.

---

## 🚀 Features

- 📝 **Blog API**  
  - Markdown-based content storage (rendered client-side)  
  - Draft support via `published` field  
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
  - Static files served via WhiteNoise  
  - Media files served via AWS S3 (production only)

---

## 🛠 Tech Stack

### 🔹 Core
- [Django 5.x](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [drf-spectacular](https://drf-spectacular.readthedocs.io/)
- [PostgreSQL](https://www.postgresql.org/)

### 🔹 Middleware & Storage
- [WhiteNoise](https://whitenoise.evans.io/) for static file handling
- [django-cors-headers](https://pypi.org/project/django-cors-headers/)
- [django-storages](https://django-storages.readthedocs.io/) + [AWS S3](https://aws.amazon.com/s3/) for production media storage

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

This app is hosted on **Render** using a **native Python environment**. Auto-deployment is triggered on every `git push` to the main branch.

In production, static files are served via WhiteNoise, while media files (like uploaded images) are stored and served via **AWS S3**, using `django-storages`.

### 🔐 Required Environment Variables

- `SECRET_KEY`: The Django secret key
- `DEBUG`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`
- `ALLOWED_HOSTS`: comma-separated values
- `CORS_ALLOWED_ORIGINS`: comma-separated values as well
- `DJANGO_SUPERUSER_USERNAME`: automatic super user creation. Keep it here
- `DJANGO_SUPERUSER_EMAIL`: automatic super user creation. Keep it 
- `DJANGO_SUPERUSER_PASSWORD`: automatic super user creation
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_STORAGE_BUCKET_NAME`

Make sure to create your PostgreSQL database and user in development before applying migrations.

The `DJANGO_SUPERUSER_*` variables allow Render to auto-create an admin user on deployment.

---

## 🔗 Related Projects

- Frontend repo: [Vue Portfolio](https://bayardolopez.com)

---

## 📄 License

This project is for personal use and learning.  
Feel free to explore and learn from it.