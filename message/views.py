from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from message.models import Message,Chat

from message.serializers import ChatSerializer, MessageSerializer

class ChatListViewSet(generics.ListAPIView):
    
    serializer_class = ChatSerializer
    def get_queryset(self):
        queryset = Chat.objects.all()
        return Chat.objects.filter(members=self.request.user)
   
    

class MessageListViewSet(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    