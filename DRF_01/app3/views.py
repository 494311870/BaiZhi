from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly

from app3.authentications import MyAuth
from app3.models import User
from app3.permission import MyPermission
from app3.throttle import SendMessageRate


class Demo(APIView):
    authentication_classes = [MyAuth]

    def get(self, request, *args, **kwargs):
        user = User.objects.first()
        print(user)
        print(user.groups.first())
        print(user.user_permissions.first())

        return Response("OK")


class UserAPIView(APIView):
    # authentication_classes = [MyAuth]
    # permission_classes = [MyPermission]

    throttle_classes = [SendMessageRate]

    def get(self, request, *args, **kwargs):
        print("读请求")
        return Response("读请求")

    def post(self, request, *args, **kwargs):
        print("写请求")
        return Response("写请求")
