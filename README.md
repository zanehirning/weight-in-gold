# Django Gold Cost Calculator
This is a Django application that allows users to input their weight and calculates the cost of that weight in gold using a RESTful API. The application first converts the weight using a RESTful API, then makes another API call to get the current price of gold, and finally calculates the total cost of the gold.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
Python 3.9 and 
Django

## Installing
### Clone the repository to your local machine:
```python
git clone https://github.com/zanehirning/weight-in-gold.git
```
### Install the required packages:
pip install django

### Migrate the database:
```python
python manage.py makemigrations
python manage.py migrate
```

### Run the development server:
```python
python manage.py runserver
```

##Using the Gold Cost Calculator
Go to http://127.0.0.1:8000/ in your web browser.
Input your weight in the form field.
Click the "Calculate" button.
The cost of gold for your weight will be displayed on the page.

## Built With
Django - The web framework used
Python - Programming language
RESTful API - used for weight conversion
API - used for gold cost evaluation
## Authors
Zane Hirning - https://github.com/zanehirning
