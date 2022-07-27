from django.urls import path
from post.views import UserList,RetrieveUpdatePost


urlpatterns = [
    path("api/", UserList.as_view()),
    path("api/update/<int:pk>", RetrieveUpdatePost.as_view()),
    ]