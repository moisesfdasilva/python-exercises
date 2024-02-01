class Car:
    def __init__(self, brand: str, model: str, year: str, color: str) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def identify(self) -> None:
        print(f"Meu carro é um {self.model}, da {self.brand}.",
              f" Ele é do ano {self.year} e tem a cor {self.color}")
