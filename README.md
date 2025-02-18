# DjangoResume - Personal Resume Portfolio

A Django-based web application to showcase your resume and portfolio. This project allows you to dynamically manage and display your professional details, skills, projects, and more.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/prasadsheetal/DjangoResume.git
cd DjangoResume
```

### 2. Create and Activate a Virtual Environment (Recommended)
To prevent conflicts with system dependencies, create a virtual environment:

```sh
python -m venv venv
```
Activate the virtual environment:

Windows:
```sh
venv\Scripts\activate
```
Mac/Linux:

```sh
venv/bin/activate
```
### 3. Install Dependencies
Run the following command to install required dependencies:

```sh
pip install -r requirements.txt
```

### 4. Apply Database Migrations
Run the following command to set up the database:

```sh
python manage.py migrate
```

If requirements.txt is missing, manually install Django:

```sh
pip install django
```
 ### 5. Run the Development Server
Start the Django application:

```sh

python manage.py runserver
```
The application will be available at:
🌐 http://127.0.0.1:8000/

### Project Structure
**djangoresume/** - The main Django project directory.  
├── **knownebetter/** - The app directory containing templates, views, models, and URLs.  
├── **static/** - Directory for static files like CSS.  
├── **templates/** - Directory containing HTML templates.  
└── **requirements.txt** - File to list Python dependencies.  
