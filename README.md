# vsquaresystem
this is a simple project for coding test for vsquaresystem, project includes Python, Django, and Django Rest framework.

Steps to run the Project:
1. Create a project folder i.e. vsquaresystem.
2. cd to vsquaresystem.
3. Make a virtual environment for the project using the command, python3 -m venv env.
4. Activate the virtual environment using the command source, env/bin/activate.
5. Install project dependencies using the command, pip install -r requirements.txt.
6. Make migrations using,
     python manage.py makemigrations.
     python manage.py migrate.
7. Run the project: cd to where manage.py is present and put, python manage.py runserver.
8. Access at http://127.0.0.1
9. To create an invoice, make a POST request to http://127.0.0.1/invoices/.
10. To create an invoice item, make a POST request to http://127.0.0.1/invoice-items/.
11. To retrieve invoices, you can use GET requests to http://127.0.0.1/invoices/.
12. To retrieve invoice items, you can use GET requests to http://127.0.0.1/invoice-items/.
