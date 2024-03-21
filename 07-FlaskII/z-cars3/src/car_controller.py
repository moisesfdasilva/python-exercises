from flask import make_response, jsonify
from car_model import Cars
from app import app


@app.route("/cars/all", methods=["GET"])
def get_all():
    all_cars = Cars.query.all()
    print(all_cars)
    # cars_json = [car.to_json() for car in all_cars]

    return make_response(jsonify(
        mensage="Cars List",
        data="cars"))
