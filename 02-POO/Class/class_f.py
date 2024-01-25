def list_to_sum(values: list[int]) -> int:
    result = 0

    for num in values:
        result = result + num

    return result


def list_animals(animals: list[str], char: str) -> list[str]:
    result = []

    for animal in animals:
        if animal[0] is char[0]:
            result.append(animal)

    return result


class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self) -> None:
        print(f"{self.title}",
              f"by {self.author}",
              f"contains {self.pages} pages")


book_a = Book("Mozart in the Jungle: Sex, Drugs, and Classical Music",
              "Blair Tindall", 336)
book_a.describe()


class Car:
    def __init__(self, model: str, year: int, speed: int) -> None:
        self.model = model
        self.year = year
        self.speed = speed

    def speed_up(self) -> None:
        print(f"{self.model}, year {self.year}, speed up 30km/k")

    def slow_down(self) -> None:
        print(f"{self.model}, year {self.year}, slow down 10km/k")


car_a = Car("Fiat Uno", 1994, 220)
car_a.speed_up()
car_a.slow_down()
