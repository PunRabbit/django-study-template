from abc import ABCMeta, abstractmethod
from app.apps.movie.models import Director


class MovieServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def find_movie(self, movie_id: int) -> Director:
        pass
