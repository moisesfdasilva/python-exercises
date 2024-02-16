from flask import Blueprint, render_template
from movie_model import get_movies_list


movie_controller = Blueprint("movie_controller", __name__)


@movie_controller.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        movies=get_movies_list())
