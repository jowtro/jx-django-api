from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    # Posts
    path('', include('rest_framework.urls')),
    path('posts', views.PostListCreate.as_view()),
    path('posts/<int:pk>', views.PostRetrieveDestroy.as_view()),
    path('posts/<int:pk>/vote', views.VoteCreate.as_view()),

    # Auth
    path('auth/signup', views.signup),
    path('auth/login', views.login),
]
