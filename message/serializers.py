from rest_framework import serializers
from .models import Chat,Message


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
        # depth = 1

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('text','image','chat')
        # depth = 1