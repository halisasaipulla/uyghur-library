# Uyghur Library - Capstone Project

## Introduction

Uyghur Library is a web application that allows users to read and download Uyghur books and upload PDFs and a picture from their own gallery as a book cover for their upload. Users are provided a page to bookmark their favorite reads and also leave comments on any book in the library. They have the ability to send inquiries and send messages via the contact form that the administrators will receive. Users also have the option to translate the page in three different languages, for now: Uyghur, English, and Korean.


## <a href="https://uyghur-library-capstone.herokuapp.com/">Demo</a>
  <img alt="Uyghur Library" width="800" src="Screen Shot 2021-08-17 at 21.11.51.png" /> 
  <img alt="Uyghur Library" width="800" src="Screen Shot 2021-08-17 at 21.08.52.png" />


## Things we've learned
- Demonstrating understanding of the client-server model, request-response cycle and conventional RESTful routes
- Driving development with independent research, experimentation, and collaboration
- Using git as part of the development workflow
- Working with the Django framework:
    - Creating models
    - Creating conventional RESTful CRUD routes for models
    - Reading query parameters to create custom behavior
    - Create unconventional routes for custom behavior
    - Creating a many-to-many relationship between two models (Books to Users, Comments to Books, Favorites to Users)

## Installation
1. Clone this repository
  ```bash
   git clone https://github.com/lisa1501/uyghur-library.git
   cd uyghur-library
  ``` 
2. Create virtual environment:
  ```bash
  mkdir django
  cd django
  python3 -m venv django
  source django/bin/activate
  ```
3. Install Django in the virtual environment
  ```bash
  pip install Django
  cd..
  ```
4. Set up the project and run:
  ```bash
  mkdir mysite
  cd mysite
  django-admin startproject mysite
  ```
5. Navigate into the outer directory where manage.py script exists:
  ```bash
  cd mysite
  python manage.py startapp library
  ```
6. Apply migrations:
  ```bash
  python manage.py migrate
  ```
7. Start server by running:
  ```bash
  python3 manage.py runserver
  ```
8. Open your browser and go to this address
  ```bash
  http://127.0.0.1:8000/
  ```
   if everything went well you should see this page.

  <img alt="Django" width="800" src="Screen Shot 2021-08-17 at 21.20.06.png" />
  
9. Install requirements:
  ```bash
  cd ..
  cd ..
  pip install -r requirements.txt
  ```
10. Create a .env file with the following variables:
  ```bash
  SECRET_KEY=" "
  DEBUG_VALUE="True"
  TZ="America/Los_Angeles"
  AWS_ACCESS_KEY_ID=" "
  AWS_SECRET_ACCESS_KEY=" "
  AWS_STORAGE_BUCKET_NAME=" "
  EMAIL_HOST_USER=" "
  EMAIL_HOST_PASSWORD=" "
  ```
      
11.  Define Database Models and make migrations:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
12.  Start the server by running:
  ```bash
  python3 manage.py runserver
  ```
13.  Create an administration site and super user:
  ```bash
  python manage.py createsuperuser
  
  http://127.0.0.1:8000/admin
  ```
