from flask import Flask
from controller.home_controller import home_controller


app = Flask(__name__)
app.static_folder = "views/static"
app.template_folder = "views/templates"


app.register_blueprint(home_controller, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8800)
