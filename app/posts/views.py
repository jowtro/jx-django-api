from posts.serializers import PostSerializer
from posts.models import Post
from django.shortcuts import render
from rest_framework import generics


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
