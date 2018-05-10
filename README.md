# DjangoRest-Login

## How to setup the environment?

cd to the file you download or clone

### 1. First - create virtual environment
```
For Windows:
python -m venv env
cd env/Scripts
activate
cd ../..

For MacOS:
$ python3 -m venv env
$ source env/bin/activate
```

### 2. Second - config backend
`cd backend`
Create a file named 'config.ini'.
Wrtie your own email 'host', 'port', 'user' and 'password' as the file 'config.templete'.
The server will use the email to send registration email to users.
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 3. Third - config frontend
```
npm install
npm run start
```

## Now, you can go to http://localhost:8080 to run the webapp.
