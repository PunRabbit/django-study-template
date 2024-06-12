from abc import ABCMeta, abstractmethod

from app.apps.movie.service.interface.domain.dto import MovieInfo


class MovieServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def find_movie(self, movie_id: int) -> MovieInfo:
        pass
