# Necessary imports for authentication
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.timezone import now
from rest_framework_simplejwt.serializers import TokenVerifySerializer
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import viewsets

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.core.exceptions import ValidationError
import logging

logger = logging.getLogger(__name__)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            # Log the error and also send it back in the response for debugging
            logger.error(f'Error creating user: {str(e)}')
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class IsAdminUser(permissions.BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        print(request.user)

        return bool(request.user and request.user.is_authenticated and request.user.role == 'admin')

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class VerifyTokenView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = TokenVerifySerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            return Response({'valid': True}, status=status.HTTP_200_OK)
        except TokenError as e:
            return Response({'valid': False, 'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['id'] = user.id
        token['role'] = user.role
        token['picture'] = user.picture.url if user.picture else None
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserRegister(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response({"message": "User Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestView(APIView):
    queryset = User.objects.all()

    def get(self, request):
        return Response({"message": "You are authenticated"}, status=status.HTTP_200_OK)

