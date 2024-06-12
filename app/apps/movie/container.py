from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton

from app.apps.movie.service.interface.application.application import MovieServiceInterface
from app.apps.movie.service.interface.module.repo import MovieRepoInterface
from app.apps.movie.service.interface.module.verify import MovieVerifyInterface


class MovieContainer(DeclarativeContainer):
    _repo_manager: MovieRepoInterface = Singleton()
    _verify_manager: MovieVerifyInterface = Singleton()

    service: MovieServiceInterface = Singleton()



