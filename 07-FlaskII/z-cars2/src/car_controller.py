from flask import Blueprint, make_response, jsonify
from models.car_model import get_all


car_controller = Blueprint("car_controller", __name__)


@car_controller.route("/all", methods=["GET"])
def get_cars():
    cars = get_all()
    return make_response(jsonify(
        mensage="Cars List",
        data=cars))
