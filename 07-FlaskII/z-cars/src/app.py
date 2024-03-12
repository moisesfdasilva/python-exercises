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


@app.route("/car/<car_id>", methods=["GET"])
def get_car(car_id):
    my_cursor = mydb.cursor()
    query = f"SELECT * FROM cars WHERE id={car_id}"
    my_cursor.execute(query)
    car_db = my_cursor.fetchall()[0]

    car = {
        "id": car_db[0],
        "brand": car_db[1],
        "model": car_db[2],
        "year": car_db[3]}

    return make_response(jsonify(
        mensage="Car",
        data=car))


@app.route("/car", methods=["POST"])
def create_car():
    car = request.json

    my_cursor = mydb.cursor()
    query = f"INSERT INTO cars (brand, model, year) VALUES ('{car['brand']}',"\
        f"'{car['model']}', {car['year']})"
    my_cursor.execute(query)
    mydb.commit()

    return make_response(jsonify(
        mensage="Car created",
        data=car))


@app.route("/car/<car_id>", methods=["PUT"])
def update_car(car_id):
    car = request.json
    my_cursor = mydb.cursor()
    query = f"UPDATE cars SET brand={car['brand']}, model={car['model']}, "\
        f"year={car['year']} WHERE id={car_id}"
    my_cursor.execute(query)
    mydb.commit()
    return make_response(jsonify(
        mensage="Car updated",
        data=car))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
