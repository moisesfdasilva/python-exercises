from flask import Flask, make_response, jsonify
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="z_cars2",
)

app = Flask(__name__)
app.config["JASON_SORT_KEYS"] = False


@app.route("/cars", methods=["GET"])
def get_cars():
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM cars;")
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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
