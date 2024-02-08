from flask import Blueprint, render_template
from models.student_model import StudentsModel


student_controller = Blueprint("student_controller", __name__)


@student_controller.route("/students", methods=["GET"])
def index():
    return render_template(
        "alunos.html",
        students=[
            {"name": "Elena Rybakina", "register": "005"},
            {"name": "Danielle Collins", "register": "071"},
        ])
