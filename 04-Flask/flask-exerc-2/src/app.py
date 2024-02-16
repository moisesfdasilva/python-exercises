from flask import Flask
from controller.book_controller import book_controller


app = Flask(__name__)
app.template_folder = "views/templates"


app.register_blueprint(book_controller, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
