"TO DO LIST" PROJECT.
HOW TO USE:
1. This project use django as the framework of the project.
2. Clone this project
3. Install these parts on your command prompt/terminal:
a. pip install django (add django framework).
b. pip install -r requirements.txt (Make sure to check if there is a 'requirements.txt' file in the project directory. If it exists, running this command will install all listed dependencies).
c. python -m venv venv (create virtual environment).
d. pip install reportlab django (add requirement for download data in pdf file).
e. pip install python-decouple (to hide sensitive data in ".env" file).
4. Set up the database:
- type your database data in file "settings.py" (see on the project directory).
- if you want to hide your database data, then create file ".env" and install python-decouple.
- use "config" to hide your data (if you want).
- copy the model class of this project in "models.py" file into yours.
- type on your command prompt/terminal: python manage.py makemigrations.
- type on your command prompt/terminal: python manage.py migrate.
5. Register the models in the Django administration in "admin.py" file (you can copy of this project).
6. Access your database with django administration.
- type on your command prompt/terminal: python manage.py createsuperuser.
(after finished create super user, then run the server).
7. LOGIN METHOD
=> If you want to login to the website with your google account, install this on your command prompt: pip install django-allauth
=> If you want to login to the website with the default from of the website, you can use "mailtrap", you can set the information of mailtrap in "settings.py"
8. Run the server
- type on your command prompt/terminal: python manage.py runserver.
- copy this link on your browser url: http://localhost:8000/.
9. Access django administration with your super user account.
- access this url: http://localhost:8000/admin.

Feel free to share your idea with your contributions on this project 🫡