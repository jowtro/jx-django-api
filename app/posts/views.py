from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import PostSerializer, VoteSerializer
from .models import Post, Vote
# from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status



class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


class PostRetrieveDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        post = Post.objects.filter(pk=kwargs['pk'],
                                   poster=self.request.user)
        if post.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError(r"This isn't your post to update or it doesn't exist.")

    def delete(self, request, *args, **kwargs):
        post = Post.objects.filter(pk=kwargs['pk'],
                                   poster=self.request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError(r"This isn't your post to delete or it doesn't exist.")


class VoteCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user, post=post)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('You have already voted for this post :)')
        serializer.save(voter=self.request.user,
                        post=Post.objects.get(pk=self.kwargs['pk']))

    # accepts delete request based on URL bond to this class
    def delete(self, request, *args, **kwargs):
        """An user can delete his own vote

        Args:
            request (any): default args

        Raises:
            ValidationError: Something bad will happen

        Returns:
            http_status: Will return http 204
        """
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('You never voted for this post...')
