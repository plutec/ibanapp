# IBANAPP

## Prerequisites
In order to develop and test this system, **vagrant** and **virtualbox** are required in your host machine.

## Preparing the environment
This project uses vagrant to run the test environment, do the following:
- Join in the project folder
- ```vagrant up```
- Provisioning must be done during *up*, but if it does not happens, run: ```vagrant provision```
- ```vagrant ssh```
- Now, we must create only the first time the database and the username with:
- ```sudo su - postgres```
- ```cd /vagrant```
- ```psql -f configure_db.sql```

## Preparing the tests
- We must create a superuser in the django application:
- ```cd /vagrant/ibanapp/```
- ```pipenv install --dev```
- ```pipenv shell```
- ```python3 manage.py migrate```
- ```python3 manage.py createsuperuser```
- And introduce the first admin data (this last step is optional to run the tests)

## Run tests
After preparing the environment, we can run the test joining in the virtual machine with
- ```vagrant ssh```
- And running the complete test suite (pylint, flake8 and django tests)
- ```cd /vagrant```
- ```tox```

## Google API creation
- Create a new project in: https://console.developers.google.com
- In the left hand, click on "Credentials" and create a new one (OAuth client) for Web.
- Introduce a name, and the permited redirections (for testing):
  - http://localhost:8000/auth/complete/google-oauth2/
- Save all and write the new credentials (Client ID and client secret) in the file local_settings.py

### Run development server
If you prefer to run the server to check the application manually, you must start vagrant as the previous steps, going to the application folder and run:
```
python3 manage.py runserver 0.0.0.0:8000
```
And in your host machine, go to http://127.0.0.1:8000 in order to see the result.
