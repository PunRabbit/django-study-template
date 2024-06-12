from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Singleton

from app.apps.movie.service.interface.domain.application import MovieServiceInterface
from app.apps.movie.service.interface.module.verify import MovieVerifyInterface

from app.apps.movie.service.module.verify import MovieVerifyManager
from app.apps.movie.service.application.application import MovieApplication


class MovieContainer(DeclarativeContainer):
    _verify_manager: MovieVerifyInterface = Singleton(MovieVerifyManager)

    service: MovieServiceInterface = Singleton(MovieApplication, _verify_manager)

    def get_test_verify_manager(self) -> MovieVerifyInterface:
        return self._verify_manager

    # wiring_config = WiringConfiguration(
    #     modules=['app.apps.movie.service.application.application', 'app.apps.movie.views']
    # )




