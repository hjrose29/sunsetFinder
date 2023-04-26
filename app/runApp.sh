#!/bin/bash

virtualenv venv 
source env/bin/activate 
export FLASK_APP=app
export FLASK_ENV=development 
flask run