from overrides import override

from app.apps.movie.models import Director
from app.apps.movie.service.interface.application.application import MovieServiceInterface


class MovieApplication(MovieServiceInterface):
    @override
    def find_movie(self, movie_id: int) -> Director:
        pass


