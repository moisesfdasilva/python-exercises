from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from controllers.car_controller import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
