# Django App for a SQL database management

Python version: python3.7

It's highly recommended to create a virtual environment. After activating the virtual environment, run the following command from the project home directory to install dependencies:

```
pip install -r requirements.txt
```

Run the following commands to create the appropriate tables in the database
```
python manage.py makemigrations
python manage.py migrate
```

The following command takes the Input CSV file and parses it while putting it in the sql tables:
```
python parse_csv.py 
```

To start the server run the following command:

```
python manage.py runserver
```

By default, the server should be accessible at ```http://127.0.0.1:8000/```
