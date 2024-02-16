from flask import Blueprint, render_template
from models.student_model import StudentsModel


student_controller = Blueprint("student_controller", __name__)


@student_controller.route("/students", methods=["GET"])
def get_all():
    all_students = StudentsModel.get_all()

    return render_template(
        "students.html",
        students=all_students)
