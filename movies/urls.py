from django.urls import path
from .views import MovieView, MovieDetaView, MovieOrderView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieDetaView.as_view()),
    path("movies/<int:movie_id>/orders/", MovieOrderView.as_view()),
]