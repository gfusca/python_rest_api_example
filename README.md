# Python REST API Test example

Example for testing a rest api using python request + flask

## Environment configuration
1. Install virtualenv

`$ sudo apt-get install virtuaenv`

2. Virtualenv configuration
  
  2.1 Generate virtualenv config
    `$ virtualenv .`
  
  2.2 Activate virtualenv
    `$ source bin/activate`

3. Install python packages

  `$ pip install flask`

  `$ pip install flask-httpauth`
  
  `$ pip install Flask-API`

  `$ pip install requests`

## Execute
To execute unit tests:

1. Start flask rest server (rest server run on localhost:5000):
  `$ python app.py`
2. Run unittest:
  `$ python rest_tester.py`


