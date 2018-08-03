# Meat Up

Meat up is an application to host events.

## Technologies Used

* Python 3.7
* Django framework 2.0
* PostgreSQL
* Bootstrap 4.1.3 CSS framework
* jQuery 3.3.1 JS framework

## Features in the application

* Has authentication based on email address
* Email address client side validation using HTML5
* Authentication validation on server side with graceful error on client
* We use Django template to create the base layout of the app
* About page with team member details
* Responsive app design using Bootstrap CSS
* Integrated with Zomato API Widget to display nearby restaurants

## Hacking

To start hacking on this project, you will need to install the following dependencies once:

```
$ pip3 install Pillow
$ pip install django-extensions
```

To build and run the development server:

```
$ python3 manage.py runserver
```

The website will start at http://localhost:8080

## Updating Database Model

Whenever we change a database model class under `models.py` we need
to run the following commands:

```
// to generate the DDL commands from python source code
$ python3 manage.py makemigrations

// to update the database tables under DB
$ python3 manage.py migrate
```
