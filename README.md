# Django Book Catalogue

A simple book catalogue application with clean UI.

## Features

- Manage authors and books with CRUD operations
- Clean, simple user interface
- Django admin interface
- Comprehensive testing

## Requirements

- Python 3.13
- Poetry

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-book-catalogue.git
   cd django-book-catalogue
   

2. Install dependencies using Poetry:

   ```powershell
   poetry install
   
3. Activate the virtual environment:

   ```powershell
   poetry shell

Note: this poetry shell might not work if your poetry version is equal or above poetry 2.0.0, 
please use 'poetry env activate ' and follow instruction in the powershell to activate virtual environment.


4. Apply database migrations:

   ```powershell
   python manage.py migrate

5. Create a superuser (optional):

   ```powershell
   python manage.py createsuperuser
   
Running the Application

6. Start the development server:

   ```powershell
   python manage.py runserver

## Access the application at:

Home: http://localhost:8000/

Authors: http://localhost:8000/authors/

Books: http://localhost:8000/books/

Admin: http://localhost:8000/admin/



## Testing
The project includes a comprehensive test suite using pytest.

## Running Tests
1. Make sure you're in the Poetry shell:

   ```powershell
   poetry shell
   
Note: this poetry shell might not work if your poetry version is equal or above poetry 2.0.0, 
please use 'poetry env activate ' and follow instruction in the powershell to activate virtual environment.

If you are not using poetry shell, then you have to use 'poetry run' beore any test command below
2. Run all tests:

   ```powershell
      pytest




Running Specific Tests

## Run a specific test file:

   ```powershell
Model Tests: pytest books/tests/test_models.py

View Tests: pytest books/tests/test_views.py

URL Tests: pytest books/tests/test_urls.py

Form Tests: pytest books/tests/test_forms.py






## Run a single test:

   ```powershell
   pytest books/tests/test_models.py::TestBookModel -v



## Things to add in future:

   1. User Manangement additon, Django has very simple feature for this
   2. Authenticate users before creation or deletion of Author and Books
   2. Add Dockerfile and docker-compose.yml file to contenarize with Docker
   3. Change Database to PostgreSQL
   4. Add Sentry-sdk for catching erros in the application
   5. Consider to add and swithc to Djago REST Framework ( DRF) if needed
   5. And many more.....