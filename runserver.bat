@echo off
REM Lancement de docker-compose up
docker-compose up -d

REM Attendre quelques secondes pour s'assurer que les conteneurs sont démarrés
timeout /t 10

REM Exécution des migrations Django
docker-compose exec web python manage.py migrate
