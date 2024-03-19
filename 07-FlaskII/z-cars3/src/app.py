from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = \
  "mysql+pymysql://root:password@127.0.0.1:3306/z_cars2"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100))
    model = db.Column(db.String(100))
    year = db.Column(db.Integer)


@app.route("/cars/all", methods=["GET"])
def get_all():
    all_cars = Car.query.all()
    print("__________________________A")
    cars_json = [car.to_json() for car in all_cars]
    print("__________________________B")

    return Response(cars_json)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
