# my-web-app
Setup
Fork and clone the repo, then navigate there from the command-line:

cd my-web-app-12/
Setup and activate the virtual environment, and install package dependencies:

pipenv install
pipenv shell
Setup the database:

FLASK_APP=web_app flask db init
FLASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade
Usage
Run the app:

FLASK_APP=web_app flask run
Then visit localhost:5000 in the browser!

# Windows:
set FLASK_APP=app.py # one-time thing, to set the env var
flask run