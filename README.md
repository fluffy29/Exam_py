# Python Web Apps: Django + Flask

This repository demonstrates two different web frameworks within a single project structure:

1. A **Django** application under `school_management/`.
2. A **Flask** application defined in `app.py` (with templates and static files in the `Flask-project-to-fix` folder).

## Project Overview

```
exam_pythonforwebapp-main
├── Flask-project-to-fix
│   ├── static
│   │   └── styles.css
│   └── templates
│       └── dashboard.html
├── app.py            # Main Flask application
├── README.md         
└── school_management
    ├── data_management
    │   ├── admin.py
    │   ├── apps.py   # Contains DataManagementConfig
    │   ├── models.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   └── __init__.py
    │   ├── serializers.py
    │   ├── tests.py
    │   └── views.py
    ├── school_management
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    ├── db.sqlite3
    └── manage.py
    ├──README.md # Project README (this file)
```

### 1) Django: `school_management`

The `school_management` directory is a **Django** project containing an example “app” named `data_management`.  
- **`data_management/apps.py`**: Here you’ll find `DataManagementConfig`, which is a standard `AppConfig` subclass used by Django to configure certain app-level behaviors.

You can explore or run the Django project by:

```bash
cd school_management
python manage.py runserver
```

This should launch the Django server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/) by default (unless you specify another port).

#### Relevant Files in Django
- `settings.py`, `urls.py`, `wsgi.py`, `asgi.py`: Core Django configuration.
- `data_management/`: Where the models, admin configuration, migrations, and other Django-specific modules for this app live.
- `db.sqlite3`: Default SQLite database file created by Django.

### 2) Flask: `app.py`

Separately, this project includes a **Flask** application:
- **`app.py`**: The primary Flask file, which:
  - Uses [Faker](https://pypi.org/project/Faker/) to generate random data (students, subjects, and grades).
  - Calculates average grades and ranking.
  - Renders a simple dashboard (via the `dashboard.html` template).
- **`Flask-project-to-fix/static/styles.css`**: A basic stylesheet for the Flask dashboard.
- **`Flask-project-to-fix/templates/dashboard.html`**: A Jinja2 template that displays the generated data.

To run the Flask app:

```bash
python app.py
```

By default, Flask runs on [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Installation

1. **Install Python 3**  
   Ensure you have Python 3 on your machine:
   ```bash
   python --version
   ```
   or  
   ```bash
   python3 --version
   ```

2. **Install Required Packages**  
   - **Django** (for the Django project)
   - **Flask** and **Faker** (for the Flask project)  

   For example:
   ```bash
   pip install django flask faker
   ```
   *(If you prefer using a virtual environment, create and activate one before installing.)*

## Usage

### Running the Django Project

1. Move into the `school_management` folder:
   ```bash
   cd school_management
   ```
2. Run migrations to ensure your database is up to date (optional if you have no new models to migrate):
   ```bash
   python manage.py migrate
   ```
3. Start the server:
   ```bash
   python manage.py runserver
   ```
4. Open a browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### Running the Flask App

1. In the **root** of the project (where `app.py` is located), run:
   ```bash
   python app.py
   ```
2. Open a browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Project Highlights

- **Django**  
  - `data_management/apps.py` shows a minimal `AppConfig` with the standard `default_auto_field` setting.
  - A typical Django file structure is in place (models, views, admin, migrations, etc.).

- **Flask**  
  - Demonstrates random data generation with Faker.
  - Basic example of using Jinja2 templates to display data (ranking, averages, etc.).
  - Simple route (`"/"`) that renders `dashboard.html`.

## Customization

- **Django**  
  - Add or modify models in `data_management/models.py`.
  - Update URLs and views in `school_management/urls.py` and `data_management/views.py`.
  - Adjust settings in `school_management/settings.py` (e.g., database configuration, installed apps, etc.).

- **Flask**  
  - Edit the subjects, number of students, or grading logic within `generate_fake_data()` in `app.py`.
  - Adjust the style or layout of the dashboard in `Flask-project-to-fix/templates/dashboard.html` and `static/styles.css`.

