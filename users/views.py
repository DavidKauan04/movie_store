from rest_framework.views import APIView, Request, Response, status
from .permissions import PermissionIsSuper
from .serializers import UserSerializer
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404

# Create your views here.

class UserView(APIView):
    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [PermissionIsSuper]

    def get(self, req: Request, user_id:int) -> Response:
        user = get_object_or_404(User, id=user_id)

        self.check_object_permissions(req, user)
        serializer = UserSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)