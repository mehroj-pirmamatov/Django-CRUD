Django CRUD

A simple and practical Book Management CRUD application built with Python and Django. The project demonstrates the four basic database operations: Create, Read, Update, and Delete.

Features

View all books in a clean list

Add a new book

Edit existing book information

Delete books

Store data in a local SQLite database

Django admin panel support

Responsive interface powered by Bootstrap

Tech Stack

Python

Django

SQLite3

HTML5

Bootstrap

Django Templates
Project Structure
Plain Text

Django-CRUD/
├── app/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── templates/
│   ├── base.html
│   ├── form.html
│   └── index.html
├── manage.py
└── README.md



Data Models

Book

The Book model contains the following fields:

•
name — book title

•
author — author's name

•
info — additional information about the book

•
price — book price

•
created_at — record creation date

Category

The project also includes a Category model with:

•
name — category name

•
created_at — record creation date

Getting Started

1. Clone the repository

Bash


git clone https://github.com/mehroj-pirmamatov/Django-CRUD.git
cd Django-CRUD



2. Create a virtual environment

Windows

Bash


python -m venv venv
venv\Scripts\activate



macOS/Linux

Bash


python3 -m venv venv
source venv/bin/activate



3. Install Django

This project does not currently include a requirements.txt file, so install Django manually:

Bash


pip install django



4. Apply database migrations

Bash


python manage.py migrate



5. Start the development server

Bash


python manage.py runserver



Open the application in your browser:

Plain Text


http://127.0.0.1:8000/



Available Routes

Route
Method
Description
/
GET
Display all books
/add/
GET, POST
Add a new book
/edit/<id>/
GET, POST
Edit a book
/delete/<id>/
GET
Delete a book
/admin/
GET
Open the Django admin panel




Create an Admin User

To access the Django admin panel, create a superuser:

Bash


python manage.py createsuperuser



Then open:

Plain Text


http://127.0.0.1:8000/admin/



Usage

1.
Open the home page to see the list of books.

2.
Click Create to add a new book.

3.
Use Edit to update a book's information.

4.
Use Delete to remove a book from the database.

5.
Use the admin panel for Django administration.

Development Notes

This project is intended for learning and development purposes. Before deploying it to production, consider the following improvements:

•
Move the Django SECRET_KEY to environment variables.

•
Set DEBUG = False in production.

•
Configure ALLOWED_HOSTS properly.

•
Add a requirements.txt file with pinned dependencies.

•
Use POST requests for delete operations and add confirmation prompts.

•
Add automated tests for CRUD operations.

•
Add form validation with Django Forms or ModelForms.

Contributing

Contributions are welcome. To contribute:

1.
Fork the repository.

2.
Create a new branch:

Bash


git checkout -b feature/your-feature





3.
Make your changes.

4.
Commit your changes:

Bash


git commit -m "Add your feature"





5.
Push the branch and open a pull request.

License

This project is available for educational and personal use. You may adapt and improve it as needed.

Author

Mehroj Pirmamatov

•
GitHub: 

@mehroj-pirmamatov

•
Repository: 

Django-CRUD

