from .protocol_a import CalculatePerimeter


class Triangle(CalculatePerimeter):
    def __init__(self, side_1: int, side_2: int, side_3: int) -> None:
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def calculate_perimeter(self) -> str:
        message = "O perímetro do triângulo é de "\
          f"{self.side_1 + self.side_2 + self.side_3} cm"
        return message


triangle = Triangle(5, 5, 5)
print(triangle.calculate_perimeter())
