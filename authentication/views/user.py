from http import HTTPStatus
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from authentication.serializers.user import UserBasicSerializer, UserSerializer

class AuthViewset(viewsets.ViewSet):

    @action(detail=False, methods=['get'], url_path='me', permission_classes=[IsAuthenticated])
    def me(self, request):
        return Response(UserBasicSerializer(request.user).data)

    @action(detail=False, methods=['post'], url_path='login', permission_classes=[])
    def login(self, request):
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password'),
        )
        if user is None:
            return Response(data={'msg': 'Invalid credentials'}, status=HTTPStatus.UNAUTHORIZED)
        login(request, user)
        if user and user.is_authenticated:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'token': token.key}, status=HTTPStatus.OK)
        return Response(status=HTTPStatus.UNAUTHORIZED)

    @action(detail=False, methods=['post'], url_path='logout', permission_classes=[IsAuthenticated])
    def logout(self, request):
        user = request.user
        if user and user.is_authenticated:
            Token.objects.filter(user=user).delete()
        logout(request)
        return Response(status=HTTPStatus.ACCEPTED)

    @action(detail=False, methods=['post'], url_path='register', permission_classes=[])
    def register(self, request):
        if not self.__validate_user_data(request.data):
            return Response(data={'msg': 'Invalid user data'}, status=HTTPStatus.BAD_REQUEST)
        try:
            user = User.objects.create_user(
                first_name=request.data.get('first_name'),
                last_name=request.data.get('last_name'),
                username=request.data.get('username'),
                email=request.data.get('email'),
                password=request.data.get('password'),
            )
            group = Group.objects.get(name='Client')
            group.user_set.add(user)
        except Exception as e:
            return Response(data={'msg': 'User is already registered'}, status=HTTPStatus.BAD_REQUEST)
        return Response(status=HTTPStatus.CREATED)

    def __validate_user_data(self, user_data):
        cond = []
        cond.append(user_data.get('first_name') is not None)
        cond.append(user_data.get('last_name') is not None)
        cond.append(user_data.get('username') is not None)
        cond.append(user_data.get('email') is not None)
        cond.append(user_data.get('password') is not None)
        return all(cond)

    @action(detail=False, methods=['put'], url_path='update_profile', permission_classes=[IsAuthenticated])
    def update_profile(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profile updated successfully"})
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)

    @action(detail=False, methods=['delete'], url_path='unsubscribe', permission_classes=[IsAuthenticated])
    def unsubscribe(self, request):
        user = request.user
        user.is_active = False
        user.save()
        return Response({"message": "User unsubscribed successfully"})
