<!-- Project Title -->
Coding Website

<!-- Installation -->
1. Clone this repository
2. Create "virtual environment" with command prompt: python -m venv venv
3. Activate "virtual environment" with command prompt: env\scripts\activate
4. Install django with command prompt: pip install django
5. Use dependency with: pip install -r requirements.txt
6. LOGIN METHOD
=> If you want to login to the website with your google account, use this on your command prompt: pip install django-allauth
=> If you want to login to the website with the default from of the website, you can use "mailtrap", you can set the informatio of mailtrap in "settings.py"
7. Don't forget to set up with your database, then put in file "settings.py"
7. Migrate the database (use with terminal/command prompt): python manage.py makemigrations
8. Execute the migration with: python manage.py migrate

<!-- Alternate -->
If you want to use "config" like on my code, you can install it on your command prompt: pip install python-decouple

<!-- Run the server -->
1. Run the server (use with terminal): python manage.py runserver
2. Copy the link: http://127.0.0.1:8000/ into your browser

<!-- Contribution -->
Feel free to share your idea or revision of this project