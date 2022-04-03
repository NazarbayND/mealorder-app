# Meal Ordering App

## Environment requirements

- python 
- pipenv
- mysql
- docker (Optional)

## Installation

### Clone project from repository

`git clone git@github.com:NazarbayND/mealorder-app.git`


### Install pip dependencies

`pipenv install`

### Create a database and Add Credentials of Database

Create MySQL database for mealorder
In 'mealorder/settings.py' file on DATABASES section change credentials for database

### Migrate database schema

`python manage.py makemigrations`

`python manage.py migrate`

### Run the project

`python manage.py runserver`
