from flask import Flask
from movie_controller import movie_controller


app = Flask(__name__)
app.template_folder = ""
app.static_folder = ""


app.register_blueprint(movie_controller, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
