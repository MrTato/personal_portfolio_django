# 🌐 Personal Portfolio Website

This is a personal portfolio website built with **Vue 3** and **Django**. It showcases my blog posts and personal projects with a clean, dark-themed, responsive design. I’m using this project to hone my full-stack development skills while creating something personally meaningful.

---

## ✨ Features

### 📝 Blog Section
- Posts written and managed via Django Admin  
- Rendered in Vue using Markdown ([Marked.js](https://marked.js.org/))  
- Public comments with spam and self-promotion filtering

### 💼 Project Showcase
- Gallery of project cards with screenshots, tech stack, and links  
- Dedicated detail pages for each project  
- Content managed through Django Admin

### 📬 Contact Form
- Sends emails directly to my inbox  
- Client-side validation

### 🌍 Multilingual Support
- Toggle between English and Spanish using [Vue I18n](https://vue-i18n.intlify.dev/)

### 🌑 Dark Theme
- Responsive layout for mobile and desktop  
- Based on a free dark [Figma](https://www.figma.com/) template

---

## 🛠 Tech Stack

### 🔹 Frontend
- [Vue 3](https://vuejs.org/)  
- [Vue Router](https://router.vuejs.org/)  
- [Axios](https://axios-http.com/)  
- [Marked.js](https://marked.js.org/)  
- [Vue I18n](https://vue-i18n.intlify.dev/)

### 🔹 Backend
- [Python 3](https://www.python.org/)  
- [Django](https://www.djangoproject.com/)  
- [Django REST Framework](https://www.django-rest-framework.org/)  
- [PostgreSQL](https://www.postgresql.org/)  
- [django-markdownx](https://neutronx.github.io/django-markdownx/)  
- [django-cors-headers](https://pypi.org/project/django-cors-headers/)

### 🔹 Hosting
- [DigitalOcean](https://www.digitalocean.com/) VPS  
- [Gunicorn](https://gunicorn.org/) + [Nginx](https://www.nginx.com/)  
- Manual deployment (for now)

## 🚀 Getting Started

### 🔧 Prerequisites
- Python 3.13.2  
- PostgreSQL
- Virtualenv

### ▶️ Backend Setup
1. Activate venv
```
source personal_portfolio_venv/bin/activate
```

2. Install requirements
```
pip install -r requirements.txt
```

3. Run Development server
```
python manage.py runserver
```

4. Create a super user to access admin panel
```
python manage.py createsuperuser
```

5. Run the migrations
```
python manage.py makemigrations
python manage.py migrate
```

6. You can access the admin panel via http://localhost:8000/admin

### 🖥️ Useful commands
When you install a new library, use this to update the requirements.txt file
```
pip freeze > requirements.txt
```

Running tests
```
python manage.py test
```

For generating database documentation
```
python manage.py spectacular --color --file schema.yml
```

For collecting static files
```
python manage.py collectstatic
```

### 🪲 Troubleshooting