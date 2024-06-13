from django.test import TestCase
from unittest.mock import patch, create_autospec

from app.apps.movie.service.interface.module.verify import MovieVerifyInterface
from app.apps.movie.container import MovieContainer


class MovieModuleTest(TestCase):
    container: MovieContainer

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.container: MovieContainer = MovieContainer()
        cls.container.wire(modules=[__name__])
    
    def setUp(self) -> None:
        self.verify_manager: MovieVerifyInterface = self.container._verify_manager()

    def test_non_mock_verify(self) -> None:
        self.assertEquals(True, self.verify_manager.verify_movie_name(name='test'))

    def test_verify(self) -> None:
        mock_verify_instance = create_autospec(MovieVerifyInterface)
        mock_verify_instance.verify_movie_name.return_value = False

        self.verify_manager = mock_verify_instance

        result = self.verify_manager.verify_movie_name(name='test')
        print(f"Result: {result}")

        self.assertEquals(False, result)

        mock_verify_instance.verify_movie_name.assert_called_once_with(name='test')



