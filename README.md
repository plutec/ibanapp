# IBANAPP

## Google API creation
- Create a new project in: https://console.developers.google.com
- In the left hand, click on "Credentials" and create a new one (OAuth client) for Web.
- Introduce a name, and the permited redirections (for testing):
  - http://localhost:8000/auth/complete/google-oauth2/
- Save all and write the new credentials (Client ID and client secret) in the file local_settings.py

## Run tests
This project uses vagrant to run the test environment, do the following:
- Join in the project folder
- ```vagrant up```
- Provisioning must be done during *up*, but if it does not happens, run: ```vagrant provision```
- ```vagrant ssh```
- ```cd /vagrant/ibanapp/```
- ```tox```

### Run development server
If you prefer to run the server to check the application manually, you must start vagrant as the previous steps, going to the application folder and run:
```
python3 manage.py runserver
```

