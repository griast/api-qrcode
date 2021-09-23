## Activate the environment
    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat 
## Install Dependencies
    $ pip install -r requirements.txt
## Run APP
    $ set FLASK_APP=app.py
    $ set FLASK_ENV=development
    $ flask run
## Build Docker
    $ docker build -t anva-qrcode:latest .
    $ docker run -d -p 5000:5000 anva-qrcode


## REF
    - https://flask.palletsprojects.com/en/2.0.x/api/#
    - https://marcoagner.github.io/Flask-QRcode/
    - https://github.com/lincolnloop/python-qrcode
