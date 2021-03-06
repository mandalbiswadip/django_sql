# Django App for a SQL database management

Python version: python3.7<br>
Mysql version: 8.0.25

1. First clone the project.<br>
2. Create the MySQL database using the following command

```mysql -u root -e 'create database contact_db'```

3. **Install Requirements**

It's highly recommended creating a virtual environment. After activating the virtual environment, run the following command from the project home directory to install dependencies:

```
pip install -r requirements.txt
```
4. **Run migrations**<br>
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

5. **Run server**
```
python manage.py runserver
```

By default, the server should be accessible at ```http://127.0.0.1:8000/```

Go through the user guide for instructions on how to use the web app.
