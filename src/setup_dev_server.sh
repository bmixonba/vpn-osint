#!/bin/bash

source .env/bin/activate
export FLASK_APP=frontend
export FLASK_ENV=development
flask run
