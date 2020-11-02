from django.urls import path

from app3.views import UserAPIView,Demo

urlpatterns = [

    path("user/", UserAPIView.as_view()),
    path("demo/", Demo.as_view()),


]
