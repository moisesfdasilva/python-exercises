class Rectangle:
    def __init__(self, base: int, height: int) -> None:
        self.base = base
        self.height = height

    def calculate_area(self) -> int:
        return self.base * self.height

    def calculate_perimeter(self) -> int:
        return (2 * self.base) + (2 * self.height)


rectangle_a = Rectangle(base=5, height=10)
rectangle_a.calculate_area()
rectangle_a.calculate_perimeter()
