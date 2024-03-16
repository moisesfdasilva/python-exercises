from .db import mydb


def get_all() -> list:
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

    return cars
