from flask import make_response, jsonify
from services import car_service
from app import app


@app.route("/cars", methods=["GET"])
def get_all():
    cars = car_service.get_all()
    response_json = jsonify({
        "mensage": "Cars List",
        "data": cars})
    return make_response(response_json)
