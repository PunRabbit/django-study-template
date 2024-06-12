from dataclasses import dataclass

from app.apps.movie.models import Director


@dataclass(frozen=True)
class MovieInfo:
    movie_info: Director
    is_valid: bool

