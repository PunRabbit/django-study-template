from overrides import override

from app.apps.movie.service.interface.domain.dto import MovieInfo
from app.apps.movie.service.interface.domain.application import MovieServiceInterface
from app.apps.movie.service.interface.module.verify import MovieVerifyInterface


class MovieApplication(MovieServiceInterface):
    def __init__(self, verify_module: MovieVerifyInterface):
        self.verify_module = verify_module

    @override
    def find_movie(self, movie_id: int) -> MovieInfo:
        pass

    @override
    def test_mock(self) -> bool:
        return self.verify_module.verify_movie_name(name='test')


