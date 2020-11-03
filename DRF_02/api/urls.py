from django.urls import path
from rest_framework_jwt.views import ObtainJSONWebToken, obtain_jwt_token

from api.views import UserDetailAPIView,LoginAPIView,ComputerListAPIView

urlpatterns = [
    path("login/", ObtainJSONWebToken.as_view()),
    path("detail/", UserDetailAPIView.as_view()),
    path("user/", LoginAPIView.as_view()),
    path("com/", ComputerListAPIView.as_view()),
]
