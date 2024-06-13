from django.test import TestCase
from unittest.mock import patch, create_autospec

from app.apps.movie.service.interface.domain.application import MovieServiceInterface
from app.apps.movie.container import MovieContainer


class MovieApplicationTest(TestCase):
    def setUp(self) -> None:
        self.container: MovieContainer = MovieContainer()
        self.container.wire(modules=[__name__])
        self.service: MovieServiceInterface = self.container.service()

    def test_application(self) -> None:
        pass





