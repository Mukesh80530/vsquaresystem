# Invoice Generator 
this is a simple project for coding test for Invoice Generator, project includes Python, Django, and Django Rest framework.

Steps to run the Project:
1. Create a project folder i.e. Invoice Generator.
2. cd to  Invoice Generator.
3. Make a virtual environment for the project using the command, python3 -m venv env.
4. Activate the virtual environment using the command source, env/bin/activate.
5. Install project dependencies using the command, pip install -r requirements.txt.
6. To Run the project: cd to where manage.py file is present and Make migrations using,
     python manage.py makemigrations.
     python manage.py migrate.
     python manage.py runserver 4000
7. Access at http://127.0.0.1:4000

# Endpoints
9. To create an invoice object, make a POST request to http://127.0.0.1:4000/invoices/.
    ##
    Url:- http://127.0.0.1:4000/invoices/
    Method:- POST
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = 'date=2023-08-14'
    response:{
     "id": 5,
     "items": [],
     "date": "2023-08-14"
    }

11. To get all invoice objects, make a GET request to http://127.0.0.1:4000/invoices/.
    URL:-  http://127.0.0.1:4000/invoices/
    Method: GET
    headers: {}
    payload: {}
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
    URL:- http://127.0.0.1:8000/invoice-items/
    Method: GET
    headers: {}
    payload: {}
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
    Url:- http://127.0.0.1:4000/invoice-items/
    Method:- POST
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = 'units=2&description=bags&amount=399&invoice=5'
    response:{
    "id": 4,
    "units": 2,
    "description": "bags",
    "amount": "399.00",
    "invoice": 5     
    }
