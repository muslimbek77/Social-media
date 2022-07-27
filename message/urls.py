
from django.urls import path
from .views import ChatListViewSet, MessageListViewSet



urlpatterns = [
    path("api/chat/", ChatListViewSet.as_view()),
    path("api/message/", MessageListViewSet.as_view()),
    

]