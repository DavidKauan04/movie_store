from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Movie
from .serializers import MovieSerializer, MovieOrderSerializer
from django.shortcuts import get_object_or_404
from .permissions import MyCustomPermissionMovie, IsAuthenticated
from project.pagination import SourcePageNumberPagination

# Create your views here.

class MovieView(APIView, SourcePageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermissionMovie] 

    def get(self, req:Request) -> Response:
        movies = Movie.objects.all()
        result = self.paginate_queryset(movies, req, view=self)
        serializer = MovieSerializer(result, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, req:Request)  -> Response:
        serializer = MovieSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=req.user)

        return Response(serializer.data, status.HTTP_201_CREATED)

class MovieDetaView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermissionMovie]     

    def get(self, req:Request, movie_id:int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)

        return Response(serializer.data, 200)


    def delete(self, req:Request, movie_id:int) -> Response:
        movie = get_object_or_404(Movie, id = movie_id)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, req:Request, movie_id: int)  -> Response:

        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieOrderSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=req.user, movie=movie)

        return Response(serializer.data, status.HTTP_201_CREATED)