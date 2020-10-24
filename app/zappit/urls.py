from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts', views.PostList.as_view()),
    path('api/posts/<int:pk>', views.PostRetrieveDestroy.as_view()),
    path('api/posts/<int:pk>/vote', views.VoteCreate.as_view()),
    path('api/auth', include('rest_framework.urls')),

]
