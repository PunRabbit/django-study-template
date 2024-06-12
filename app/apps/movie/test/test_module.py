from django.test import TestCase
from unittest.mock import patch

from app.apps.movie.service.interface.module.repo import MovieRepoInterface
from app.apps.movie.service.interface.module.verify import MovieVerifyInterface
from app.apps.movie.container import MovieContainer


class MovieModuleTest(TestCase):
    def setUp(self) -> None:
        self.container: MovieContainer = MovieContainer()
