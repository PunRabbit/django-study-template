from overrides import override

from app.apps.movie.service.interface.module.verify import MovieVerifyInterface


class MovieVerifyManager(MovieVerifyInterface):
    @override
    def verify_movie_name(self, name: str) -> bool:
        pass

