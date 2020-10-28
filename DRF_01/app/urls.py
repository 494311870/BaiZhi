from django.urls import path
from app.views import UserView, StudentAPIView, TeacherAPIView

urlpatterns = [

    path("user_view/", UserView.as_view()),
    path("user_view/<str:id>/", UserView.as_view()),

    path("student/", StudentAPIView.as_view()),

    path("teacher/", TeacherAPIView.as_view()),
    path("teacher/<str:id>/", TeacherAPIView.as_view()),

]
