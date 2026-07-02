# to create virtual environment
python -m venv venv

# to activate virtual environment
powershell|windows = .\venv\scripts\activate
git|mac|linux = source venv/scripts/activate

# to install django
pip install django

# to create new project
django-admin startproject (projectname)

# to run local server
python manage.py runserver

# to create app
python manage.py startapp (appname)