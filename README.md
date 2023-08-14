# Invoice Generator 
this is a simple project for coding test for Invoice Generator, project includes Python, Django, and Django Rest framework.

# 1. Steps to run the Project - Django Rest Framework
1. Create a project folder i.e. Invoice Generator.
2. cd to  Invoice Generator.
3. Make a virtual environment for the project using the command, python3 -m venv env.
4. Activate the virtual environment using the command source, env/bin/activate.
5. Install project dependencies using the command, pip install -r requirements.txt.
6. To Run the project: cd to where the manage.py file is present and Make migrations using,
     python manage.py makemigrations.
     python manage.py migrate.
     python manage.py runserver 4000
7. Access the URL at http://127.0.0.1:4000

# 2. Endpoints - Postman
9. To create an invoice object, make a POST request to http://127.0.0.1:4000/invoices/.
    ##
    Url:- http://127.0.0.1:4000/invoices/<br/>
    Method:- POST<br/>
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }<br/>
    payload = 'date=2023-08-14'<br/>
    response:{
     "id": 5,
     "items": [],
     "date": "2023-08-14"
    }

11. To get all invoice objects, make a GET request to http://127.0.0.1:4000/invoices/.
    ##
    URL:-  http://127.0.0.1:4000/invoices/<br/>
    Method: GET<br/>
    headers: {}<br/>
    payload: {}<br/>
    Sample Response:[
        {
        "id": 1,
        "items": [
            {
                "id": 1,
                "units": 59,
                "description": "shoes",
                "amount": "400.00",
                "invoice": 1
            }
        ],
        "date": "0023-08-12"
    },
    ]
    
13. To retrieve all invoice item objects, you can use GET requests to http://127.0.0.1:4000/invoice-items/
    ##
    URL:- http://127.0.0.1:8000/invoice-items/<br/>
    Method: GET<br/>
    headers: {}<br/>
    payload: {}<br/>
    Sample Response:[
        {
        "id": 1,
        "units": 59,
        "description": "shoes",
        "amount": "400.00",
        "invoice": 1
     },
    ]
    
15. To create an invoice items object, you can use POST requests to http://127.0.0.1:4000/invoice-items/.
    ##
    Url:- http://127.0.0.1:4000/invoice-items/<br/>
    Method:- POST<br/>
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }<br/>
    payload = 'units=2&description=bags&amount=399&invoice=5'<br/>
    response:{
    "id": 4,
    "units": 2,
    "description": "bags",
    "amount": "399.00",
    "invoice": 5     
    }
