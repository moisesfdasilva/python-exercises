from models.car_model import Cars


def get_all() -> list[dict]:
    all_cars = Cars.query.all()
    cars = list()

    for car in all_cars:
        cars.append({
            "brand": car.brand,
            "model": car.model,
            "year": car.year})

    return cars
