# Para iniciar um ambiente virtual em Python
python -m pip install --upgrade pip
python -m pip install django

python -m venv venv
.\venv\Scripts\activate

# Para desativar o ambiente virtual
deactivate

# Iniciar um projeto
django-admin startproject {project_name} {directory}
manage.py runserver