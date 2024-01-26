class Animal:
    def __init__(self, name: str) -> None:
        self.name = name


class FlyMixin:
    def fly(self) -> None:
        print("Pássaro voando...")


class Bird(Animal, FlyMixin):
    def __init__(self, name: str) -> None:
        super().__init__(name)


bird = Bird("Pardal")
bird.fly()  # Pássaro voando...
