from flask import Flask, make_response, jsonify, request
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="z_cars",
)

app = Flask(__name__)
app.config["JASON_SORT_KEYS"] = False


@app.route("/cars", methods=["GET"])
def get_cars():
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM cars")
    cars_db = my_cursor.fetchall()

    cars = list()
    for car in cars_db:
        cars.append({
            "id": car[0],
            "brand": car[1],
            "model": car[2],
            "year": car[3]})

    return make_response(jsonify(
        mensage="Cars List",
        data=cars))


# @app.route("/cars", methods=["POST"])
# def create_car():
#     car = request.json

#     my_cursor = mydb.cursor()
#     query = "INSERT INTO cars (brand, model, year)"\
#       f"VALUES ('{car['brand']}', '{car['model']}', '{car['year']})'"
#     my_cursor.execute(query)
#     mydb.commit()

#     return make_response(jsonify(
#         mensage="Cars List",
#         data=cars))
