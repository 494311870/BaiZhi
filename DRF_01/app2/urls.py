from django.urls import path

from app2.views import BookAPIView,BookGenericAPIView,BookViewSetView

urlpatterns = [
    path("books/", BookAPIView.as_view()),
    path("books/<str:id>/", BookAPIView.as_view()),

    path("g/books/", BookGenericAPIView.as_view()),
    path("g/books/<str:id>/", BookGenericAPIView.as_view()),

    # 这着实看着有些难受，为什么要在这里进行绑定
    path("s/books/", BookViewSetView.as_view({"post": "user_login", "get": "get_user"})),
    path("s/books/<str:id>/", BookViewSetView.as_view({"post": "user_login", "get": "get_user"})),

]
