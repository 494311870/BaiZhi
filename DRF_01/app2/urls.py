from django.urls import path

from app2.views import BookAPIView

urlpatterns = [
    path("books/", BookAPIView.as_view()),
    path("books/<str:id>/", BookAPIView.as_view()),

]
