class Product:
    def __init__(self, price: float) -> None:
        self.price = price

    def print_price(self) -> None:
        message = "Classes derivadas de Product precisam"\
          " implementar o método print_price."
        raise NotImplementedError(message)


class Book(Product):
    def __init__(self, price: float) -> None:
        super().__init__(price)

    def print_price(self) -> None:
        print(f"O preço do livro é: {self.price}")


book = Book(10)
book.print_price()
