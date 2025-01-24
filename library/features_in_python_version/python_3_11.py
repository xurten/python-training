"""
Marking individual TypedDict items as required or not-required
"""
from typing import TypedDict, Required
from typing_extensions import NotRequired


class Movie(TypedDict, total=False):
    title: Required[str]
    year: NotRequired[int]


def create_movie(title: str, year: int = None) -> Movie:
    """Create a Movie TypedDict with the given title and optional year."""
    return {"title": title, "year": year}


def display_movies(movies: list[Movie]) -> None:
    """Print the list of movies."""
    for movie in movies:
        print(movie)


if __name__ == '__main__':
    movies = [
        create_movie("Black Panther", 2018),    # OK
        create_movie("Star Wars"),              # OK (year is not required)
        create_movie(year=2022)                 # ERROR (missing required field title)
    ]
    display_movies(movies)