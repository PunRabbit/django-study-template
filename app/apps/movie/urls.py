from django.urls import path
from app.apps.movie.views import MovieDetailView
from app.apps.movie.container import MovieContainer

container: MovieContainer = MovieContainer()
container.wire(modules=[__name__])

urlpatterns = [
    path('movies/<int:movie_id>/', MovieDetailView.as_view(), name='movie-detail'),
]
