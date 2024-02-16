from flask import Blueprint, render_template
from model.book_model import book_a


book_controller = Blueprint("book_controller", __name__)


@book_controller.route("/", methods=["GET"])
def index():
    return render_template(
        "book.html",
        title=book_a.title,
        author=book_a.author,
        year=book_a.year)
