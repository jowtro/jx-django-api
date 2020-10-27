from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),

    # posts endpoints
    path('api/', include('posts.urls')),
    # Auth
    path('api/auth/signup', views.signup),
    path('api/auth/login', views.ObtainExpiringAuthToken.as_view()),
]
