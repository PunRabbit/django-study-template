from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from dependency_injector.wiring import inject, Provide

from app.apps.movie.service.interface.domain.application import MovieServiceInterface
from app.apps.movie.service.interface.domain.dto import MovieInfo
from app.apps.movie.container import MovieContainer
from app.apps.movie.serializer.view_serializer import MovieInfoSerializer


class MovieDetailView(APIView):
    @inject
    def __init__(self, movie_service: MovieServiceInterface = Provide[MovieContainer.service], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.movie_service: MovieServiceInterface = movie_service

    def get(self, request: Request, movie_id: int) -> Response:
        movie_info: MovieInfo = self.movie_service.find_movie(movie_id=movie_id)
        return Response(
            MovieInfoSerializer(movie_info).data, status=status.HTTP_200_OK
        )

