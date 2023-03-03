from rest_framework import serializers
from .models import RatingChoices, Movie, MovieOrder
from users.serializers import UserSerializer

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, default=None)
    synopsis = serializers.CharField(allow_null=True, default=None, required=False)
    rating = serializers.ChoiceField(choices= RatingChoices.choices, default=RatingChoices.G, allow_null=True)
    added_by = serializers.SerializerMethodField(method_name='user_added')
    user = UserSerializer(required=False)


    def user_added(self, obj:Movie):
        email = Movie.objects.get(id = obj.id).user.email
        return email

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        print(movie)
        return movie        

class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField(read_only=True, method_name='title_movie')
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField(read_only=True, method_name='user_bought')
    buyed_at = serializers.DateTimeField(read_only=True)
    

    def get_title_movie(self, obj:MovieOrder):
        title = Movie.objects.get(id = obj.movie_id).title
        return title

    def get_user_bought(self, obj:MovieOrder):
        return obj.user.email       

    def create(self, validated_data):
        movie = MovieOrder.objects.create(**validated_data)

        return movie