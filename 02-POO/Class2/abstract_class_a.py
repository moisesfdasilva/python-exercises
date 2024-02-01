from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def name(self) -> None:
        pass


class Seller(Person):
    def __init__(self, your_name: str) -> None:
        self.your_name = your_name

    def name(self) -> None:
        print(f"Seu nome é: {self.your_name}")
