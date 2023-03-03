from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=127, validators=[UniqueValidator(queryset=User.objects.all(), message="email already registered.")])
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField(max_length=20, validators=[UniqueValidator(queryset=User.objects.all(), message="username already taken.")])
    password = serializers.CharField(write_only=True, max_length=127)
    is_employee = serializers.BooleanField(allow_null=True, default=False)
    is_superuser = serializers.BooleanField(read_only=True)
    birthdate = serializers.DateField(allow_null=True, required=False)

    def create(self, validated_data):
        if validated_data['is_employee']:
            user = User.objects.create_superuser(**validated_data)
            return user
        
        user = User.objects.create_user(**validated_data)
        return user