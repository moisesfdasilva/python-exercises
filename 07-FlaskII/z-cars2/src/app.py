from flask import Flask
from car_controller import car_controller


app = Flask(__name__)
app.config["JASON_SORT_KEYS"] = False
app.register_blueprint(car_controller, url_prefix="/cars")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
