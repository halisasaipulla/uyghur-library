# Uyghur Library - Capstone Project

## Introduction

Uyghur Library is a web application that allows users to read and download Uyghur books and upload PDFs and a picture from their own gallery as a book cover for their upload. Users are provided a page to bookmark their favorite reads and also leave comments on any book in the library. They have the ability to send inquiries and send messages via the contact form that the administrators will receive. Users also have the option to translate the page in three different languages, for now: Uyghur, English, and Korean.


## Demo
<a style="float:right" href="https://drive.google.com/file/d/1V9Jtk1-W13fCYQs8ofLgf5UDIszEZUSv/view?usp=sharing" target="_blank">
  <img alt="Uyghur Library" width="800" src="https://i.ibb.co/vvFBBy1/vizlator.png" />
</a>

## Skills Assessed

- Following directions and reading comprehension
- Demonstrating understanding of the client-server model, request-response cycle and conventional RESTful routes
- Driving development with independent research, experimentation, and collaboration
- Using git as part of the development workflow

- Working with the Django framework:
    - Creating models
    - Creating conventional RESTful CRUD routes for models
    - Reading query parameters to create custom behavior
    - Create unconventional routes for custom behavior
    - Creating a many-to-many relationship between two models 
- (Books to Users, Comments to Books, Favorites to Users)

## Installation
1. Clone this repository.
2. Create virtual environment:
mkdir django
cd django
python3 -m venv django
source django/bin/activate

3. Install Django in the virtual environment
	pip install Django
4. Set up the project and run: 	
	cd Desktop
mkdir mysite
cd mysite
django-admin startproject mysite
5. Navigate into the outer directory where manage.py script exists and run the below command.
	cd mysite
python manage.py startapp blog
6. Install apps in settings.py file
7. Apply migrations: 
	python manage.py migrate

8. Start server by running:
python3 manage.py runserver
9. Open your browser and go to this address http://127.0.0.1:8000/ if everything went well you should see this page.



10. Define Database Models and make migrations:
	python manage.py makemigrations 
	python manage.py migrate
11. Create an administration site and super user
	python manage.py createsuperuser
12. Build views:
	A Django view is just a Python function that receives a web request and returns a web response. 
13. Add URL patterns for views
14. Create templates for views
