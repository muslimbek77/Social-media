from django.shortcuts import render

# Create your views here.
# POSTLIST
# POSTCREATE
# 1ta view

from post.models import Post
from post.serializers import PostDetailSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import GenericAPIView

class RetrieveUpdatePost(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericAPIView):

    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class UserList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


