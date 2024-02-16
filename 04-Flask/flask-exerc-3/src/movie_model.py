class Movie():
    def __init__(self, title: str, year: int) -> None:
        self.title = title
        self.year = year


def get_movies_list() -> list[Movie]:
    movies_tuple = [
        ("Bloodsport", 1988),
        ("Crouching Tiger, Hidden Dragon", 2000),
        ("The Grandmaster", 2013),
        ("The Warlords", 2007),
        ("Enter the Dragon", 1973),
    ]
    movies = list()

    for movie in movies_tuple:
        movies.append(Movie(title=movie[0], year=movie[1]))

    return movies
