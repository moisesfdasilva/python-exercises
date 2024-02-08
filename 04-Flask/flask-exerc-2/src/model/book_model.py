class Book():
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year


book_a = Book(
    title="Ensaio sobre a Cegueira",
    author="José Saramago",
    year=1995)
