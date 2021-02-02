# Django Bug Tracker
This is a simple bug tracking application built with Python and the Django framework. It allows for two types of users; admins and users. Admins can create new tickets and assign them to users. Users can make progress on tickets and leave comments. 

## To run
After cloning the repo, open a terminal in the project's directory and run the following commands to install and activate the virtual environment. 
```bash
poetry install
poetry shell
```
Create a super user:
```bash
python manage.py createsuperuser
```
Push changes to the sql server:
```bash
python manage.py makemigrations
python manage.py migrate
```
Finally run the server
```bash
python manage.py runserver
```

Log in the the superuser account or create a new user.