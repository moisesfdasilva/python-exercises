from flask import Flask
from controllers.student_controller import student_controller


app = Flask(__name__)
app.template_folder = "views/template"
app.static_folder = "views/static"


app.register_blueprint(student_controller, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
