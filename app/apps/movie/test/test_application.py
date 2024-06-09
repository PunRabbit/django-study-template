from django.test import TestCase
from django.test.utils import tag
from dependency_injector.providers import Singleton
from typing import Union
from unittest.mock import patch, create_autospec, Mock

from app.apps.movie.service.interface.domain.application import MovieServiceInterface
from app.apps.movie.service.interface.module.verify import MovieVerifyInterface
from app.apps.movie.container import MovieContainer


@tag('with_mocking')
class MovieApplicationTest(TestCase):
    def setUp(self) -> None:
        self.container: MovieContainer = MovieContainer()
        self.container.wire(modules=[__name__])
        self.service: Union[Singleton, MovieServiceInterface] = self.container.service()

    def test_application(self) -> None:
        mock_verify = create_autospec(MovieVerifyInterface)
        mock_verify.verify_movie_name.return_value = False

        self.service.verify_module = mock_verify
        self.assertEquals(False, self.service.test_mock())

    def test_mocking(self) -> None:
        self.assertEquals(False, self.service.test_mock())


