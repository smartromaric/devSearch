@echo off

REM Créer un environnement virtuel
python -m venv venv3

REM Activer l'environnement virtuel
venv\Scripts\activate.bat
cd ../..
REM Installer les dépendances
pip install -r requirements.txt

REM Lancer la commande
python manage.py runserver
